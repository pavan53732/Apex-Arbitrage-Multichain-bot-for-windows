#!/usr/bin/env python3
"""
Dashboard Tree Structure Processor
Processes the massive dashboard folder tree in micro-chunks for quality control
"""

import re
from typing import List, Dict, Tuple, Any
import json

class TreeProcessor:
    def __init__(self):
        self.root_structure = {}
        self.current_path = []
        self.item_counts = {"folders": 0, "files": 0}

    def parse_line(self, line: str) -> Tuple[str, str, str]:
        """Parse a single line from the tree output"""
        stripped = line.strip()

        # Skip empty lines and header lines
        if not stripped or stripped.startswith("Folder PATH") or stripped.startswith("Volume serial"):
            return None, None, None

        # Count leading spaces to determine depth
        depth = (len(line) - len(line.lstrip())) // 4  # Assuming 4-space indentation

        # Extract item name and type
        if stripped.startswith("|   ") or stripped.startswith("+---") or stripped.startswith("\\---"):
            # Remove tree characters
            clean_name = re.sub(r'^[\+\|\\\-\-\-\s\|]*\s*', '', stripped)
            if clean_name:
                # Determine if it's a file or folder
                if stripped.startswith("|       ") or (depth > 0 and not stripped.startswith("+---") and not stripped.startswith("\\---")):
                    item_type = "file"
                elif ".md" in clean_name or ".js" in clean_name or ".jsx" in clean_name or ".json" in clean_name or ".css" in clean_name or ".scss" in clean_name or ".ts" in clean_name or ".py" in clean_name or ".csv" in clean_name or ".pdf" in clean_name or ".png" in clean_name or ".svg" in clean_name or ".jpg" in clean_name or ".ico" in clean_name or ".woff2" in clean_name or ".ttf" in clean_name or ".bin" in clean_name or ".onnx" in clean_name or ".glb" in clean_name or ".toml" in clean_name or ".ini" in clean_name or ".txt" in clean_name or ".log" in clean_name or ".xml" in clean_name or ".yaml" in clean_name or ".yml" in clean_name or ".enc" in clean_name or ".zip" in clean_name or ".html" in clean_name or ".sh" in clean_name or ".config.js" in clean_name:
                    item_type = "file"
                else:
                    item_type = "folder"
                return depth, item_type, clean_name

        return None, None, None

    def add_to_structure(self, depth: int, item_type: str, name: str):
        """Add item to the structure tree"""
        # Adjust current path based on depth
        while len(self.current_path) > depth:
            self.current_path.pop()

        if item_type == "folder":
            self.current_path.append(name)
            # Create nested dictionary structure
            current = self.root_structure
            for path_part in self.current_path:
                if path_part not in current:
                    current[path_part] = {"__files__": [], "__folders__": {}}
                current = current[path_part]["__folders__"]
            self.item_counts["folders"] += 1
        else:
            # Add file to current path
            current = self.root_structure
            for path_part in self.current_path:
                if path_part not in current:
                    current[path_part] = {"__files__": [], "__folders__": {}}
                current = current[path_part]["__folders__"]

            # Add to parent folder's files
            parent_folder = self.current_path[-1] if self.current_path else ""
            if parent_folder in self.root_structure and "__files__" in self.root_structure[parent_folder]:
                self.root_structure[parent_folder]["__files__"].append(name)
            else:
                self.root_structure.setdefault(parent_folder, {"__files__": [], "__folders__": {}})["__files__"].append(name)
            self.item_counts["files"] += 1

    def process_tree_file(self, filename: str):
        """Process the tree file line by line"""
        with open(filename, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                depth, item_type, name = self.parse_line(line)
                if depth is not None:
                    self.add_to_structure(depth, item_type, name)

    def get_sorted_structure(self) -> Dict:
        """Get the structure with alphabetically sorted folders and files"""
        def sort_structure(struct: Dict) -> Dict:
            result = {}

            # Sort folders first
            folders = []
            files = []

            for key, value in struct.items():
                if key.startswith("__"):
                    continue
                if isinstance(value, dict) and "__folders__" in value:
                    folders.append((key, value))
                else:
                    files.append((key, value))

            # Sort folders A-Z
            folders.sort(key=lambda x: x[0].lower())
            # Sort files A-Z
            files.sort(key=lambda x: x[0].lower())

            # Add folders first
            for folder_name, folder_content in folders:
                result[folder_name] = {
                    "__files__": sorted(folder_content.get("__files__", []), key=str.lower),
                    "__folders__": sort_structure(folder_content.get("__folders__", {}))
                }

            # Add files
            for file_name, file_content in files:
                result[file_name] = file_content

            return result

        return sort_structure(self.root_structure)

    def generate_formatted_output(self, structure: Dict, level: int = 0) -> str:
        """Generate the formatted output with proper numbering"""
        output = []
        indent = "    " * level

        # Process folders and files
        items = []
        for name, content in structure.items():
            if name.startswith("__"):
                continue
            items.append((name, content))

        # Sort items: folders first, then files
        folders = [(name, content) for name, content in items if isinstance(content, dict) and "__folders__" in content]
        files = [(name, content) for name, content in items if not isinstance(content, dict) or "__folders__" not in content]

        folders.sort(key=lambda x: x[0].lower())
        files.sort(key=lambda x: x[0].lower())

        all_items = folders + files

        total_items = len(all_items)
        for idx, (name, content) in enumerate(all_items, 1):
            if isinstance(content, dict) and "__folders__" in content:
                # This is a folder
                folder_files = content.get("__files__", [])
                total_files = len(folder_files)
                sub_folders = content.get("__folders__", {})
                sub_folder_count = len([k for k in sub_folders.keys() if not k.startswith("__")])

                output.append(f'{indent}├── FOLDER {idx}/{total_items}: {name}/')

                if folder_files:
                    for file_idx, file_name in enumerate(folder_files, 1):
                        output.append(f'{indent}│   ├── FILE {file_idx}/{total_files}: {file_name}')

                if sub_folders:
                    sub_output = self.generate_formatted_output(sub_folders, level + 1)
                    output.append(sub_output)
            else:
                # This is a file
                output.append(f'{indent}├── FILE {idx}/{total_items}: {name}')

        return '\n'.join(output)

    def process_in_chunks(self, structure: Dict, chunk_size: int = 10) -> List[str]:
        """Process the structure in chunks for quality control"""
        def flatten_structure(struct: Dict, path: str = "") -> List[Tuple[str, str, Dict]]:
            """Flatten the structure into a list of items"""
            items = []

            for name, content in struct.items():
                if name.startswith("__"):
                    continue

                current_path = f"{path}/{name}" if path else name

                if isinstance(content, dict) and "__folders__" in content:
                    # Folder
                    items.append((current_path, "folder", content))
                    # Recursively process subfolders
                    sub_items = flatten_structure(content.get("__folders__", {}), current_path)
                    items.extend(sub_items)
                else:
                    # File
                    items.append((current_path, "file", content))

            return items

        # Flatten the structure
        flat_items = flatten_structure(structure)

        # Process in chunks
        chunks = []
        for i in range(0, len(flat_items), chunk_size):
            chunk = flat_items[i:i + chunk_size]
            chunks.append(chunk)

        return chunks

def main():
    processor = TreeProcessor()

    # Process the tree file
    processor.process_tree_file("dashboard-tree.txt")

    print(f"Total folders: {processor.item_counts['folders']}")
    print(f"Total files: {processor.item_counts['files']}")

    # Get sorted structure
    sorted_structure = processor.get_sorted_structure()

    # Generate formatted output
    formatted_output = processor.generate_formatted_output(sorted_structure)

    # Write to output file
    with open("dashboard-structure-output.txt", "w", encoding="utf-8") as f:
        f.write("## COMPLETE FOLDER TREE STRUCTURE\n")
        f.write("FOLDER 1/1: dashboard/\n")
        f.write(formatted_output)
        f.write(f"\n\nTOTAL: {processor.item_counts['folders']} folders, {processor.item_counts['files']} files")

    print("Processing complete. Output written to dashboard-structure-output.txt")

if __name__ == "__main__":
    main()
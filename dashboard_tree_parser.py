#!/usr/bin/env python3
"""
Dashboard Tree Structure Parser
Parses the tree output and generates properly formatted structure
"""

import re
from typing import List, Dict, Tuple

def parse_tree_line(line: str) -> Tuple[int, str, str]:
    """Parse a single line from tree output"""
    stripped = line.strip()
    if not stripped or stripped.startswith("Folder PATH") or stripped.startswith("Volume serial"):
        return -1, None, None

    # Count indentation (4 spaces per level)
    depth = 0
    for char in line:
        if char == " ":
            depth += 1
        else:
            break
    depth = depth // 4

    # Extract name and type
    if "│" in stripped or "+" in stripped or "\\" in stripped:
        # Remove tree characters
        clean_name = re.sub(r'^[\+\|\\\-\-\-\s\|]*\s*', '', stripped).strip()
        if clean_name and clean_name != "":
            if clean_name.endswith('/') or not any(clean_name.endswith(ext) for ext in
                ['.md', '.js', '.jsx', '.json', '.css', '.scss', '.ts', '.py', '.csv',
                 '.pdf', '.png', '.svg', '.jpg', '.ico', '.woff2', '.ttf', '.bin',
                 '.onnx', '.glb', '.toml', '.ini', '.txt', '.log', '.xml', '.yaml',
                 '.yml', '.enc', '.zip', '.html', '.sh']):
                return depth, "folder", clean_name.rstrip('/')
            else:
                return depth, "file", clean_name

    return -1, None, None

def build_structure(lines: List[str]) -> Dict:
    """Build nested structure from parsed lines"""
    structure = {"dashboard": {"__files__": [], "__folders__": {}}}
    current_path = ["dashboard"]

    for line in lines:
        depth, item_type, name = parse_tree_line(line)
        if depth == -1:
            continue

        # Adjust current path based on depth
        while len(current_path) > depth + 1:
            current_path.pop()

        if item_type == "folder":
            current_path.append(name)
            # Create nested structure
            current = structure
            for part in current_path:
                if part not in current:
                    current[part] = {"__files__": [], "__folders__": {}}
                current = current[part]["__folders__"]
        else:
            # Add file to current folder
            current = structure
            for part in current_path:
                if part not in current:
                    current[part] = {"__files__": [], "__folders__": {}}
                current = current[part]["__folders__"]

            # Add to parent folder's files
            parent = current_path[-1]
            if parent in structure and "__files__" in structure[parent]:
                structure[parent]["__files__"].append(name)

    return structure

def generate_formatted_output(structure: Dict, level: int = 0) -> str:
    """Generate formatted output with proper numbering"""
    output = []
    indent = "    " * level

    # Get items and sort them
    items = []
    for name, content in structure.items():
        if name.startswith("__"):
            continue
        items.append((name, content))

    # Separate folders and files, sort alphabetically
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

            # Add files in this folder (if any)
            if folder_files:
                for file_idx, file_name in enumerate(folder_files, 1):
                    output.append(f'{indent}│   ├── FILE {file_idx}/{total_files}: {file_name}')

            # Add subfolders (if any)
            if sub_folders:
                sub_output = generate_formatted_output(sub_folders, level + 1)
                output.append(sub_output)
        else:
            # This is a file
            output.append(f'{indent}├── FILE {idx}/{total_items}: {name}')

    return '\n'.join(output)

def main():
    # Read the tree file
    with open("dashboard-tree.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Build structure
    structure = build_structure(lines)

    # Generate formatted output
    formatted_output = generate_formatted_output(structure["dashboard"]["__folders__"])

    # Write to output file
    with open("dashboard-structure-output.txt", "w", encoding="utf-8") as f:
        f.write("## COMPLETE FOLDER TREE STRUCTURE\n")
        f.write("FOLDER 1/1: dashboard/\n")
        f.write(formatted_output)
        f.write("\n\nTOTAL: Complete structure generated")

    print("Processing complete. Output written to dashboard-structure-output.txt")

if __name__ == "__main__":
    main()
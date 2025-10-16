#!/usr/bin/env python3
"""
Final Dashboard Structure Generator
Creates the complete dashboard folder tree structure with proper formatting
"""

import os
import json
from pathlib import Path

def get_dashboard_structure():
    """Get the complete dashboard directory structure"""
    dashboard_path = Path("Apex Arbitrage Multichain bot/dashboard")

    def scan_directory(directory, prefix=""):
        """Recursively scan directory and build structure"""
        items = []

        try:
            # Get all items in directory
            all_items = list(directory.iterdir())

            # Separate folders and files
            folders = [item for item in all_items if item.is_dir()]
            files = [item for item in all_items if item.is_file()]

            # Sort alphabetically (folders first, then files)
            folders.sort(key=lambda x: x.name.lower())
            files.sort(key=lambda x: x.name.lower())

            # Combine and number them
            numbered_items = []

            for i, folder in enumerate(folders, 1):
                folder_items = scan_directory(folder, prefix + "    ")
                items_in_folder = len(folder_items) if folder_items else 0
                numbered_items.append({
                    'type': 'folder',
                    'name': folder.name,
                    'path': str(folder.relative_to(dashboard_path)),
                    'items': folder_items
                })

            for i, file in enumerate(files, len(numbered_items) + 1):
                numbered_items.append({
                    'type': 'file',
                    'name': file.name,
                    'path': str(file.relative_to(dashboard_path))
                })

            return numbered_items

        except Exception as e:
            print(f"Error scanning {directory}: {e}")
            return []

    return scan_directory(dashboard_path)

def generate_formatted_output(structure, level=0):
    """Generate the formatted output with proper FOLDER X/Y and FILE X/Y numbering"""
    output = []
    indent = "    " * level

    total_items = len(structure)

    for idx, item in enumerate(structure, 1):
        if item['type'] == 'folder':
            # Count files and subfolders in this folder
            subfolders = [sub for sub in item['items'] if sub['type'] == 'folder']
            files = [sub for sub in item['items'] if sub['type'] == 'file']

            output.append(f'{indent}├── FOLDER {idx}/{total_items}: {item["name"]}/')

            # Add files in this folder
            for file_idx, file_item in enumerate(files, 1):
                output.append(f'{indent}│   ├── FILE {file_idx}/{len(files)}: {file_item["name"]}')

            # Add subfolders
            if subfolders:
                sub_output = generate_formatted_output(item['items'], level + 1)
                output.append(sub_output)

        else:
            # This is a file
            output.append(f'{indent}├── FILE {idx}/{total_items}: {item["name"]}')

    return '\n'.join(output)

def count_structure_items(structure):
    """Count total folders and files in structure"""
    folders = 0
    files = 0

    def count_recursive(items):
        nonlocal folders, files
        for item in items:
            if item['type'] == 'folder':
                folders += 1
                count_recursive(item['items'])
            else:
                files += 1

    count_recursive(structure)
    return folders, files

def main():
    print("Scanning dashboard directory structure...")

    # Get the structure
    structure = get_dashboard_structure()

    # Count items
    folders, files = count_structure_items(structure)
    print(f"Found {folders} folders and {files} files")

    # Generate formatted output
    formatted_output = generate_formatted_output(structure)

    # Write to output file
    with open("dashboard-complete-structure.txt", "w", encoding="utf-8") as f:
        f.write("## COMPLETE FOLDER TREE STRUCTURE\n")
        f.write("FOLDER 1/1: dashboard/\n")
        f.write(formatted_output)
        f.write(f"\n\nTOTAL: {folders} folders, {files} files")

    print("Processing complete. Output written to dashboard-complete-structure.txt")

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
"""
Clean Python script to fix character encoding corruption in generated-prompts folder.

Specifically fixes the 'â†' → '→' (right arrow) corruption that occurred due to
UTF-8 encoding issues in the PowerShell script.

Processes all prompt-*.md files in the generated-prompts folder.
"""

import os
import glob
import sys
from pathlib import Path


def fix_encoding_in_file(file_path):
    """
    Fix encoding corruption in a single file.

    Args:
        file_path (str): Path to the file to process

    Returns:
        int: Number of replacements made in the file
    """
    try:
        # Read file with UTF-8 encoding, handle potential decoding errors
        with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()

        original_content = content
        replacements_count = 0

        # Replace the corrupted sequence 'â†' with proper '→'
        if 'â†' in content:
            # Count occurrences before replacement
            replacements_count = content.count('â†')
            content = content.replace('â†', '→')

        # Only write back if content changed
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)

        return replacements_count

    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}", file=sys.stderr)
        return 0


def main():
    """Main function to process all prompt files in generated-prompts folder."""

    # Define the folder and pattern
    folder_path = "generated-prompts"
    pattern = os.path.join(folder_path, "prompt-*.md")

    # Find all matching files
    files = glob.glob(pattern)

    if not files:
        print(f"No files found matching pattern: {pattern}")
        print(f"Make sure you're running this script from the correct directory.")
        return 1

    total_files = len(files)
    total_replacements = 0
    files_with_changes = 0

    print(f"Found {total_files} files to process in {folder_path}/")
    print("Starting character encoding fix (â† → →)...\n")

    # Process each file
    for i, file_path in enumerate(sorted(files), 1):
        try:
            replacements_in_file = fix_encoding_in_file(file_path)

            if replacements_in_file > 0:
                files_with_changes += 1
                total_replacements += replacements_in_file
                print("2d")
            else:
                print("2d")

            # Show progress updates every 50 files or at the end
            if i % 50 == 0 or i == total_files:
                progress = f"[{i}/{total_files}]"
                print(f"{progress} Processed {i} files...")

        except Exception as e:
            print(f"Failed to process {file_path}: {str(e)}", file=sys.stderr)

    # Summary
    print("\nProcessing complete!")
    print(f"Total files processed: {total_files}")
    print(f"Files with encoding fixes: {files_with_changes}")
    print(f"Total â† → → replacements: {total_replacements}")

    if total_replacements > 0:
        print("\n✅ Character encoding corruption has been fixed!")
    else:
        print("\nℹ️  No corrupted characters found to fix.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
#!/usr/bin/env python3
"""
Bulk character replacement and encoding fix for corrupted emojis in prompt files.

This script processes all files matching the pattern generated-prompts/prompt-*.md
and replaces corrupted character sequences with their proper emoji equivalents.
"""

import os
import glob
from pathlib import Path


def fix_emojis_in_file(file_path):
    """
    Fix corrupted emojis in a single file.
    
    Args:
        file_path (str): Path to the file to process
        
    Returns:
        int: Number of replacements made in the file
    """
    # Define the mapping of corrupted sequences to proper emojis
    replacements = {
        'âœ…': '✅',  # checkmark
        'ðŸŽ¯': '🎯',  # target
        'â†\'' : '→',  # arrow
        'âŒ' : '❌',   # X mark
        'ðŸ"' : '📁',  # folder
        'o.': '✅',   # checkmark
        '+\'': '→',   # arrow
        'dYZ_': '🎯', # target
        'âš ï¸' : '⚠️'  # warning
    }
    
    # Read the file with utf-8 encoding, fallback to latin-1 if needed
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        # If UTF-8 fails, try with latin-1
        with open(file_path, 'r', encoding='latin-1') as f:
            content = f.read()
    
    original_content = content
    total_replacements = 0
    
    # Perform all replacements
    for old_seq, new_seq in replacements.items():
        count = content.count(old_seq)
        if count > 0:
            content = content.replace(old_seq, new_seq)
            total_replacements += count
    
    # If content changed, write it back with UTF-8 encoding
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
    
    return total_replacements


def main():
    """Main function to process all prompt files."""
    # Find all files matching the pattern
    pattern = "generated-prompts/prompt-*.md"
    files = glob.glob(pattern)
    
    if not files:
        print(f"No files found matching pattern: {pattern}")
        return
    
    total_files = len(files)
    total_replacements = 0
    
    print(f"Processing {total_files} files...")
    
    # Process each file
    for i, file_path in enumerate(files, 1):
        try:
            replacements_in_file = fix_emojis_in_file(file_path)
            total_replacements += replacements_in_file
            
            # Show progress
            if i % 50 == 0 or i == total_files:  # Show progress every 50 files or at the end
                print(f"Processed {i}/{total_files} files... ({replacements_in_file} replacements in current file)")
        except Exception as e:
            print(f"Error processing {file_path}: {str(e)}")
    
    print(f"\nProcessing complete!")
    print(f"Total files processed: {total_files}")
    print(f"Total replacements made: {total_replacements}")


if __name__ == "__main__":
    main()
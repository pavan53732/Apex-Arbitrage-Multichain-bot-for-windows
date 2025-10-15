#!/usr/bin/env python3
"""
Fix corrupted UTF-8 characters in all 842 prompts
Replaces corrupted emoji characters with proper UTF-8 symbols
"""

import os
import re
import shutil
from pathlib import Path

def fix_utf8_encoding():
    """Fix corrupted UTF-8 characters in all prompt files"""
    
    # Define the corrupted character mappings
    utf8_fixes = {
        # Warning siren emoji
        'ðŸš¨': '🚨',
        # Warning sign emoji  
        'âš ï¸': '⚠️',
        # Arrow symbol
        'â†'': '→',
        # Dash symbols
        'â€"': '—',
        'â€"': '–',
        # Quote symbols
        'â€™': ''',
        'â€œ': '"',
        'â€': '"',
        # Bullet and ellipsis
        'â€¢': '•',
        'â€¦': '…',
        # Dagger symbols
        'â€¡': '‡',
        'â€ ': '†'
    }
    
    prompts_dir = Path("generated-prompts")
    if not prompts_dir.exists():
        print("❌ generated-prompts directory not found!")
        return False
    
    # Get all prompt files
    prompt_files = list(prompts_dir.glob("prompt-*.md"))
    if not prompt_files:
        print("❌ No prompt files found!")
        return False
    
    print(f"🔍 Found {len(prompt_files)} prompt files to process...")
    
    # Create backup directory
    backup_dir = Path("backup_utf8_fix")
    backup_dir.mkdir(exist_ok=True)
    
    fixed_count = 0
    total_replacements = 0
    
    for prompt_file in prompt_files:
        try:
            # Read file with UTF-8 encoding
            with open(prompt_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            replacements_made = 0
            
            # Apply all UTF-8 fixes
            for corrupted, fixed in utf8_fixes.items():
                if corrupted in content:
                    count = content.count(corrupted)
                    content = content.replace(corrupted, fixed)
                    replacements_made += count
                    print(f"  ✅ {prompt_file.name}: Replaced {count} instances of '{corrupted}' → '{fixed}'")
            
            # Only write if changes were made
            if content != original_content:
                # Create backup
                backup_file = backup_dir / f"{prompt_file.name}.backup"
                shutil.copy2(prompt_file, backup_file)
                
                # Write fixed content
                with open(prompt_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                fixed_count += 1
                total_replacements += replacements_made
                print(f"  📝 {prompt_file.name}: {replacements_made} replacements made")
            else:
                print(f"  ⏭️  {prompt_file.name}: No UTF-8 issues found")
                
        except Exception as e:
            print(f"  ❌ Error processing {prompt_file.name}: {e}")
            continue
    
    print(f"\n🎉 UTF-8 Fix Complete!")
    print(f"📊 Files processed: {len(prompt_files)}")
    print(f"📊 Files fixed: {fixed_count}")
    print(f"📊 Total replacements: {total_replacements}")
    print(f"💾 Backups saved to: {backup_dir}")
    
    return True

if __name__ == "__main__":
    print("🚀 Starting UTF-8 encoding fix for all prompts...")
    success = fix_utf8_encoding()
    if success:
        print("✅ UTF-8 fix completed successfully!")
    else:
        print("❌ UTF-8 fix failed!")
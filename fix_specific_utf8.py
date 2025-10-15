#!/usr/bin/env python3
"""
Fix ONLY the specific corrupted UTF-8 characters:
ðŸš¨ → 🚨 (warning siren emoji)
âš ï¸ → ⚠️ (warning sign emoji)
"""

import os
import shutil
from pathlib import Path

def fix_specific_utf8():
    """Fix only the two specific corrupted UTF-8 characters"""
    
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
    backup_dir = Path("backup_utf8_specific")
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
            
            # Fix ONLY the two specific corrupted characters
            # Warning siren emoji: ðŸš¨ → 🚨
            if 'ðŸš¨' in content:
                count = content.count('ðŸš¨')
                content = content.replace('ðŸš¨', '🚨')
                replacements_made += count
                print(f"  ✅ {prompt_file.name}: Replaced {count} instances of 'ðŸš¨' → '🚨'")
            
            # Warning sign emoji: âš ï¸ → ⚠️
            if 'âš ï¸' in content:
                count = content.count('âš ï¸')
                content = content.replace('âš ï¸', '⚠️')
                replacements_made += count
                print(f"  ✅ {prompt_file.name}: Replaced {count} instances of 'âš ï¸' → '⚠️'")
            
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
                print(f"  ⏭️  {prompt_file.name}: No specific UTF-8 issues found")
                
        except Exception as e:
            print(f"  ❌ Error processing {prompt_file.name}: {e}")
            continue
    
    print(f"\n🎉 Specific UTF-8 Fix Complete!")
    print(f"📊 Files processed: {len(prompt_files)}")
    print(f"📊 Files fixed: {fixed_count}")
    print(f"📊 Total replacements: {total_replacements}")
    print(f"💾 Backups saved to: {backup_dir}")
    
    return True

if __name__ == "__main__":
    print("🚀 Starting specific UTF-8 encoding fix...")
    print("🎯 Fixing ONLY: ðŸš¨ → 🚨 and âš ï¸ → ⚠️")
    success = fix_specific_utf8()
    if success:
        print("✅ Specific UTF-8 fix completed successfully!")
    else:
        print("❌ Specific UTF-8 fix failed!")

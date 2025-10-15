#!/usr/bin/env python3
"""
Fix corrupted UTF-8 characters in all 842 prompts
Replaces corrupted emoji characters with proper UTF-8 symbols
"""

import os
import shutil
from pathlib import Path

def fix_utf8_encoding():
    """Fix corrupted UTF-8 characters in all prompt files"""
    
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
            
            # Fix specific corrupted characters
            # Warning siren emoji
            if 'ðŸš¨' in content:
                count = content.count('ðŸš¨')
                content = content.replace('ðŸš¨', '🚨')
                replacements_made += count
                print(f"  ✅ {prompt_file.name}: Replaced {count} instances of warning siren emoji")
            
            # Warning sign emoji
            if 'âš ï¸' in content:
                count = content.count('âš ï¸')
                content = content.replace('âš ï¸', '⚠️')
                replacements_made += count
                print(f"  ✅ {prompt_file.name}: Replaced {count} instances of warning sign emoji")
            
            # Arrow symbol
            if 'â†'' in content:
                count = content.count('â†'')
                content = content.replace('â†'', '→')
                replacements_made += count
                print(f"  ✅ {prompt_file.name}: Replaced {count} instances of arrow symbol")
            
            # Dash symbols
            if 'â€"' in content:
                count = content.count('â€"')
                content = content.replace('â€"', '—')
                replacements_made += count
                print(f"  ✅ {prompt_file.name}: Replaced {count} instances of em dash")
            
            if 'â€"' in content:
                count = content.count('â€"')
                content = content.replace('â€"', '–')
                replacements_made += count
                print(f"  ✅ {prompt_file.name}: Replaced {count} instances of en dash")
            
            # Quote symbols
            if 'â€™' in content:
                count = content.count('â€™')
                content = content.replace('â€™', ''')
                replacements_made += count
                print(f"  ✅ {prompt_file.name}: Replaced {count} instances of right single quote")
            
            if 'â€œ' in content:
                count = content.count('â€œ')
                content = content.replace('â€œ', '"')
                replacements_made += count
                print(f"  ✅ {prompt_file.name}: Replaced {count} instances of left double quote")
            
            if 'â€' in content:
                count = content.count('â€')
                content = content.replace('â€', '"')
                replacements_made += count
                print(f"  ✅ {prompt_file.name}: Replaced {count} instances of right double quote")
            
            # Bullet and ellipsis
            if 'â€¢' in content:
                count = content.count('â€¢')
                content = content.replace('â€¢', '•')
                replacements_made += count
                print(f"  ✅ {prompt_file.name}: Replaced {count} instances of bullet point")
            
            if 'â€¦' in content:
                count = content.count('â€¦')
                content = content.replace('â€¦', '…')
                replacements_made += count
                print(f"  ✅ {prompt_file.name}: Replaced {count} instances of ellipsis")
            
            # Dagger symbols
            if 'â€¡' in content:
                count = content.count('â€¡')
                content = content.replace('â€¡', '‡')
                replacements_made += count
                print(f"  ✅ {prompt_file.name}: Replaced {count} instances of double dagger")
            
            if 'â€ ' in content:
                count = content.count('â€ ')
                content = content.replace('â€ ', '†')
                replacements_made += count
                print(f"  ✅ {prompt_file.name}: Replaced {count} instances of dagger")
            
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

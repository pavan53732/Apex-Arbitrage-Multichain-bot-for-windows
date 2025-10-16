#!/usr/bin/env python3
"""
Update all 27 prompts to include proper feature file handling logic
"""

import os
import re

def update_feature_handling():
    """Update prompts to handle existing feature files properly"""
    
    prompts_dir = "generated-prompts"
    fixed_count = 0
    
    for i in range(1, 28):
        filename = f"prompt-{i:03d}.md"
        filepath = os.path.join(prompts_dir, filename)
        
        if not os.path.exists(filepath):
            print(f"❌ File not found: {filepath}")
            continue
            
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Update the WHAT YOU MUST DO section
            old_instructions = """**WHAT YOU MUST DO:**
1. ✅ Analyze ALL files in the specified folder
2. ✅ Create a complete folder tree structure  
3. ✅ Write detailed descriptions for each file (20-30 words)
4. ✅ Generate comprehensive Windows implementation details
5. ✅ Based on content analysis, decide which feature file to append to
6. ✅ APPEND this documentation to the appropriate features/*.md file
7. ✅ NO QUESTIONS - START IMMEDIATELY"""
            
            new_instructions = """**WHAT YOU MUST DO:**
1. ✅ Analyze ALL files in the specified folder
2. ✅ Create a complete folder tree structure  
3. ✅ Write detailed descriptions for each file (20-30 words)
4. ✅ Generate comprehensive Windows implementation details
5. ✅ Check if target feature file exists in features/ folder
6. ✅ If feature exists: APPEND to existing features/*.md file
7. ✅ If feature doesn't exist: CREATE new features/*.md file
8. ✅ Handle multiple features: Create separate entries for different content types
9. ✅ NO QUESTIONS - START IMMEDIATELY"""
            
            content = content.replace(old_instructions, new_instructions)
            
            # Update the WHAT YOU MUST NOT DO section
            old_restrictions = """**WHAT YOU MUST NOT DO:**
❌ Ask which folder to analyze (it's specified above)
❌ Ask for existing documentation content (you will append to it)
❌ Ask for clarification on what to do
❌ Create standalone documentation (append to existing file)"""
            
            new_restrictions = """**WHAT YOU MUST NOT DO:**
❌ Ask which folder to analyze (it's specified above)
❌ Ask for existing documentation content (check features/ folder first)
❌ Ask for clarification on what to do
❌ Create standalone documentation (use features/ folder)"""
            
            content = content.replace(old_restrictions, new_restrictions)
            
            # Add feature file handling section before REQUIRED OUTPUT FORMAT
            feature_handling_section = """
## 🔍 FEATURE FILE HANDLING PROTOCOL

**STEP 1: CHECK EXISTING FEATURES**
- Look in features/ folder for existing .md files
- Identify which feature file(s) your content belongs to
- If multiple content types: prepare separate entries

**STEP 2: DECISION MATRIX**
- **Feature exists + Single content type:** APPEND to existing file
- **Feature exists + Multiple content types:** APPEND with clear section headers
- **Feature doesn't exist:** CREATE new features/*.md file
- **Mixed content:** Create multiple feature entries with cross-references

**STEP 3: CONTENT ROUTING**
Based on your analysis, route to appropriate features/*.md:
- Smart contracts → contracts.md
- AI/ML code → ai-modules.md  
- Backend logic → backend.md
- Frontend/UI → dashboard.md
- Testing files → testing.md
- Documentation → docs.md
- Configuration → config.md
- Security → security.md
- Performance → performance.md
- Deployment → deployment.md

**STEP 4: EXECUTION**
- If appending: Add new content with clear section headers
- If creating: Use the REQUIRED OUTPUT FORMAT below
- Always maintain existing content structure and formatting
"""
            
            # Insert before REQUIRED OUTPUT FORMAT
            content = content.replace("## 📋 REQUIRED OUTPUT FORMAT", feature_handling_section + "\n## 📋 REQUIRED OUTPUT FORMAT")
            
            if content != original_content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"✅ Updated: {filename}")
                fixed_count += 1
            else:
                print(f"ℹ️  No changes needed: {filename}")
                
        except Exception as e:
            print(f"❌ Error processing {filename}: {e}")
    
    print(f"\n🎯 SUMMARY: Updated {fixed_count} out of 27 prompts")
    return fixed_count

if __name__ == "__main__":
    update_feature_handling()

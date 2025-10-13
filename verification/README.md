# Verification Scripts

## Purpose

This folder contains verification scripts to validate all 842 generated prompts before execution.

## Scripts

### verify-all-prompts.ps1

**What it checks:**
1. ✅ Correct tool names (`run_terminal_cmd`, `write`)
2. ✅ Correct base path
3. ✅ No GitHub references
4. ✅ No unreplaced placeholders (`{PROMPT_NUMBER}`, `{FOLDER_PATH}`)
5. ✅ UTF-8 encoding integrity
6. ✅ Complete template structure

**How to run:**

```powershell
cd verification
.\verify-all-prompts.ps1
```

**Expected output:**
- Total prompts validated: 842
- Valid prompts: 842
- Invalid prompts: 0
- Detailed error report if any issues found

**Exit codes:**
- 0 = All prompts valid
- 1 = Some prompts invalid

## Validation Criteria

### Tool Names
- ✅ Must use: `run_terminal_cmd`, `write`
- ❌ Must NOT use: `executeBash`, `fsWrite`, `create_or_update_file`

### Base Path
- ✅ Must be: `C:\Users\Pavan pc\Desktop\Apex Arbitrage Multichain bot for windows\Apex-Arbitrage-Multichain-bot-for-windows\Apex Arbitrage Multichain bot`

### GitHub References
- ❌ Must NOT contain: `github`, `pavan53732`, `branch: main`

### Placeholders
- ❌ Must NOT contain unreplaced: `{PROMPT_NUMBER}`, `{FOLDER_PATH}`

### Structure
- ✅ Must contain: DELEGATION FLOW, STEP 2, POWERSHELL COMMAND, 20-POINT VALIDATION MATRIX

## Usage

Run verification before executing any prompts to ensure quality.

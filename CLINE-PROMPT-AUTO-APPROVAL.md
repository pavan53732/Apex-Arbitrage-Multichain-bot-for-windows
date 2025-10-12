# CLINE TASK: Configure ALL AI Agent Extensions for Auto-Approval

## OBJECTIVE
Configure ALL AI coding assistants (Cline, Roo Code, Kilo Code, Amazon Q) in BOTH VS Code and Cursor for GLOBAL auto-approval and continuous workflow.

## EXTENSIONS TO CONFIGURE
1. **Cline** (saoudrizwan.claude-dev)
2. **Roo Code** (rooveterinaryinc.roo-cline)
3. **Kilo Code** (kilo-code.kilo-code)
4. **Amazon Q** (amazonwebservices.amazon-q-vscode)

## TASK REQUIREMENTS

### 1. Locate Global Settings Files
Modify GLOBAL user settings in:
- **VS Code**: `%APPDATA%\Code\User\settings.json`
- **Cursor**: `%APPDATA%\Cursor\User\settings.json`

### 2. Add Auto-Approval Configuration for ALL Extensions
Add these settings to BOTH files:

```json
{
  "cline.autoApprove": true,
  "cline.continueOnDelegation": true,
  "cline.autoExecuteTools": true,
  "cline.confirmBeforeExecution": false,
  "cline.requireManualApproval": false,
  "cline.alwaysAllowReadOnly": true,
  "cline.alwaysAllowWriteOnly": true,
  
  "roo-cline.autoApprove": true,
  "roo-cline.continueOnDelegation": true,
  "roo-cline.autoExecuteTools": true,
  "roo-cline.confirmBeforeExecution": false,
  "roo-cline.requireManualApproval": false,
  "roo-cline.alwaysAllowReadOnly": true,
  "roo-cline.alwaysAllowWriteOnly": true,
  
  "kilo-code.autoApprove": true,
  "kilo-code.continueOnDelegation": true,
  "kilo-code.autoExecuteTools": true,
  "kilo-code.confirmBeforeExecution": false,
  "kilo-code.requireManualApproval": false,
  "kilo-code.alwaysAllowReadOnly": true,
  "kilo-code.alwaysAllowWriteOnly": true,
  
  "amazonQ.autoApprove": true,
  "amazonQ.continueOnDelegation": true,
  "amazonQ.autoExecuteTools": true,
  "amazonQ.confirmBeforeExecution": false,
  "amazonQ.workflowMode": "continuous",
  "amazonQ.pauseOnDelegation": false,
  "amazonQ.requireManualApproval": false,
  "amazonQ.alwaysAllowReadOnly": true,
  "amazonQ.alwaysAllowWriteOnly": true
}
```

### 3. Check Extension-Specific Config Folders
Verify and modify configs in:

**VS Code:**
- `%APPDATA%\Code\User\globalStorage\saoudrizwan.claude-dev\`
- `%APPDATA%\Code\User\globalStorage\rooveterinaryinc.roo-cline\`
- `%APPDATA%\Code\User\globalStorage\kilo-code.kilo-code\`
- `%APPDATA%\Code\User\globalStorage\amazonwebservices.amazon-q-vscode\`

**Cursor:**
- `%APPDATA%\Cursor\User\globalStorage\saoudrizwan.claude-dev\`
- `%APPDATA%\Cursor\User\globalStorage\rooveterinaryinc.roo-cline\`
- `%APPDATA%\Cursor\User\globalStorage\kilo-code.kilo-code\`
- `%APPDATA%\Cursor\User\globalStorage\amazonwebservices.amazon-q-vscode\`

### 4. Create Workspace Override (Already Done)
Workspace settings already created:
- `.vscode/settings.json`
- `.cursor/settings.json`

### 5. Backup Before Modification
Create backups:
```powershell
copy "%APPDATA%\Code\User\settings.json" "%APPDATA%\Code\User\settings.json.backup"
copy "%APPDATA%\Cursor\User\settings.json" "%APPDATA%\Cursor\User\settings.json.backup"
```

### 6. EXACT COMMANDS TO EXECUTE

**Command 1: Backup VS Code settings**
```cmd
powershell.exe -Command "& { Copy-Item '$env:APPDATA\Code\User\settings.json' '$env:APPDATA\Code\User\settings.json.backup' -Force }"
```

**Command 2: Backup Cursor settings**
```cmd
powershell.exe -Command "& { Copy-Item '$env:APPDATA\Cursor\User\settings.json' '$env:APPDATA\Cursor\User\settings.json.backup' -Force }"
```

**Command 3: Update VS Code settings**
```cmd
powershell.exe -Command "& { $settings = Get-Content '$env:APPDATA\Code\User\settings.json' -Raw | ConvertFrom-Json; $settings | Add-Member -NotePropertyName 'cline.autoApprove' -NotePropertyValue $true -Force; $settings | Add-Member -NotePropertyName 'cline.continueOnDelegation' -NotePropertyValue $true -Force; $setting
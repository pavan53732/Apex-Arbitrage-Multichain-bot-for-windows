# Deployment Feature Specification

## Feature Files

- playbook.yml — Ansible orchestration playbook for AI module deployment
- inventory.ini — Server inventory and environment definitions
- secrets.yml — Encrypted deployment credentials and API keys
- all.yml — Global variables for all environments
- prod.yml — Production-specific deployment configuration
- run-all.sh — Batch script to execute full deployment pipeline

## Windows Implementation

- PowerShell wrapper converts Ansible playbooks to Windows batch scripts
- NSIS installer packages AI modules with auto-configuration
- Windows Service installer registers AI backend components
- Electron builder integrates dashboard AI features into desktop app

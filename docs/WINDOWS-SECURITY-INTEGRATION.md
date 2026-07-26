# Windows Security Integration

## Purpose
Defines how Windows-specific security features protect credentials, signing, and sandboxing.

## Ownership
- Owns DPAPI, Credential Manager, SmartScreen, AppContainer, and Defender integration.
- Does not own app-level trading risk policy or execution policy.

## Security controls
- Secrets must use DPAPI or Windows Credential Manager.
- Signed binaries are required for trusted distribution.
- Firewall rules and code-signing checks must be documented for networked components.

## Cross-references
- `SECURITY-CONTRACTS.md`
- `SECURITY.md`
- `WINDOWS-DEPLOYMENT.md`
- `PLUGIN-LIFECYCLE.md`

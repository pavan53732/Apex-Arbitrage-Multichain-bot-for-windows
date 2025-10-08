# Upload Logs

Track upload activity, errors, and sessions.

## Log Types
- **Upload Errors**: Failed uploads with error details
- **AI Session Logs**: AI model usage and results
- **Audit Logs**: User activity and file access
- **System Logs**: Upload service health

## Retention
- Error logs: 90 days
- Session logs: 30 days
- Audit logs: 1 year (compliance)
- System logs: 7 days

## Privacy
- PII is redacted or encrypted
- Access restricted to admins/operators
- GDPR compliant

## Format
- Plain text log files
- JSON structured logs for parsing
- Rotation: Daily or by size (10MB)

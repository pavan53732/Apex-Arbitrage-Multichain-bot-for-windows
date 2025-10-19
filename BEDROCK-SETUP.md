# 🔑 AWS Bedrock API Setup Guide

## Quick Setup Steps

### 1. Get AWS Credentials

1. Go to [AWS IAM Console](https://console.aws.amazon.com/iam/)
2. Create user: `bedrock-coding-assistant`
3. Attach policy: `AmazonBedrockFullAccess`
4. Create access key → Copy both keys

### 2. Configure Extensions

**Edit these files with your credentials:**

#### For Roo Extension:
```
.roo/bedrock-config.json
```

#### For Kilocode Extension:
```
.kilocode/bedrock-config.json
```

#### For Environment Variables:
```
.env.bedrock
```

**Replace:**
- `YOUR_ACCESS_KEY_ID_HERE` → Your actual Access Key ID
- `YOUR_SECRET_ACCESS_KEY_HERE` → Your actual Secret Access Key

### 3. Available Models

**Best Models (Recommended):**
- `anthropic.claude-opus-4-1-v1:0` - Most capable
- `anthropic.claude-sonnet-4-5-v1:0` - Fast + powerful
- `anthropic.claude-haiku-4-5-v1:0` - Fastest, cheapest

**Other Options:**
- `anthropic.claude-3-7-sonnet-v1:0`
- `meta.llama-4-maverick-17b-instruct-v4:0`
- `openai.gpt-oss-120b-v1:0`
- `deepseek.deepseek-r1-v1:0`

### 4. Model ID Format

```
{provider}.{model-name}-{version}:0
```

Examples:
- `anthropic.claude-opus-4-1-v1:0`
- `meta.llama-3-3-70b-instruct-v1:0`

### 5. Test Configuration

**Using AWS CLI:**
```bash
aws bedrock list-foundation-models --region us-east-1
```

**Using Node.js:**
```javascript
const { BedrockRuntimeClient, InvokeModelCommand } = require("@aws-sdk/client-bedrock-runtime");

const client = new BedrockRuntimeClient({
  region: "us-east-1",
  credentials: {
    accessKeyId: process.env.AWS_ACCESS_KEY_ID,
    secretAccessKey: process.env.AWS_SECRET_ACCESS_KEY
  }
});

const command = new InvokeModelCommand({
  modelId: "anthropic.claude-opus-4-1-v1:0",
  body: JSON.stringify({
    anthropic_version: "bedrock-2023-05-31",
    max_tokens: 1024,
    messages: [{ role: "user", content: "Hello!" }]
  })
});

const response = await client.send(command);
console.log(JSON.parse(new TextDecoder().decode(response.body)));
```

### 6. Security Best Practices

⚠️ **NEVER commit credentials to git!**

Add to `.gitignore`:
```
.env.bedrock
**/bedrock-config.json
```

### 7. Cost Monitoring

Set up billing alerts in AWS:
1. Go to AWS Billing Console
2. Create budget alert
3. Set threshold (e.g., $10/month)

**Estimated Costs:**
- Claude Opus 4.1: ~$15 per 1M output tokens
- Claude Sonnet 4.5: ~$3 per 1M output tokens
- Claude Haiku 4.5: ~$1 per 1M output tokens

### 8. Extension-Specific Setup

**For Roo Code:**
- Check extension settings for Bedrock provider option
- Point to `.roo/bedrock-config.json`

**For Kilocode:**
- Check extension settings for custom model provider
- Point to `.kilocode/bedrock-config.json`

### 9. Troubleshooting

**Error: Access Denied**
- Verify IAM permissions include `AmazonBedrockFullAccess`
- Check model access is enabled in Bedrock console

**Error: Model Not Found**
- Verify model ID format is correct
- Check model is available in your region

**Error: Invalid Credentials**
- Regenerate access keys in IAM
- Update configuration files

### 10. Region Availability

**Recommended Regions:**
- `us-east-1` (N. Virginia) - Most models
- `us-west-2` (Oregon) - Good availability
- `eu-west-1` (Ireland) - EU users

Check current region support:
https://docs.aws.amazon.com/bedrock/latest/userguide/models-regions.html

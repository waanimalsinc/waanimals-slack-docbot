# WA Animals DocBot

General purpose SlackBot for WA Animals

## Slack Setup

Create secret from the `slack_signing_secret`

```bash
aws ssm put-parameter \
  --name waanimals_slack_signing_secret \
  --type String \
  --value XXXXXXXXXXXXXXXXXXXXXXXX
```

Create a secret for the Animals in care sheet ID

```bash
aws ssm put-parameter \
  --name waanimals_gcloud_sheet_animals \
  --type String \
  --value XXXXXXXXXXXXXXXXXXXXXXXX
```

## Google Sheets API Setup

Follow the guide [here](https://gspread.readthedocs.io/en/latest/oauth2.html#using-signed-credentials) and put the credentials file in `docbot/utils/gauth.json`

### Testing

```bash
serverless offline start --stage=test
```

```bash
curl -X POST \
  http://localhost:3000 \
  -H 'Content-Type: application/json' \
  -d 'token=XXXXXXXXXXXXXXXXXXXXXXXXXX&team_id=TL00AB204&team_domain=waanimals&channel_id=GL8LA7DUP&channel_name=privategroup&user_id=UL0UV78CU&user_name=nathan&command=%2Fmicrochip&text=Testing&response_url=https%3A%2F%2Fhooks.slack.com%2Fcommands%2XXXXXXXXXXXXXXXXXXXXXXXXXX%2XXXXXXXXXXXXXXXXXXXXXXXXXX&trigger_id=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
```

### Deploy

```bash
serverless deploy --stage=dev
```

### Assume Role

```bash
response=$(aws sts assume-role --role-arn arn:aws:iam::XXXXXXXXXXXX:role/SandboxDev --role-session-name "Serverless")

# Set Variables
export AWS_ACCESS_KEY_ID=$(echo $response | jq -r '.Credentials.AccessKeyId')
export AWS_SECRET_ACCESS_KEY=$(echo $response | jq -r '.Credentials.SecretAccessKey')
export AWS_SESSION_TOKEN=$(echo ${response} | jq -r '.Credentials.SessionToken')
```

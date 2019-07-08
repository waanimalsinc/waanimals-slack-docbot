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

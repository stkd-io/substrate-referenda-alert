# substrate-referenda-alert


You will need to create a Values.yaml and configure as needed. The Slack intergration will require an API key and invite the app to the channel. Slack Doc's https://api.slack.com/authentication/basics

Example Values.yaml
```
schedule: "0 12 * * *"

timezone: "UTC"
wallet_address: "Fq4YmiAq76DntjMKKjMiL98MYszoApUa9idSErvyzfdGoqG"
WSS_URL: "wss://kusama-rpc.polkadot.io/"
SLACK_API: "API_KEY_FROM_SLACK_FOR_APPLICATION"
SLACK_CHANNEL_NAME: "NEW-REF"
```


Chart installation:
```
helm repo add substrate-referenda-alert  https://stkd-io.github.io/substrate-referenda-alert/
helm repo update
helm install ksm-ref-alert substrate-referenda-alert/substrate-referenda-alert -n ksm-ref-alert --create-namespace -f Values.yaml
```


Tips: 
-  KSM: Fq4YmiAq76DntjMKKjMiL98MYszoApUa9idSErvyzfdGoqG 
-  DOT: 12pdN2XsNmG2yPAv5QCkq7YYUg1MM3prvGMgusH7S6FnDHAx

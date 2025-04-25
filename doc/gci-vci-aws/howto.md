# How-to guides

## How to create an API key for the GCI/VCI

### Before you begin...

If you're adding a key for curators with a specific affiliation, write down the
affiliation ID. You'll need it later.

### Create the API key

- In the AWS web console, go to the API Gateway service.
- In the sidebar, click **API keys**.
- Look at the list of API keys and make sure the API key you need to create
  doesn't already exist.
- If the API key doesn't already exist, click **Create API key**.
  - If you're adding an API key for curators with a specific affiliation with
    the "curator" role, name the key `curator-<affiliation ID>`.
  - Otherwise, give the key a descriptive name.
  - Write what the key is for in the description.
- Write down the API key for later.

### Get the API URL

- You'll need to provide the person who requested the API key with a URL.
- In the sidebar, click **APIs**.
- Select the `<stage-name>-gci-vci-api` API.
- In the sidebar section for `<stage-name>-gci-vci-api`, click **Stages**.
- Write down the **Invoke URL** for later.

### Add the API key to a usage plan

- In the sidebar, click **Usage plans**.
- Select `<stage-name>-usage-plan`.
- Go to the **Associated API keys** tab.
- Add your new API key to this usage plan.

### Add the API key to DynamoDB

- Go to the DynamoDB table named `GCI-VCI-API-<stage-name>`.
- Click **Explore table items**.
- Click **Create item**.
- Add the new API key under the attribute `api_key_value`.
- Add other attributes as necessary.
- If you're adding an API key for curators with a specific affiliation, you'll
  want the JSON view of the item to look like the JSON below.

```
{
 "api_key_value": "<key>",
 "affiliations": [
  "<affiliation ID>"
 ],
 "roles": [
  "curator"
 ]
}
```

### Provide the user with the API documentation and an example script

- The API documentation can be found [here](https://vci-gci-docs.clinicalgenome.org/vci-gci-docs/gci-help/gci-api).
- Fill out the following example script.
- Send the link and the script to the user.

```
#!/usr/bin/env bash

URL="<fill this out>"
KEY="<fill this out>"
AFF="<fill this out>"
DATE_START="2024-01-01"
DATE_END="<fill this out>"

# Summarize gene-disease records for the given affiliation and date range.
curl \
    -H "x-api-key:$KEY" \
    -G "$URL/snapshots" \
    -d target=gci \
    -d name=summary \
    -d status=published \
    -d start="$DATE_START" \
    -d end="$DATE_END" \
    -d affiliation="$AFF" \
    -d format=csv \
    >"$AFF".csv
```

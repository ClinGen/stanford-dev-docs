### Restore DynamoDB Table

1. (Point-in-time only) Create a new (temporary) content table via Point-in-time recovery
    1. Viewing the table to restore (content table) within the DynamoDB service console, find the **Point-in-time recovery (PITR)** area of the **Backups** tab/section and initiate a restore<br><img alt="Step 1 screenshot" src="images/dynamodb-restore/dynamodb-tables-backups-pitr.png" width="60%"><br>URL: *us-west-2.console.aws.amazon.com/dynamodbv2/home?region=us-west-2#table?initialTagKey=&name=[content table name]&tab=backups*
    2. Use the following restore options:
        - Table name: [content table name]-pitr (e.g. GeneVariantCuration-bwtest-pitr)
        - Point-in-time recovery: specify the date and time to which the content table needs to be reverted/restored
        - Secondary indexes: Restore the entire table (global secondary indexes are needed)
        - Region: Same Region (as content table)
        - Encryption: Owned by Amazon DynamoDB (should match setting of content table)

<br>

2. (Point-in-time only) Create a backup of the new (temporary) content table
    1. Viewing the new (temporary) content table within the DynamoDB service console, find the **Backups** area of the **Backups** tab/section and select **Create on-demand backup** under **Create backup**<br><img alt="Step 2 screenshot" src="images/dynamodb-restore/dynamodb-tables-backups-backups.png" width="60%"><br>URL: *us-west-2.console.aws.amazon.com/dynamodbv2/home?region=us-west-2#table?initialTagKey=&name=[content table name]&tab=backups*
    2. Use the following backup options:
        - Backup settings: Customize settings
        - Backup management: Backup with DynamoDB
        - Backup name: [content table name]-pitr-backup

<br>

3. Make sure the necessary backup table exists
    1. Find the backup table on the **Backups** page of the DynamoDB service console and confirm its status is **Available**<br><img alt="Step 3 screenshot" src="images/dynamodb-restore/dynamodb-backups-backups.png" width="80%"><br>URL: *us-west-2.console.aws.amazon.com/dynamodbv2/home?region=us-west-2#list-backups*

<br>

4. Prevent users from making any changes to the data/table
    - Add a maintenance mode to the app?
    - Disable user access via Cognito?
    - Use access control in Amplify?

<br>

5. Disable trigger that updates the history table when the content table is modified (to avoid generating errors when the content table is deleted)
    1. Viewing the content table within the DynamoDB service console, find the **Trigger** area of the **Exports and streams** tab/section and click on the "gci-vci-history-trigger" function name (which should open the Lambda function)<br><img alt="Step 5.1 screenshot" src="images/dynamodb-restore/dynamodb-tables-streams-trigger.png" width="60%"><br>URL: *us-west-2.console.aws.amazon.com/dynamodbv2/home?region=us-west-2#table?initialTagKey=&name=[content table name]&tab=streams*
    2. Viewing the "gci-vci-history-trigger" function within the Lambda service console, go to the **Configuration** tab/section and click on **Triggers** from the navigation panel<br><img alt="Step 5.2 screenshot" src="images/dynamodb-restore/lambda-configuration-triggers.png" width="80%"><br>URL: *us-west-2.console.aws.amazon.com/lambda/home?region=us-west-2#/functions/[trigger function name]?tab=configure*
    3. Click the checkbox of the enabled trigger (title should be DynamoDB: [content table name] (Enabled)) and select the **Disable** button

<br>

6. Delete the content table
    1. Viewing the content table within the DynamoDB service console, go to **Actions** and choose **Delete table**<br><img alt="Step 6 screenshot" src="images/dynamodb-restore/dynamodb-tables-actions.png" width="60%"><br>URL: *us-west-2.console.aws.amazon.com/dynamodbv2/home?region=us-west-2#table?initialTagKey=&name=[content table name]&tab=overview*
    2. Use the following delete options:
        - Select: Delete all CloudWatch alarms for this table.

<br>

7. Restore the content table from backup (to its original name)
    1. Select the backup table on the **Backups** page of the DynamoDB service console and choose **Restore**<br><img alt="Step 7 screenshot" src="images/dynamodb-restore/dynamodb-backups-backups.png" width="80%"><br>URL: *us-west-2.console.aws.amazon.com/dynamodbv2/home?region=us-west-2#list-backups*
    2. Use the following restore options:
        - Table name: [content table name]
        - Secondary indexes: Restore the entire table (global secondary indexes are needed)
        - Region: Same Region
        - Encryption: Owned by Amazon DynamoDB

<br>

8. Enable Point-in-time recovery (PITR) on the restored content table
    1. Viewing the restored content table within the DynamoDB service console, find the **Point-in-time recovery (PITR)** area of the **Backups** tab/section and choose **Edit**<br><img alt="Step 8 screenshot" src="images/dynamodb-restore/dynamodb-tables-backups-pitr-edit.png" width="60%"><br>URL: *us-west-2.console.aws.amazon.com/dynamodbv2/home?region=us-west-2#table?initialTagKey=&name=[content table name]&tab=backups*
    2. Use the following enable option:
        - Select: Enable point-in-time-recovery

<br>

9. Restore trigger that updates the history table when the content table is modified (in order to maintain an accurate record of content changes)
    1. Viewing the restored content table within the DynamoDB service console, find the **DynamoDB stream details** area of the **Exports and streams** tab/section and choose **Enable**<br><img alt="Step 9.1 screenshot" src="images/dynamodb-restore/dynamodb-tables-streams-stream.png" width="60%"><br>URL: *us-west-2.console.aws.amazon.com/dynamodbv2/home?region=us-west-2#table?initialTagKey=&name=[content table name]&tab=streams*
    2. Use the following enable option:
        - Select: New and old images
    3. Record/Copy the new stream ARN under **Latest stream ARN**<br><img alt="Step 9.3 screenshot" src="images/dynamodb-restore/dynamodb-tables-streams-stream-arn.png" width="60%"><br>URL: *us-west-2.console.aws.amazon.com/dynamodbv2/home?region=us-west-2#table?initialTagKey=&name=[content table name]&tab=streams*
    4. Returning to the view of the "gci-vci-history-trigger" function within the Lambda service console, go to the **Configuration** tab/section and click on **Permissions** from the navigation panel<br><img alt="Step 9.4 screenshot" src="images/dynamodb-restore/lambda-configuration-permissions.png" width="80%"><br>URL: *us-west-2.console.aws.amazon.com/lambda/home?region=us-west-2#/functions/[trigger function name]?tab=configure*
    5. Within the **Execution role** area, click on the "ClinGenTriggerRole" role name (which should open the IAM role)
    6. Viewing the "ClinGenTriggerRole" role within the IAM service console, find the **Permissions policies** area of the **Permissions** tab/section and click on the "clingenhistory" policy name<br><img alt="Step 9.6 screenshot" src="images/dynamodb-restore/iam-permissions-policies.png" width="80%"><br>URL: *console.aws.amazon.com/iamv2/home#/roles/details/[execution role name]?section=permissions*
    7. Click on the **JSON** tab and update the one reference to the content table's stream ARN<br><img alt="Step 9.7 screenshot" src="images/dynamodb-restore/iam-permissions-policy-json.png" width="80%"><br>URL: *console.aws.amazon.com/iam/home#/roles/[execution role name]$jsonEditor?policyName=clingenhistory&step=edit*
    8. Returning to the view of the restored content table within the DynamoDB service console, choose **Create trigger**<br><img alt="Step 9.8 screenshot" src="images/dynamodb-restore/dynamodb-tables-streams-trigger-create.png" width="60%"><br>URL: *us-west-2.console.aws.amazon.com/dynamodbv2/home?region=us-west-2#table?initialTagKey=&name=[content table name]&tab=streams*
    9. Use the following create options:
        - Lambda function: "gci-vci-history-trigger" function (specific to the deployment of interest, e.g. gci-vci-serverless-bwtest-gci-vci-history-trigger)
        - Batch size: 10
        - Select: Enable trigger

<br>

10. Restoration of other functionality/services tied to the content table (such as CloudWatch alarms)?

<br>

11. Confirm restored content table is accessible from deployed application
    - Within the app, visit multiple curations, gene and variant, to confirm the presence of evidence, evaluations, saved classifications/interpretations, etc.
    - Specific to the VCI, confirm that curation audit trails have data
    - Check that VP search results include VCI interpretation data?
    - **If not testing the production app/data**, add gene and variant curations and confirm all data appears as expected

<br>

12. Restore user access to the data/application

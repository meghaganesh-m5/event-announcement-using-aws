import json
import boto3

def lambda_handler(event, context):
    sns = boto3.client('sns', region_name='ap-south-1')

    # SNS Topic ARN (REPLACE WITH YOUR OWN)
    topic_arn = "PASTE_YOUR_SNS_TOPIC_ARN_HERE"

    # Read message from API Gateway
    body = json.loads(event['body'])
    message = body['message']

    # Publish message to SNS
    sns.publish(
        TopicArn=topic_arn,
        Message=message,
        Subject="Event Announcement"
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Announcement sent successfully!')
    }

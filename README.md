# event-announcement-using-aws
Creating a an AWS Event announcement system on aws  to learn about various aws services

This project implements a serverless event announcement system using AWS services.
It allows events or announcements to be sent through an API endpoint, which triggers a Lambda function to publish notifications via Amazon SNS, delivering real-time email alerts to subscribers.


---

🏗️ Architecture

Client / API Call
        ↓
API Gateway (POST request)
        ↓
AWS Lambda (Python)
        ↓
Amazon SNS
        ↓
Email Notification


---

🧰 Technologies Used

AWS Lambda (Python)

Amazon SNS (Email Notifications)

Amazon API Gateway

IAM (Roles & Permissions)

AWS CloudShell / Console



---

⚙️ How It Works

1. A POST request is sent to an API Gateway endpoint.


2. API Gateway triggers an AWS Lambda function.


3. The Lambda function processes the message.


4. The message is published to an SNS topic.


5. SNS sends the announcement as an email to subscribed users.





🧪 Sample API Request

POST request body (JSON):

{
  "message": "This is a test announcement"
}


---

🧠 Lambda Function Logic

Parses the incoming event message.

Uses AWS SDK (boto3) to publish the message to an SNS topic.

Returns a success response after publishing.



---

🔐 Security & IAM

Lambda function uses an IAM role with:

sns:Publish permission

Basic CloudWatch logging permissions


Follows least-privilege access principle.



---

✅ Verification

Email notifications successfully received after triggering the API.

Lambda execution confirmed via AWS console logs.

End-to-end flow tested and validated.



---

📸 Screenshots

Screenshots included in the screenshots/ folder:

SNS Topic & Subscription

Lambda Function Code

API Gateway Route

Email Notification Received



---

🧹 Cleanup

All AWS resources were deleted after testing to avoid unnecessary charges.



📌 Key Learnings

Serverless architecture using AWS

Event-driven communication with SNS

API-based triggering of cloud functions

Secure IAM role configuration




🚀 Future Enhancements

Add SMS notifications

Store announcements in DynamoDB

Add authentication to API Gateway



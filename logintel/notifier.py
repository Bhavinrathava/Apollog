import boto3

class SNSNotifier:
    def __init__(self, topic_arn):
        self.client = boto3.client('sns')
        self.topic_arn = topic_arn

    def send_alert(self, subject, message):
        self.client.publish(
            TopicArn=self.topic_arn,
            Subject=subject,
            Message=message
        )
import json
import random
import time

def generate_fake_apigateway_logs(num_entries):
    fake_logs = []
    for _ in range(num_entries):
        log_entry = {
            "requestId": f"request-{random.randint(1000, 9999)}",
            "ip": f"192.168.{random.randint(0, 255)}.{random.randint(0, 255)}",
            "requestTime": time.strftime("%d/%b/%Y:%H:%M:%S %z", time.gmtime()),
            "httpMethod": random.choice(["GET", "POST", "PUT", "DELETE"]),
            "resourcePath": f"/api/resource/{random.randint(1, 10)}",
            "status": random.choices([200, 400, 404, 500], weights=[90, 3, 3, 4], k=1)[0],
            "responseLength": random.randint(100, 5000)
        }
        fake_logs.append(log_entry)
    return fake_logs

def generate_fake_stepfunctions_logs(num_entries):
    fake_logs = []
    for _ in range(num_entries):
        log_entry = {
            "executionArn": f"arn:aws:states:us-east-1:123456789012:execution:stateMachine-{random.randint(1000, 9999)}",
            "stateMachineArn": f"arn:aws:states:us-east-1:123456789012:stateMachine:stateMachine-{random.randint(1000, 9999)}",
            "name": f"execution-{random.randint(1000, 9999)}",
            "status": random.choices(["SUCCEEDED", "FAILED", "RUNNING", "TIMED_OUT"], weights=[90, 3, 5, 2], k=1)[0],
            "startDate": time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime()) + f".{int(time.time() % 1 * 1000):03d}Z",
            "stopDate": time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime()) + f".{int(time.time() % 1 * 1000):03d}Z"
        }
        fake_logs.append(log_entry)
    return fake_logs

def generate_fake_fargate_logs(num_entries):
    fake_logs = []
    for _ in range(num_entries):
        log_entry = {
            "taskArn": f"arn:aws:ecs:us-east-1:123456789012:task/{random.randint(1000, 9999)}",
            "clusterArn": f"arn:aws:ecs:us-east-1:123456789012:cluster/cluster-{random.randint(1000, 9999)}",
            "taskDefinitionArn": f"arn:aws:ecs:us-east-1:123456789012:task-definition/taskdef-{random.randint(1000, 9999)}",
            "lastStatus": random.choices(["RUNNING", "STOPPED", "PENDING"], weights=[90, 5, 5], k=1)[0],
            "desiredStatus": random.choice(["RUNNING", "STOPPED"]),
            "createdAt": time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime()) + f".{int(time.time() % 1 * 1000):03d}Z",
            "startedAt": time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime()) + f".{int(time.time() % 1 * 1000):03d}Z"
        }
        fake_logs.append(log_entry)
    return fake_logs

def generate_fake_lambda_logs(num_entries):
    fake_logs = []
    for _ in range(num_entries):
        log_entry = {
            "requestId": f"request-{random.randint(1000, 9999)}",
            "functionName": f"lambda-function-{random.randint(1000, 9999)}",
            "memorySize": random.choice([128, 256, 512, 1024, 2048]),
            "duration": random.uniform(0.1, 3.0),
            "billedDuration": random.randint(100, 3000),
            "logStreamName": f"log-stream-{random.randint(1000, 9999)}",
            "status": random.choices(["Success", "Error"], weights=[90, 10], k=1)[0]
        }
        fake_logs.append(log_entry)
    return fake_logs

import boto3

def export_logs_to_cloudwatch(logs, namespace, region_name='us-west-2'):
    client = boto3.client('logs', region_name=region_name)
    log_group_name = f"/aws/{namespace}"
    
    # Create log group if it doesn't exist
    try:
        client.create_log_group(logGroupName=log_group_name)
    except client.exceptions.ResourceAlreadyExistsException:
        pass

    # Create log stream
    log_stream_name = f"{namespace}-stream"
    try:
        client.create_log_stream(logGroupName=log_group_name, logStreamName=log_stream_name)
    except client.exceptions.ResourceAlreadyExistsException:
        pass

    # Put log events
    log_events = []
    for i, log in enumerate(logs):
        log_events.append({
            'timestamp': int(time.time() * 1000),
            'message': json.dumps(log)
        })

    client.put_log_events(
        logGroupName=log_group_name,
        logStreamName=log_stream_name,
        logEvents=log_events
    )
if __name__ == "__main__":
    # Generate 10 fake API Gateway log entries
    fake_apigateway_logs = generate_fake_apigateway_logs(10)
    print("API Gateway Logs:")
    print(json.dumps(fake_apigateway_logs, indent=4))

    # Generate 10 fake Step Functions log entries
    fake_stepfunctions_logs = generate_fake_stepfunctions_logs(10)
    print("\nStep Functions Logs:")
    print(json.dumps(fake_stepfunctions_logs, indent=4))

    # Generate 10 fake Fargate log entries
    fake_fargate_logs = generate_fake_fargate_logs(10)
    print("\nFargate Logs:")
    print(json.dumps(fake_fargate_logs, indent=4))

    # Generate 10 fake Lambda log entries
    fake_lambda_logs = generate_fake_lambda_logs(10)
    print("\nLambda Logs:")
    print(json.dumps(fake_lambda_logs, indent=4))

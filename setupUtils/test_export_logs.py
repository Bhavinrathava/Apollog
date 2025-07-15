from setupAPILogs import (
    generate_fake_apigateway_logs,
    generate_fake_stepfunctions_logs,
    generate_fake_fargate_logs,
    generate_fake_lambda_logs,
    export_logs_to_cloudwatch
)

def test_export_logs():
    # Generate fake logs
    howMany = 1000
    apigateway_logs = generate_fake_apigateway_logs(howMany)
    stepfunctions_logs = generate_fake_stepfunctions_logs(howMany)
    fargate_logs = generate_fake_fargate_logs(howMany)
    lambda_logs = generate_fake_lambda_logs(howMany)

    # Export logs to CloudWatch
    export_logs_to_cloudwatch(apigateway_logs, "APIGateway")
    export_logs_to_cloudwatch(stepfunctions_logs, "StepFunctions")
    export_logs_to_cloudwatch(fargate_logs, "Fargate")
    export_logs_to_cloudwatch(lambda_logs, "Lambda")

if __name__ == "__main__":
    test_export_logs()

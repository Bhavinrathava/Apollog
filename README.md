# Apollog (v0.1.1)

![Apollog](robot.png)

## What is Apollog?

Apollog is an open source solution for monitoring your existing services on AWS. There are 2 key offerings of this project:

- **Log Aggregation over services**: Collect and centralize logs from multiple AWS services
- **Error Event summarization powered by LLMs**: Automatically analyze and summarize error events

With this project, the aim is to allow users to simply deploy a side car stack on AWS that can keep track of your services and provide detailed analysis of any error events.

## Installation

### Option 1: Install from PyPI (Recommended)

```bash
pip install apollog
```

### Option 2: Install from Source

```bash
git clone https://github.com/Bhavinrathava/Apollog.git
cd Apollog
pip install -e .
```

## Quick Start

### 1. Initialize a New Project

```bash
# Create a new project in the current directory
apollog init

# Or specify a different directory
apollog init --destination my-apollog-project
```

### 2. Configure Your AWS Credentials

Ensure your AWS credentials are properly configured. You can do this by:

- Using the AWS CLI: `aws configure`
- Setting environment variables: `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`
- Using a credentials file in `~/.aws/credentials`

### 3. Edit the Configuration File

Edit the `examples/config.yaml` file to specify the AWS services you want to monitor:

```yaml
# Services to monitor
services:
  - serviceName: "MyAPIGateway"
    namespace: "/aws/APIGateway"
    region: "us-west-2"
  - serviceName: "MyLambda"
    namespace: "/aws/Lambda"
    region: "us-west-2"

# Architecture configuration
architecture: 
  logTableName: "Apollog-TimeBlock-Logs"
  summaryTableName: "Apollog-event-summary"
  tableRegion: "us-west-2"

# Stack name for CloudFormation
stack_name: "Apollog-Monitoring-Stack"
```

### 4. Deploy the Stack

```bash
apollog deploy --config examples/config.yaml
```

This will:
1. Create Lambda deployment packages
2. Upload them to an S3 bucket
3. Deploy a CloudFormation stack with all necessary resources
4. Set up the frontend for accessing the monitoring dashboard

## Architecture

Apollog deploys the following AWS resources:

- **API Gateway**: Serves the frontend interface
- **Lambda Functions**:
  - Log Ingestion Lambda: Collects logs from specified services
  - Summary Lambda: Analyzes logs and generates summaries
  - Frontend Lambda: Serves the web interface
- **DynamoDB Tables**:
  - Logs Table: Stores collected logs
  - Summary Table: Stores error event summaries
- **CloudWatch Events**: Triggers the log ingestion process on a schedule

## Advanced Usage

![alt text](image.png)
### Custom Project Directory

If you've organized your project files in a different directory structure, you can specify the project directory when deploying:

```bash
apollog deploy --config examples/config.yaml --project-dir /path/to/project
```

### Updating an Existing Stack

When you run the deploy command and a stack with the same name already exists, you'll be prompted to update it:

```
Stack Apollog-Monitoring-Stack already exists. Do you want to update it? (Y/N):
```

Enter `Y` to update the existing stack with your new configuration.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

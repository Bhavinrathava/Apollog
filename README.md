# Smart Log Ingestion Service

This is a smart log ingestion service designed to poll logs, process them, and send event reports to users in case of errors. The service is built to work with AWS CloudWatch and SNS for log management and notifications.

## Features

- **Log Polling**: Continuously polls AWS CloudWatch for logs containing error patterns.
- **Log Processing**: Summarizes logs to provide insights and recommendations.
- **Notifications**: Sends alerts to users via AWS SNS when errors are detected.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Bhavinrathava/Apollog.git
   cd Apollog
   ```

2. **Install Dependencies**:
   Ensure you have Python and pip installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **AWS Configuration**:
   Make sure your AWS credentials are configured. You can set them up using the AWS CLI:
   ```bash
   aws configure
   ```

## Usage

1. **Configuration**:
   Update the `examples/config.yaml` file with your log group names and SNS topic ARN.

2. **Run the Service**:
   Execute the main runner script to start the service:
   ```bash
   python controlPlane/runner.py
   ```

## Configuration

- **Log Groups**: Specify the AWS CloudWatch log groups you want to monitor in the configuration file.
- **SNS Topic ARN**: Provide the ARN of the SNS topic where notifications will be sent.

## Contribution

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.

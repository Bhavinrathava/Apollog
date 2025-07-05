import time
from controlPlane.config import ConfigLoader
from controlPlane.logIngestionEngine.poller import CloudWatchPoller
from controlPlane.logProcessingEngine.summarizer import LogSummarizer
from controlPlane.notificationEngine.notifier import SNSNotifier

def main():
    config = ConfigLoader('config.yaml')
    poller = CloudWatchPoller(config.get_log_groups(), config.get_poll_interval())
    summarizer = LogSummarizer()
    notifier = SNSNotifier(config.get_sns_topic_arn())

    while True:
        logs = poller.poll()
        if logs:
            grouped = {}
            for log_group, msg in logs:
                grouped.setdefault(log_group, []).append(msg)
            for lg, msgs in grouped.items():
                summary = summarizer.summarize(lg, msgs)
                notifier.send_alert(subject=f"[LogIntel] Alert from {lg}", message=summary)
        time.sleep(config.get_poll_interval())


if __name__ == '__main__':
    main()



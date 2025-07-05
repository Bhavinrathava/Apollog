import boto3
import time

class CloudWatchPoller:
    def __init__(self, log_groups, interval):
        self.client = boto3.client('logs')
        self.log_groups = log_groups
        self.interval = interval
        self.last_timestamps = {lg: 0 for lg in log_groups}

    def poll(self):
        all_logs = []
        for log_group in self.log_groups:
            start_time = self.last_timestamps[log_group] + 1
            response = self.client.filter_log_events(
                logGroupName=log_group,
                startTime=start_time,
                filterPattern='?ERROR ?Error ?Exception'
            )
            events = response.get('events', [])
            if events:
                latest = max(e['timestamp'] for e in events)
                self.last_timestamps[log_group] = latest
                all_logs.extend([(log_group, e['message']) for e in events])
        return all_logs

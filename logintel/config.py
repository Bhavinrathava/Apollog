import yaml

class ConfigLoader:
    def __init__(self, path):
        with open(path, 'r') as f:
            self.config = yaml.safe_load(f)

    def get_log_groups(self):
        return self.config.get("log_groups", [])

    def get_poll_interval(self):
        return self.config.get("poll_interval", 60)

    def get_sns_topic_arn(self):
        return self.config.get("sns_topic_arn")
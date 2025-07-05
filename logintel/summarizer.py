class LogSummarizer:
    def __init__(self, model=None):
        self.model = model or self.mock_model

    def mock_model(self, logs):
        summary = "\n".join(logs[:5])  # fake summarization
        return f"SUMMARY:\n{summary}\nROOT CAUSE: Unknown\nRECOMMENDATION: Investigate the service."

    def summarize(self, log_group, logs):
        combined = "\n".join(logs)
        return self.model(combined)


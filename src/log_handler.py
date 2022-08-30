import logging

class PremineLogHandler(logging.Handler):

    _logs = {}

    def _add_to_logs(self, threadName: str, message: str):
        if threadName in PremineLogHandler._logs:
            PremineLogHandler._logs[threadName].append(message)
        else:
            PremineLogHandler._logs[threadName] = [message]

    def emit(self, record: logging.LogRecord):
        self.format(record)
        self._add_to_logs(record.threadName, record.message)
        return record

    @staticmethod
    def get_logs_for_thread(threadName: str) -> list[str]:
        if threadName in PremineLogHandler._logs:
            return PremineLogHandler._logs[threadName]
        return []

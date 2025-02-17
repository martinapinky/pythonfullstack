# logging_handlers.py
import csv
import logging

class CSVLoggingHandler(logging.Handler):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename

        # Ensure the file exists and is ready for appending
        with open(self.filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Time', 'Level', 'Message'])  # Write header only once

    def emit(self, record):
        try:
            log_entry = self.format(record)
            # Split log entry into time, level, and message for CSV
            log_parts = log_entry.split(',')
            with open(self.filename, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(log_parts)
        except Exception:
            self.handleError(record)
import csv
import os
from datetime import datetime

# File name
CSV_FILE = "emotion_log.csv"

# Create CSV file if not exists
if not os.path.exists(CSV_FILE):

    with open(CSV_FILE, mode='w', newline='') as file:

        writer = csv.writer(file)

        writer.writerow([
            "timestamp",
            "emotion"
        ])


def log_emotion(emotion):

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    with open(CSV_FILE, mode='a', newline='') as file:

        writer = csv.writer(file)

        writer.writerow([
            timestamp,
            emotion
        ])
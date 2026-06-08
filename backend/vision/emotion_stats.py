import csv
from collections import Counter

CSV_FILE = "emotion_log.csv"


def generate_statistics():

    emotions = []

    try:

        with open(CSV_FILE, mode='r') as file:

            reader = csv.DictReader(file)

            for row in reader:

                emotions.append(
                    row['emotion']
                )

    except FileNotFoundError:

        print("No emotion log found.")
        return

    # No emotions logged
    if len(emotions) == 0:

        print("No emotion data available.")
        return

    # Count emotions
    emotion_counts = Counter(emotions)

    total = len(emotions)

    print("\n")
    print("=" * 40)
    print("SESSION EMOTION SUMMARY")
    print("=" * 40)

    # Percentages
    for emotion, count in emotion_counts.items():

        percentage = (
            count / total
        ) * 100

        print(
            f"{emotion:<10}: "
            f"{percentage:.1f}%"
        )

    # Dominant emotion
    dominant = emotion_counts.most_common(1)[0][0]

    print("\nDominant Emotion:",
          dominant)

    print("=" * 40)
from collections import Counter

# =========================
# EMOTION HISTORY
# =========================

emotion_history = []

MAX_HISTORY = 100

# =========================
# ADD EMOTION
# =========================

def update_emotion_history(
    emotion
):

    emotion_history.append(
        emotion
    )

    if len(emotion_history) > MAX_HISTORY:

        emotion_history.pop(0)

# =========================
# DOMINANT EMOTION
# =========================

def get_dominant_emotion():

    if not emotion_history:

        return "neutral"

    counter = Counter(
        emotion_history
    )

    dominant = counter.most_common(1)[0][0]

    return dominant

# =========================
# EMOTION PERCENTAGES
# =========================

def get_emotion_percentages():

    if not emotion_history:

        return {}

    counter = Counter(
        emotion_history
    )

    total = len(
        emotion_history
    )

    percentages = {}

    for emotion, count in counter.items():

        percentages[emotion] = round(
            (count / total) * 100,
            1
        )

    return percentages

# =========================
# STABILITY SCORE
# =========================

def get_stability_score():

    if len(emotion_history) < 2:

        return 100

    changes = 0

    for i in range(
        1,
        len(emotion_history)
    ):

        if (
            emotion_history[i]
            != emotion_history[i - 1]
        ):

            changes += 1

    stability = 100 - (
        (changes / len(emotion_history))
        * 100
    )

    return round(stability, 1)
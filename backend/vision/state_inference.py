# =========================
# SMART STATE INFERENCE
# =========================

def infer_state(
    dominant_emotion,
    stability_score
):

    # =========================
    # HIGH STABILITY
    # =========================

    if stability_score >= 85:

        if dominant_emotion == "happy":

            return "Highly Engaged"

        elif dominant_emotion == "neutral":

            return "Focused"

        elif dominant_emotion == "sad":

            return "Fatigued"

        elif dominant_emotion == "angry":

            return "Stressed"

        else:

            return "Emotionally Stable"

    # =========================
    # MEDIUM STABILITY
    # =========================

    elif stability_score >= 60:

        if dominant_emotion == "happy":

            return "Attentive"

        elif dominant_emotion == "neutral":

            return "Balanced"

        else:

            return "Emotionally Reactive"

    # =========================
    # LOW STABILITY
    # =========================

    else:

        return "Highly Reactive"
import cv2

print("NEW UI RENDERER LOADED")


def get_color(emotion):

    colors = {
        "happy": (0, 255, 0),        # Green
        "sad": (255, 0, 0),          # Blue
        "angry": (0, 0, 255),        # Red
        "surprise": (0, 255, 255),   # Yellow
        "fear": (128, 0, 128),       # Purple
        "neutral": (255, 255, 255),  # White
        "disgust": (0, 128, 0)       # Dark Green
    }

    return colors.get(emotion, (255, 255, 255))


def draw_overlay(frame, emotion_data):

    x = emotion_data['region']['x']
    y = emotion_data['region']['y']
    w = emotion_data['region']['w']
    h = emotion_data['region']['h']

    emotion = emotion_data['emotion']
    confidence = emotion_data['confidence']

    color = get_color(emotion)

    # Face Box
    cv2.rectangle(
        frame,
        (x, y),
        (x + w, y + h),
        color,
        3
    )

    # Emotion Text
    text = f"{emotion} ({confidence:.1f}%)"

    cv2.putText(
        frame,
        text,
        (x, y - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.9,
        color,
        2
    )

    return frame
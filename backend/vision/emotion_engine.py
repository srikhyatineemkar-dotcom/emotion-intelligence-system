from deepface import DeepFace

def detect_emotion(frame):
    result = DeepFace.analyze(
        frame,
        actions=['emotion'],
        enforce_detection=False
    )

    data = result[0]

    emotion = data['dominant_emotion']
    confidence = data['emotion'][emotion]

    region = data['region']
    print(emotion)

    return {
        "emotion": emotion,
        "confidence": confidence,
        "region": region
    }
import cv2
import time
import threading
from collections import Counter

from vision.emotion_engine import detect_emotion
from vision.ui_renderer import draw_overlay

from vision.voice_emotion import (
    detect_voice_emotion
)

# =========================
# CAMERA
# =========================

cap = cv2.VideoCapture(0)

# =========================
# FACE SYSTEM
# =========================

emotion_buffer = []

BUFFER_SIZE = 15

stable_emotion = "neutral"

last_face_log = time.time()

# =========================
# VOICE SYSTEM
# =========================

voice_emotion = "idle"

voice_processing = False

last_voice_check = 0

VOICE_INTERVAL = 15

# =========================
# FPS
# =========================

prev_frame_time = 0

# =========================
# VOICE THREAD
# =========================

def process_voice():

    global voice_emotion
    global voice_processing

    try:

        print("\n====================")
        print("VOICE ANALYSIS STARTED")
        print("====================")

        detected = (
            detect_voice_emotion()
        )

        voice_emotion = detected

        print(
            "\nVOICE RESULT:",
            voice_emotion
        )

        print("====================\n")

    except Exception as e:

        print(
            "VOICE ERROR:",
            e
        )

    voice_processing = False

# =========================
# MAIN LOOP
# =========================

while True:

    ret, frame = cap.read()

    if not ret:

        break

    current_time = time.time()

    try:

        # =========================
        # FACE DETECTION
        # =========================

        emotion_data = detect_emotion(
            frame
        )

        detected_emotion = (
            emotion_data['emotion']
        )

        # =========================
        # EMOTION BUFFER
        # =========================

        emotion_buffer.append(
            detected_emotion
        )

        if len(emotion_buffer) > BUFFER_SIZE:

            emotion_buffer.pop(0)

        # Majority vote
        stable_emotion = (
            Counter(
                emotion_buffer
            ).most_common(1)[0][0]
        )

        emotion_data['emotion'] = (
            stable_emotion
        )

        # =========================
        # FACE LOGGING
        # =========================

        if (
            current_time
            - last_face_log
            > 3
        ):

            print(
                "FACE STATE:",
                stable_emotion
            )

            last_face_log = (
                current_time
            )

        # =========================
        # VOICE ANALYSIS
        # =========================

        if (
            current_time
            - last_voice_check
            > VOICE_INTERVAL
            and not voice_processing
        ):

            voice_processing = True

            last_voice_check = (
                current_time
            )

            threading.Thread(
                target=process_voice,
                daemon=True
            ).start()

        # =========================
        # DRAW FACE OVERLAY
        # =========================

        frame = draw_overlay(
            frame,
            emotion_data
        )

        # =========================
        # FINAL STATE
        # =========================

        final_state = (
            f"FACE: "
            f"{stable_emotion.upper()} | "
            f"VOICE: "
            f"{voice_emotion.upper()}"
        )

        cv2.putText(
            frame,
            final_state,
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.75,
            (0, 0, 255),
            2
        )

        # =========================
        # VOICE STATUS
        # =========================

        voice_status = (
            "VOICE ACTIVE"
            if voice_processing
            else "VOICE READY"
        )

        cv2.putText(
            frame,
            voice_status,
            (20, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 255, 0),
            2
        )

        # =========================
        # FPS
        # =========================

        new_frame_time = time.time()

        fps = int(
            1 / (
                new_frame_time
                - prev_frame_time
                + 0.0001
            )
        )

        prev_frame_time = (
            new_frame_time
        )

        cv2.putText(
            frame,
            f"FPS: {fps}",
            (20, 120),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
            2
        )

    except Exception as e:

        print("ERROR:", e)

    # =========================
    # DISPLAY
    # =========================

    cv2.imshow(
        "Emotion Intelligence System",
        frame
    )

    # Exit
    if cv2.waitKey(1) & 0xFF == ord('q'):

        break

# =========================
# CLEANUP
# =========================

cap.release()

cv2.destroyAllWindows()
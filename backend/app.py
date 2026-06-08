import cv2
import time
from collections import Counter

from vision.emotion_engine import detect_emotion

from vision.ui_renderer import (
    draw_overlay
)

from vision.analytics_engine import (
    update_emotion_history,
    get_dominant_emotion,
    get_stability_score
)

from vision.timeline_graph import (
    update_graph,
    draw_graph
)

from vision.state_inference import (
    infer_state
)

print("EMOTION INTELLIGENCE SYSTEM STARTED")

# =========================
# CAMERA INITIALIZATION
# =========================

cap = cv2.VideoCapture(0)

# =========================
# EMOTION BUFFER SYSTEM
# =========================

emotion_buffer = []

BUFFER_SIZE = 15

stable_emotion = "neutral"

# =========================
# FPS VARIABLES
# =========================

prev_frame_time = 0

# =========================
# MAIN LOOP
# =========================

while True:

    ret, frame = cap.read()

    if not ret:

        print("Camera error")

        break

    try:

        # =========================
        # DETECT EMOTION
        # =========================

        emotion_data = detect_emotion(
            frame
        )

        detected_emotion = emotion_data[
            'emotion'
        ]

        # =========================
        # EMOTION STABILIZATION
        # =========================

        emotion_buffer.append(
            detected_emotion
        )

        if len(emotion_buffer) > BUFFER_SIZE:

            emotion_buffer.pop(0)

        stable_emotion = (
            Counter(
                emotion_buffer
            ).most_common(1)[0][0]
        )

        emotion_data['emotion'] = (
            stable_emotion
        )

        # =========================
        # UPDATE ANALYTICS
        # =========================

        update_emotion_history(
            stable_emotion
        )

        update_graph(
            stable_emotion
        )

        dominant_emotion = (
            get_dominant_emotion()
        )

        stability_score = (
            get_stability_score()
        )

        # =========================
        # SMART AI STATE
        # =========================

        smart_state = infer_state(
            dominant_emotion,
            stability_score
        )

        # =========================
        # FPS CALCULATION
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

        # =========================
        # DRAW PREMIUM UI
        # =========================

        frame = draw_overlay(
            frame,
            emotion_data,
            fps
        )

        # =========================
        # DRAW TIMELINE GRAPH
        # =========================

        frame = draw_graph(
            frame
        )

        # =========================
        # ANALYTICS DISPLAY
        # =========================

        cv2.putText(
            frame,
            f"Dominant: "
            f"{dominant_emotion.upper()}",
            (20, 190),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 0),
            2
        )

        cv2.putText(
            frame,
            f"Stability: "
            f"{stability_score}%",
            (20, 225),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 255),
            2
        )

        cv2.putText(
            frame,
            f"AI State: "
            f"{smart_state}",
            (20, 260),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

    except Exception as e:

        print("ERROR:", e)

    # =========================
    # SHOW WINDOW
    # =========================

    cv2.imshow(
        "Emotion Intelligence System",
        frame
    )

    # =========================
    # EXIT KEY
    # =========================

    if cv2.waitKey(1) & 0xFF == ord('q'):

        break

# =========================
# CLEANUP
# =========================

cap.release()

cv2.destroyAllWindows()
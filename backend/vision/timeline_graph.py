import cv2
import numpy as np

# =========================
# EMOTION VALUES
# =========================

emotion_map = {

    "angry": 1,

    "sad": 2,

    "neutral": 3,

    "happy": 4,

    "surprise": 5
}

# =========================
# HISTORY
# =========================

emotion_points = []

MAX_POINTS = 120

# =========================
# UPDATE GRAPH
# =========================

def update_graph(
    emotion
):

    value = emotion_map.get(
        emotion,
        3
    )

    emotion_points.append(
        value
    )

    if len(emotion_points) > MAX_POINTS:

        emotion_points.pop(0)

# =========================
# DRAW GRAPH
# =========================

def draw_graph(
    frame
):

    height, width, _ = frame.shape

    graph_width = 420

    graph_height = 140

    start_x = 20

    start_y = height - 180

    # =========================
    # PANEL
    # =========================

    overlay = frame.copy()

    cv2.rectangle(
        overlay,
        (start_x, start_y),
        (
            start_x + graph_width,
            start_y + graph_height
        ),
        (40, 40, 40),
        -1
    )

    cv2.addWeighted(
        overlay,
        0.4,
        frame,
        0.6,
        0,
        frame
    )

    # =========================
    # TITLE
    # =========================

    cv2.putText(
        frame,
        "Emotion Timeline",
        (start_x + 15, start_y + 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )

    # =========================
    # DRAW LINES
    # =========================

    if len(emotion_points) > 1:

        spacing = (
            graph_width
            / MAX_POINTS
        )

        points = []

        for i, value in enumerate(
            emotion_points
        ):

            x = int(
                start_x
                + i * spacing
            )

            y = int(
                start_y
                + graph_height
                - (value * 20)
            )

            points.append((x, y))

        for i in range(
            1,
            len(points)
        ):

            cv2.line(
                frame,
                points[i - 1],
                points[i],
                (0, 255, 255),
                2
            )

    # =========================
    # LABELS
    # =========================

    labels = {

        1: "ANGRY",

        2: "SAD",

        3: "NEUTRAL",

        4: "HAPPY",

        5: "SURPRISE"
    }

    for value, label in labels.items():

        y = int(
            start_y
            + graph_height
            - (value * 20)
        )

        cv2.putText(
            frame,
            label,
            (start_x + 320, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.4,
            (200, 200, 200),
            1
        )

    return frame

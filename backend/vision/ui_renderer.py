import cv2

print("PREMIUM UI RENDERER LOADED")

# =========================
# EMOTION COLORS
# =========================

emotion_colors = {

    "happy": (0, 255, 0),

    "sad": (255, 0, 0),

    "angry": (0, 0, 255),

    "fear": (255, 0, 255),

    "surprise": (0, 255, 255),

    "neutral": (200, 200, 200),

    "disgust": (0, 120, 0)
}

# =========================
# DRAW PANEL
# =========================

def draw_panel(
    frame,
    x,
    y,
    w,
    h,
    color=(40, 40, 40)
):

    overlay = frame.copy()

    cv2.rectangle(
        overlay,
        (x, y),
        (x + w, y + h),
        color,
        -1
    )

    alpha = 0.4

    cv2.addWeighted(
        overlay,
        alpha,
        frame,
        1 - alpha,
        0,
        frame
    )

# =========================
# DRAW CONFIDENCE BAR
# =========================

def draw_confidence_bar(
    frame,
    confidence,
    x,
    y,
    w,
    h,
    color
):

    # Background
    cv2.rectangle(
        frame,
        (x, y),
        (x + w, y + h),
        (80, 80, 80),
        -1
    )

    # Filled bar
    filled_width = int(
        (confidence / 100) * w
    )

    cv2.rectangle(
        frame,
        (x, y),
        (x + filled_width, y + h),
        color,
        -1
    )

# =========================
# MAIN OVERLAY
# =========================

def draw_overlay(
    frame,
    emotion_data,
    fps=0
):

    emotion = emotion_data[
        'emotion'
    ]

    confidence = round(
        emotion_data[
            'confidence'
        ],
        1
    )

    color = emotion_colors.get(
        emotion,
        (255, 255, 255)
    )

    height, width, _ = frame.shape

    # =========================
    # TOP PANEL
    # =========================

    draw_panel(
        frame,
        15,
        15,
        380,
        140
    )

    # Title
    cv2.putText(
        frame,
        "Emotion Intelligence System",
        (30, 45),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 255),
        2
    )

    # Emotion
    cv2.putText(
        frame,
        f"Emotion: {emotion.upper()}",
        (30, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.75,
        color,
        2
    )

    # Confidence
    cv2.putText(
        frame,
        f"Confidence: {confidence}%",
        (30, 110),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 255, 255),
        2
    )

    # Confidence bar
    draw_confidence_bar(
        frame,
        confidence,
        30,
        125,
        320,
        15,
        color
    )

    # =========================
    # FPS PANEL
    # =========================

    draw_panel(
        frame,
        width - 170,
        15,
        150,
        60
    )

    cv2.putText(
        frame,
        f"FPS: {fps}",
        (width - 150, 52),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 0),
        2
    )

    return frame
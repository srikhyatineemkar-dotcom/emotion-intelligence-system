# Emotion Intelligence System

A real-time AI-powered emotion recognition and analytics system developed using Python, OpenCV, DeepFace, and TensorFlow.

The system detects human facial emotions through webcam input, validates emotional consistency over time, logs emotional states, and generates session-based emotion analytics.

---

## Features

* Real-time facial emotion recognition
* Emotion stability threshold validation
* Temporal emotion tracking
* Real-time FPS monitoring
* Emotion logging to CSV
* Session emotion analytics
* Dominant emotion detection
* Modular project architecture
* Git and GitHub integration

---

## Technologies Used

* Python 3.11
* OpenCV
* DeepFace
* TensorFlow
* tf-keras
* CSV-based analytics
* Git & GitHub

---

## Project Structure

```text id="4n3m2p"
Emotion-Intelligence-System/
│
├── backend/
│   ├── app.py
│   │
│   └── vision/
│       ├── emotion_engine.py
│       ├── ui_renderer.py
│       ├── emotion_logger.py
│       └── emotion_stats.py
│
├── screenshots/
├── emotion_log.csv
├── README.md
└── .gitignore
```

---

## System Workflow

1. Webcam captures live video feed
2. DeepFace performs facial emotion analysis
3. Temporal validation confirms stable emotions
4. Stable emotions are logged into a CSV file
5. Session analytics summarize emotional behavior
6. FPS counter monitors real-time system performance

---

## Session Analytics Example

```text id="9x1k7q"
========================================
SESSION EMOTION SUMMARY
========================================

neutral   : 33.3%
happy     : 22.2%
surprise  : 22.2%
sad       : 11.1%
angry     : 11.1%

Dominant Emotion: neutral
========================================
```

---

## Future Enhancements

* Voice emotion recognition
* Emotion trend visualization
* Web-based dashboard
* Digital avatar integration
* Multimodal emotion fusion
* Cloud deployment

---

## Running the Project

```bash id="6p8v2m"
python backend/app.py
```

---

## Screenshots

Add project screenshots inside the `screenshots/` folder and reference them here.

---

## Author

Developed by Khyati Neemkar

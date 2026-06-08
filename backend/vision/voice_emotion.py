import sounddevice as sd
import numpy as np
import librosa

# =========================
# AUDIO SETTINGS
# =========================

SAMPLE_RATE = 22050

# =========================
# RECORD AUDIO
# =========================

def record_audio():

    print("\nSpeak now...")

    # Silence detection settings
    silence_threshold = 0.01
    silence_duration = 1.0

    # Small chunks for real-time detection
    chunk_duration = 0.2

    chunk_size = int(
        SAMPLE_RATE * chunk_duration
    )

    recording = []

    silence_time = 0

    while True:

        # Record chunk
        audio_chunk = sd.rec(
            chunk_size,
            samplerate=SAMPLE_RATE,
            channels=1,
            dtype='float32'
        )

        sd.wait()

        audio_chunk = audio_chunk.flatten()

        recording.append(audio_chunk)

        # Calculate current volume
        volume = np.mean(
            np.abs(audio_chunk)
        )

        # Silence detection
        if volume < silence_threshold:

            silence_time += chunk_duration

        else:

            silence_time = 0

        # Stop recording after silence
        if silence_time >= silence_duration:

            print(
                "\nSilence detected. Processing..."
            )

            break

    # Merge all chunks
    full_audio = np.concatenate(
        recording
    )

    return full_audio

# =========================
# DETECT VOICE EMOTION
# =========================

def detect_voice_emotion():

    audio = record_audio()

    # =========================
    # NORMALIZE AUDIO
    # =========================

    max_value = np.max(
        np.abs(audio)
    )

    if max_value > 0:

        audio = audio / max_value

    # =========================
    # FEATURE EXTRACTION
    # =========================

    # Voice energy
    rms = np.mean(
        librosa.feature.rms(y=audio)
    )

    # Voice brightness / pitch
    spectral_centroid = np.mean(
        librosa.feature.spectral_centroid(
            y=audio,
            sr=SAMPLE_RATE
        )
    )

    # =========================
    # DEBUG VALUES
    # =========================

    print("\nRMS:", rms)

    print(
        "Spectral Centroid:",
        spectral_centroid
    )

    # =========================
    # EMOTION CLASSIFICATION
    # =========================

    if rms > 0.55 and spectral_centroid > 5000:

        emotion = "excited"

    elif rms < 0.25:

        emotion = "calm"

    elif spectral_centroid < 3000:

        emotion = "sad"

    else:

        emotion = "neutral"

    return emotion
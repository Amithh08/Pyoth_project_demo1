import os
from gtts import gTTS

# Create output folder
OUTPUT_FOLDER = "outputs"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


def text_to_speech(text, language="en", output_filename="translated_audio.mp3"):
    """
    Convert text into speech and save it as an MP3 file.

    Parameters:
        text (str): Text to convert into speech.
        language (str): Language code (default is English).
        output_filename (str): Name of the output MP3 file.

    Returns:
        str: Path to the generated MP3 file.
    """

    if not text.strip():
        raise ValueError("Text cannot be empty.")

    try:
        output_path = os.path.join(OUTPUT_FOLDER, output_filename)

        tts = gTTS(
            text=text,
            lang=language,
            slow=False
        )

        tts.save(output_path)

        return output_path

    except Exception as e:
        raise Exception(f"Text-to-Speech Error: {e}")

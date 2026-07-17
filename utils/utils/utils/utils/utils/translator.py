import pdfplumber
from deep_translator import GoogleTranslator


def extract_text_from_pdf(uploaded_pdf):
    """
    Extract text from a PDF file.

    Parameters:
        uploaded_pdf: Uploaded PDF file

    Returns:
        str: Extracted text
    """

    text = ""

    try:
        uploaded_pdf.seek(0)

        with pdfplumber.open(uploaded_pdf) as pdf:

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

        return text.strip()

    except Exception as e:
        raise Exception(f"Error extracting text: {e}")


def translate_text(text, target_language):
    """
    Translate text into the selected language.

    Parameters:
        text (str): Text to translate
        target_language (str): Language code

    Returns:
        str: Translated text
    """

    if not text.strip():
        raise ValueError("No text available for translation.")

    try:
        translator = GoogleTranslator(
            source="auto",
            target=target_language
        )

        translated_text = translator.translate(text)

        return translated_text

    except Exception as e:
        raise Exception(f"Translation Error: {e}")


def get_supported_languages():
    """
    Returns supported languages.

    Returns:
        dict
    """

    return {
        "English": "en",
        "Hindi": "hi",
        "Kannada": "kn",
        "Tamil": "ta",
        "Telugu": "te",
        "Malayalam": "ml",
        "French": "fr",
        "German": "de",
        "Spanish": "es",
        "Italian": "it",
        "Portuguese": "pt",
        "Japanese": "ja",
        "Korean": "ko",
        "Chinese (Simplified)": "zh-CN",
        "Arabic": "ar",
        "Russian": "ru"
    }

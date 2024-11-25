# sperma product by Антон 🍆💦
import sys
sys.stdout.reconfigure(encoding='utf-8')

from deep_translator import GoogleTranslator

def translate_text(sentences, source_lang='lv', target_lang='en'):
    translator = GoogleTranslator(source=source_lang, target=target_lang)
    translated_sentences = []

    for sentence in sentences:
        try:
            translated = translator.translate(sentence)
            translated_sentences.append(translated)
        except Exception as e:
            print(f"Kļūda tulkošanā: {e}")
            translated_sentences.append("Tulkošana neizdevās")

    return translated_sentences

latvian_sentences = [
    "Labdien! Kā jums klājas?",
    "Es šodien lasīju interesantu grāmatu.",
    "9. uzdevumu izdomāja pilnīgs deģenerāts."
]

translated_sentences = translate_text(latvian_sentences)

print("Tulkojumi:")
for idx, (original, translated) in enumerate(zip(latvian_sentences, translated_sentences), 1):
    print(f"{idx}. {original} -> {translated}")

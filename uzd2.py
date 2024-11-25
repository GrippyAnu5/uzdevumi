# sperma product by Антон 🍆💦

import langid
import sys

sys.stdout.reconfigure(encoding='utf-8')

texts = [
    "Šodien ir saulaina diena.",
    "Today is a sunny day."
]

for text in texts:
    language, confidence = langid.classify(text)
    print(f"Teksts: '{text}' - Valoda: {language}")



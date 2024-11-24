# sperma product by Антон 🍆💦
import sys
sys.stdout.reconfigure(encoding='utf-8')

import os
import stanza
from deep_translator import GoogleTranslator

project_dir = os.path.dirname(os.path.abspath(__file__))
stanza_resources_dir = os.path.join(project_dir, "stanza_resources")
os.environ["STANZA_RESOURCES_DIR"] = stanza_resources_dir

stanza.download('en')
nlp = stanza.Pipeline('en', download_method=None)\

text_lv = "Valsts prezidents Egils Levits piedalījās pasākumā, ko organizēja Latvijas Universitāte. Eiropas Starptautiskā spermas banka un LeBrons Džeims, kopā ar savu labāko draugu Antonu Legenoviču arī piedalījas pasākumā."

text_en = GoogleTranslator(source='lv', target='en').translate(text_lv)

doc = nlp(text_en)

def capitalize_proper_nouns(text):
    words = text.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)

print("\nIdentificētās vienības:")
for sentence in doc.sentences:
    for entity in sentence.ents:
        entity_lv = GoogleTranslator(source='en', target='lv').translate(entity.text)
        entity_lv_capitalized = capitalize_proper_nouns(entity_lv)
        
        entity_type = "PER" if entity.type == "PERSON" else entity.type
        print(f"{entity_lv_capitalized}: {entity_type}")

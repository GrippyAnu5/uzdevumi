# sperma product by Антон 🍆💦
import sys
sys.stdout.reconfigure(encoding='utf-8')

from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def automatiska_rezumesana(teksts, teikumu_skaits=2):
    summary = summarizer(teksts, max_length=teikumu_skaits * 30, min_length=teikumu_skaits * 10, do_sample=False)
    return summary[0]['summary_text']

teksts = """
Latvija ir valsts Baltijas reģionā. Tās galvaspilsēta ir Rīga, kas ir slavena ar savu vēsturisko centru un skaistajām ēkām.
Latvija robežojas ar Lietuvu, Igauniju un Krieviju, kā arī tai ir piekļuve Baltijas jūrai.
Tā ir viena no Eiropas Savienības dalībvalstīm.
"""

rezumets_teksts = automatiska_rezumesana(teksts, teikumu_skaits=2)

print("Raksta rezumējums:")
print(rezumets_teksts)

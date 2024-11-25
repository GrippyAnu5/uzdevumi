# sperma product by Антон 🍆💦
import sys
sys.stdout.reconfigure(encoding='utf-8')

from deep_translator import GoogleTranslator
from textblob import TextBlob

def noskanas_analize_ar_tulkojumu(teikumi):
    rezultati = []
    for teikums in teikumi:
        # tulko uz angļu valodu jo biblioēkas kas novērtē noskaņojumu ir pilnīga huiņa
        tulkots = GoogleTranslator(source='lv', target='en').translate(teikums)
        
        blob = TextBlob(tulkots)
        polaritate = blob.sentiment.polarity  # pievieno noskaņojumu
        
        if polaritate > 0.5:
            noskanas = "Pozitīvs"
        elif polaritate < -0.5:
            noskanas = "Negatīvs"
        else:
            noskanas = "Neitrāls"
        
        rezultati.append((teikums, noskanas, round(polaritate, 2)))
    return rezultati

teikumi = [
    "Šis produkts ir lielisks, esmu ļoti apmierināts!",
    "Esmu vīlies, produkts neatbilst aprakstam.",
    "Neitrāls produkts, nekas īpašs.",
    "Man garšo sperma. Tā ir ka saldais tiramisu deserts. Ļoti garšīgs deserts!",
    "Man negaršo sperma. Tas smird ka slikts siers."
]

rezultati = noskanas_analize_ar_tulkojumu(teikumi)

print("Teikumu noskaņojuma analīze:")
for teikums, noskanas, polaritate in rezultati:
    print(f"Teikums: \"{teikums}\" → Noskaņojums: {noskanas} (Polaritate: {polaritate})")

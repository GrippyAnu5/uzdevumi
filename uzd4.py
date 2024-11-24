# sperma product by Антон 🍆💦
import sys
sys.stdout.reconfigure(encoding='utf-8')

from transformers import pipeline

# Инициализация анализа настроений
analyzer = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

# Функция анализа
def noskanas_analize(teikumi):
    rezultati = []
    for teikums in teikumi:
        result = analyzer(teikums)[0]
        label = result['label']
        score = result['score']
        
        # Классификация настроений
        if "5" in label or "4" in label:
            noskanas = "Pozitīvs"
        elif "1" in label or "2" in label:
            noskanas = "Negatīvs"
        else:
            noskanas = "Neitrāls"
        
        rezultati.append((teikums, noskanas, round(score, 2)))
    return rezultati

# Teikumi
teikumi = [
    "Šis produkts ir lielisks, esmu ļoti apmierināts!",
    "Esmu vīlies, produkts neatbilst aprakstam.",
    "Neitrāls produkts, nekas īpašs."
]

# Анализ
rezultati = noskanas_analize(teikumi)

# Вывод результата
print("Teikumu noskaņojuma analīze:")
for teikums, noskanas, score in rezultati:
    print(f"Teikums: \"{teikums}\" → Noskaņojums: {noskanas} (Precizitāte: {score})")

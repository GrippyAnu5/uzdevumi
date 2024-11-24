# sperma product by Антон 🍆💦

from collections import Counter
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

teksts = "Mākoņainā dienā kaķis sēdēja uz palodzes. Kaķis domāja, kāpēc debesis ir pelēkas. Kaķis gribēja redzēt sauli, bet saule slēpās aiz mākoņiem."

# vardi ko nevajg skaitit
stop_vardi = {'ir', 'uz', 'kāpēc', 'bet', 'aiz', 'un', 'ka'}

def analizet_vardu_biezumu(teksts, stop_vardi):
    vardi = re.findall(r'\b\w+\b', teksts.lower())
    
    filtrimie_vardi = [vards for vards in vardi if vards not in stop_vardi]
    
    vardu_biezums = Counter(filtrimie_vardi)
    
    sakartotais_biezums = sorted(vardu_biezums.items(), key=lambda x: x[1], reverse=True)
    
    return sakartotais_biezums

rezultats = analizet_vardu_biezumu(teksts, stop_vardi)

print("Vārdu biežums (bez stop-vārdiem):")
for vards, biežums in rezultats:
    print(f"'{vards}': {biežums}")

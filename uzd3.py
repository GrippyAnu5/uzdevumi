# sperma product by Антон 🍆💦
import sys
sys.stdout.reconfigure(encoding='utf-8')

import re

# Funkcija vārdu sakritību identificēšanai un procentuālā līmeņa aprēķināšanai
def sakritibu_parbaude(teksts1, teksts2):
    # Pārveido tekstu uz mazajiem burtiem un izvelk vārdus
    vardi1 = set(re.findall(r'\b\w+\b', teksts1.lower()))
    vardi2 = set(re.findall(r'\b\w+\b', teksts2.lower()))
    
    # Identificē sakritības
    sakritibas = vardi1 & vardi2
    
    # Aprēķina procentuālo sakritību
    kopskaits = len(vardi1 | vardi2)  # Apvienotais unikālo vārdu skaits
    sakritibas_procents = (len(sakritibas) / kopskaits) * 100 if kopskaits > 0 else 0
    
    return sakritibas, round(sakritibas_procents, 2)

# Teksti
teksts1 = "Rudens lapas ir dzeltenas un oranžas. Lapas klāj zemi un padara to krāsainu."
teksts2 = "Krāsainas rudens lapas krīt zemē. Lapas ir oranžas un dzeltenas."

# Sakritību pārbaude
sakritibas, procents = sakritibu_parbaude(teksts1, teksts2)

# Rezultātu izvadīšana
print("Vārdu sakritības starp tekstiem:")
print(f"Sakritības vārdi: {', '.join(sakritibas)}")
print(f"Sakritības līmenis: {procents}%")

# sperma product by Антон 🍆💦
import sys
sys.stdout.reconfigure(encoding='utf-8')

import re

def cleaning(teksts):
    # "lietotājs"
    teksts = re.sub(r'@\w+', '', teksts)
    
    # URL
    teksts = re.sub(r'http[s]?://\S+', '', teksts)
    
    # simbolus un emoji
    teksts = re.sub(r'[^\w\s]', '', teksts)
    
    teksts = teksts.lower()
    
    # atstarpes
    teksts = re.sub(r'\s+', ' ', teksts).strip()
    
    return teksts

neapstradats_teksts = "@John: Šis ir lielisks produkts!!! Vai ne? 👏 👏 👏 http://example.com"

# Tīrīšana un normalizēšana
tirs_teksts = cleaning(neapstradats_teksts)

# Rezultāta izvadīšana
print("Tīrais teksts:")
print(tirs_teksts)

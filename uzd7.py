# sperma product by Антон 🍆💦
import sys
sys.stdout.reconfigure(encoding='utf-8')

from gensim.models import KeyedVectors
import urllib.request
import gzip
import os

model_url = "https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.lv.300.vec.gz"
model_path = "cc.lv.300.vec"
cache_dir = "cache"
cache_model_path = os.path.join(cache_dir, "cc.lv.300.kv")

# Funkcija modeļa lejupielādei un izvilkšanai
def download_model(url, output_path):
    if not os.path.exists(output_path):
        print("Modeļa lejupielāde...")
        compressed_file = output_path + ".gz"
        urllib.request.urlretrieve(url, compressed_file)
        print("Lejupielāde pabeigta. Izvilkšana...")
        with gzip.open(compressed_file, "rb") as f_in, open(output_path, "wb") as f_out:
            f_out.write(f_in.read())
        os.remove(compressed_file)
        print("Izvilkšana pabeigta.")
    else:
        print("Modelis jau eksistē. Lejupielādes izlaišana.")

# Funkcija modeļa ielādei ar kešu
def load_model_with_cache(cache_path, vec_path):
    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir)
        print(f"Izveidota kešatmiņas mape: <{cache_dir}>")

    if os.path.exists(cache_path):
        try:
            print("Ielādē modelis no kešatmiņas...")
            model = KeyedVectors.load(cache_path)
            print("Ielāde no kešatmiņas pabeigta.")
            return model
        except Exception as e:
            print(f"Neizdevās ielādēt modeli no kešatmiņas: {e}. Ielādē no vektora faila...")

    print("Ielādē modelis no vektora faila...")
    model = KeyedVectors.load_word2vec_format(vec_path, binary=False)
    print("Modelis ielādēts. Saglabā kešatmiņā...")
    model.save(cache_path)
    print("Modelis saglabāts kešatmiņā.")
    return model

# Funkcija salīdzināt vektorus un aprēķināt līdzības
def salidzinat_vardus(model, vardi):
    rezultati = {}
    for vards in vardi:
        if vards in model:
            rezultati[vards] = model[vards]
        else:
            print(f"Vārds '{vards}' nav atrodams modelī.")
    
    # Salīdzinām līdzības starp vārdiem
    salidzinajumi = []
    for i, vards1 in enumerate(vardi):
        for j, vards2 in enumerate(vardi):
            if i < j:
                similarity = model.similarity(vards1, vards2)
                salidzinajumi.append((vards1, vards2, similarity))
    return rezultati, salidzinajumi

# Lejupielādē un ielādē modeli
download_model(model_url, model_path)
model = load_model_with_cache( cache_model_path , model_path)

vardi = ["māja", "dzīvoklis", "jūra", "ūdens", "sperma"]

vektori, salidzinajumi = salidzinat_vardus(model, vardi)

print("\nVārdu vektori:")
for vards, vektors in vektori.items():
    print(f"{vards}: {vektors[:3]}...")

print("\nSemantisks salidzinājums:")
for vards1, vards2, similarity in salidzinajumi:
    print(f"Līdzība starp '{vards1}' un '{vards2}': {similarity:.4f}")

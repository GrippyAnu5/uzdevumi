# sperma product by Антон 🍆💦
import sys
sys.stdout.reconfigure(encoding='utf-8')

from transformers import GPT2LMHeadModel, GPT2Tokenizer
from deep_translator import GoogleTranslator
import stanza
import re
import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk
import threading
import queue

loading_queue = queue.Queue()

def initialize_components():
    global nlp, tokenizer, model
    stanza.download('lv')
    nlp = stanza.Pipeline('lv')

    model_name = "gpt2"
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    model = GPT2LMHeadModel.from_pretrained(model_name)

    if tokenizer.pad_token_id is None:
        tokenizer.pad_token_id = tokenizer.eos_token_id

    loading_queue.put("Pabeigts!")

def generate_text():
    prompt_en = "Once upon a time in some distant land ..."

    input_ids = tokenizer.encode(prompt_en, return_tensors="pt")
    attention_mask = (input_ids != tokenizer.pad_token_id).long()

    output = model.generate(
        input_ids,
        attention_mask=attention_mask,
        max_length=120,
        num_return_sequences=1,
        no_repeat_ngram_size=3,
        top_k=50,
        top_p=0.9,
        temperature=0.8,
        do_sample=True,
        pad_token_id=tokenizer.pad_token_id,
    )

    generated_text_en = tokenizer.decode(output[0], skip_special_tokens=True)
    generated_text_en = clean_generated_text(generated_text_en)

    try:
        generated_text_lv = GoogleTranslator(source="en", target="lv").translate(generated_text_en)
    except Exception as e:
        generated_text_lv = generated_text_en

    generated_text_lv = stanza_correction(generated_text_lv)
    generated_text_lv = finalize_text(generated_text_lv)

    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, generated_text_lv)

def clean_generated_text(text):
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'\d+', '', text)
    sentences = text.split('. ')
    unique_sentences = []
    for sentence in sentences:
        sentence = sentence.strip()
        if sentence and sentence not in unique_sentences:
            unique_sentences.append(sentence + '.')
    return ' '.join(unique_sentences[:4])

def stanza_correction(text):
    doc = nlp(text)
    corrected_text = []
    for sentence in doc.sentences:
        tokens = [word.text.capitalize() if i == 0 else word.text for i, word in enumerate(sentence.words)]
        corrected_text.append(' '.join(tokens))
    return ' '.join(corrected_text)

def finalize_text(text):
    doc = nlp(text)
    corrected_tokens = []
    for word in text.split():
        if word.lower() in [entity.text.lower() for entity in doc.entities]:
            corrected_tokens.append(word.capitalize())
        else:
            corrected_tokens.append(word)
    text = ' '.join(corrected_tokens)

    text = re.sub(r'\s+([,.?!:;])', r'\1', text)
    text = re.sub(r'([,.?!:;])(\w)', r'\1 \2', text)
    text = text.strip('. ') + '.'

    text = re.sub(r'"\s+', '"', text)
    text = re.sub(r'\s+"', '"', text)

    open_quotes = text.count('"') % 2
    if open_quotes == 1:
        text += '"'

    return text

def check_loading_status():
    try:
        message = loading_queue.get_nowait()
        if message == "Pabeigts!":
            loading_window.destroy()
            open_main_window()
    except queue.Empty:
        loading_window.after(100, check_loading_status)

loading_window = tk.Tk()
loading_window.title("Pagaidiet")
loading_window.geometry("300x100")
loading_label = tk.Label(loading_window, text="Spermas komponentu ieladešana ...")
loading_label.pack(pady=10)
progress = ttk.Progressbar(loading_window, mode='indeterminate')
progress.pack(pady=10)
progress.start()

threading.Thread(target=initialize_components, daemon=True).start()

loading_window.after(100, check_loading_status)

def open_main_window():
    global result_text
    main_window = tk.Tk()
    main_window.title("Spermas ģenerators")

    frame = tk.Frame(main_window)
    frame.pack(padx=10, pady=10)

    generate_button = tk.Button(frame, text="Ģenerēt spermu", command=generate_text)
    generate_button.pack(pady=10)

    result_text = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=60, height=15, font=("Times New Roman", 12))
    result_text.pack()

    main_window.mainloop()

loading_window.mainloop()

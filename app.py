from flask import Flask, request, jsonify, render_template
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from datetime import datetime

app = Flask(__name__)

# GPT-2 modelini ve tokenizer'ı yükle
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-dilekce', methods=['POST'])
def generate_dilekce():
    data = request.get_json()
    kisi_adi = data.get('kisiAdi', 'Yetkili Kişi/Makam')
    anahtar_kelime = data.get('anahtarKelime', 'Anahtar Kelime Girilmedi')
    
    prompt = f"Dilekçe konusuna uygun bir metin oluştur. Anahtar kelime: {anahtar_kelime}"
    input_ids = tokenizer.encode(prompt, return_tensors='pt')

    # GPT-2 modelini kullanarak metin oluştur
    output = model.generate(input_ids, max_length=300, num_return_sequences=1)
    metin = tokenizer.decode(output[0], skip_special_tokens=True)

    # Dilekçe formatı
    dilekce = f"""Sayın {kisi_adi},

Konu: {anahtar_kelime.capitalize()}

{metin}

Gereğinin yapılmasını arz ederim.

Tarih: {datetime.now().strftime('%d-%m-%Y')}"""

    return jsonify({'generated_text': dilekce})

if __name__ == '__main__':
    app.run(debug=True)

#pip install Pillow

from PIL import Image
import hashlib

def calcular_hash_imagem(imagem, algoritmo='sha256'):
    with open(imagem, 'rb') as arquivo_imagem:
        conteudo = arquivo_imagem.read()
        hash_imagem = hashlib.new(algoritmo, conteudo).hexdigest()
    return hash_imagem

imagem = "./img/IMG_20240322_204840.jpg"

im = Image.open(imagem)

exif_data = im._getexif()

dados = {
    0x9003: "Data e hora", 
    0x010F: "Fabricante",   
    0x0110: "Modelo"   
}

for chave, value in exif_data.items():
    if chave in dados:
        print(dados[chave] + ":", value)

hash_imagem = calcular_hash_imagem(imagem)

print("Hash da imagem:", hash_imagem)

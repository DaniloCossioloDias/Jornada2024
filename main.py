from PIL import Image
im = Image.open("./img/")

exif_data = im._getexif()
print(exif_data)

for key, value in exif_data.items():
    print(key, value)
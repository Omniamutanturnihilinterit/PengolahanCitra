from PIL import Image

def grayscale(image):
    # Konversi gambar ke skala abu-abu
    return image.convert("L")

def resize(image, width, height):
    # Mengubah ukuran gambar
    return image.resize((width, height))

def rotate(image, angle):
    # Memutar gambar sebesar sudut tertentu
    return image.rotate(angle)

def save(image, output_path):
    # Menyimpan gambar ke file
    image.save(output_path)

# Contoh penggunaan
input_image = Image.open("input.jpg")

# Mengubah gambar menjadi skala abu-abu
grayscale_image = grayscale(input_image)
save(grayscale_image, "grayscale.jpg")

# Mengubah ukuran gambar
resized_image = resize(input_image, 800, 600)
save(resized_image, "resized.jpg")

# Memutar gambar sebesar 45 derajat
rotated_image = rotate(input_image, 45)
save(rotated_image, "rotated.jpg")

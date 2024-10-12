from PIL import Image

def shift_pixels(image_path):
    # Resmi aç ve RGBA formatına dönüştür
    image = Image.open(image_path).convert('RGBA')

    # Genişlik ve yükseklik bilgilerini al
    width, height = image.size

    # Tüm pikselleri al
    pixels = list(image.getdata())

    # Yeni pikselleri depolamak için boş bir liste oluştur
    shifted_pixels = []

    # Her satır için kaydırma işlemini uygula
    for y in range(height):
        start_index = y * width
        end_index = start_index + width
        row_pixels = pixels[start_index:end_index]  # Satırı al

        # Bir sağa kaydır, sonuncu pikseli en başa koy
        shifted_row = [row_pixels[-5]] + row_pixels[:-2]

        # Kaydırılmış satırı yeni piksel listesine ekle
        shifted_pixels.extend(shifted_row)

    # Yeni piksellerle bir resim oluştur
    shifted_image = Image.new(image.mode, image.size)
    shifted_image.putdata(shifted_pixels)

    return shifted_image

# Orijinal resim yolu
image_path = "orijinal resimler/anahtar2.png"

# Piksel kaydırma işlemi
shifted_image = shift_pixels(image_path)

# Kaydırılmış resim kaydedilecek yol
shifted_image_path = "degismis resimler/kaydirilmis_resim.png"
shifted_image.save(shifted_image_path)

print(f"Pikseller sağa kaydırıldı, resim kaydedildi: {shifted_image_path}")

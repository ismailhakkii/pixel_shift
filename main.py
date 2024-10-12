from PIL import Image

def shift_pixels(image_path):
    image = Image.open(image_path).convert('RGBA')
    width, height = image.size
    pixels = list(image.getdata())

    shifted_pixels = []

    for y in range(height):
        start_index = y * width
        end_index = start_index + width
        row_pixels = pixels[start_index:end_index]
        shifted_row = [row_pixels[-5]] + row_pixels[:-2]
        shifted_pixels.extend(shifted_row)

    shifted_image = Image.new(image.mode, image.size)
    shifted_image.putdata(shifted_pixels)

    return shifted_image

image_path = "orijinal resimler/anahtar2.png"
shifted_image = shift_pixels(image_path)
shifted_image_path = "degismis resimler/kaydirilmis_resim.png"
shifted_image.save(shifted_image_path)

print(f"Pikseller kaydırıldı ve resim kaydedildi: {shifted_image_path}")

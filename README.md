
# Piksel Kaydırma Görüntü İşleme Programı

Bu proje, bir resmi okuyan, her satırdaki pikselleri belirli bir miktarda kaydıran ve ardından değiştirilen resmi kaydeden basit bir görüntü işleme betiğidir. Kod Python ile yazılmıştır ve görüntü işleme için Pillow kütüphanesi kullanır.

## Özellikler
- Belirtilen bir yoldan görüntü yükler
- Görüntüyü RGBA formatına dönüştürür
- Her satırdaki pikselleri, son 5 pikseli başa alıp diğerlerini iki pozisyon kaydırarak düzenler
- Değiştirilen görüntüyü yeni bir dosyaya kaydeder

## Gereksinimler

Bu betiği çalıştırmak için aşağıdaki yazılımların yüklü olması gerekir:

- Python 3.x
- Pillow (Python Görüntü Kütüphanesi)

Pillow’u pip ile yükleyebilirsiniz:
```bash
pip install Pillow
```

## Nasıl Çalışır

1. Betik, `image_path` ile belirtilen görüntüyü açar.
2. Görüntüyü RGBA moduna dönüştürür (şeffaflık yönetimi için).
3. Görüntünün piksel verilerini alır ve her satırı tek tek işler.
4. Her satır için, son 50 pikseli öne alır ve kalan pikselleri 37 pozisyon kaydırır.
5. İşlenen görüntü, belirtilen çıkış yoluna kaydedilir.

## Kullanım

1. Resminizi `orijinal resimler/` klasörüne yerleştirin.
2. Betiği çalıştırın, bu işlem görüntüyü işleyip sonucu `degismis resimler/` klasörüne kaydedecektir.
3. İşlenmiş resim, betikte belirtilen kaydırma mantığına göre pikselleri kaydırılmış olacaktır.

## Dosya Yapısı

```
/proje-klasörü
│
├── /orijinal resimler/
│   └── anahtar2.png          # Orijinal giriş görüntüsü
├── /degismis resimler/
│   └── kaydirilmis_resim.png  # Çıktı kaydırılmış görüntü
└── main.py            # Main
```
## Projeden Ekran Görüntüleri
1. 
![image](https://github.com/user-attachments/assets/329da666-f611-4e18-84a4-a158b4c26790)
![image](https://github.com/user-attachments/assets/264769ab-4183-4954-8b45-fdeba69fa489)

2. 
![image](https://github.com/user-attachments/assets/9b2c9443-9d9b-4aaf-9c10-ef00f42c8930)
![image](https://github.com/user-attachments/assets/f7e6858d-a7de-43a9-a6d4-86c6c7d9eb9a)



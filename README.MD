# STEGANOGRAPHY LSB

## Görüntü Steganografisi
Bu proje, görüntü dosyalarının içine gizli mesajlar gizleme uygulaması olan görüntü steganografisinin bir uygulamasını sunar. Kod, bir mesajı görüntünün piksel verilerinin en önemsiz bitlerini değiştirerek görüntüye kodlayabilmenize ve ardından değiştirilmiş görüntüden mesajı çözebilmenize olanak tanır. Bu teknik, "En Önemsiz Bit (Least Significant Bit - LSB)" algoritması olarak bilinir.

### LSB Algoritması

![LSB](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgfSk6jWFUDw31Mreg87dmYghgWOytYmrq00kP_j58w0hdUz71hcczpoJeP6Uuw9Rzbpxy1c-jzb7xkRhTOjoMiB5dgrnAi407AhLPxXx7hYR6o3UzkZi-zMk2cWFN7h4jvuY8Z6M92jWs/s1600/encode.png)
LSB algoritması, bir görüntünün her pikselinin en önemsiz bitlerini değiştirerek gizli bir mesajı kodlamak için kullanılır. Bu algoritma, insan gözünün bu küçük değişiklikleri fark edemeyeceği varsayımına dayanır. Mesaj, her pikselin en önemsiz bitlerini değiştirerek kodlanır ve bu sayede görüntü neredeyse değişmeden kalır.

### Kurulum
Bu proje Python 3 ile geliştirilmiş ve test edilmiştir. Projeyi çalıştırmak için Python 3 ve aşağıdaki kütüphanelerin yüklü olması gerekir:

- OpenCV (cv2)
- NumPy (numpy)
Bu kütüphaneleri pip3 ile yükleyebilirsiniz:

```
pip3 install opencv-python numpy
```


### Kullanım
Repoyu Klonlama
Bu projeyi kullanmak için öncelikle GitHub'dan repoyu klonlamanız gerekir. Bunu yapmak için aşağıdaki komutu kullanabilirsiniz:

```
git clone https://github.com/emirhancibir/stega_lsb.git
```


### Kodlama (Encoding)
Bir mesajı bir görüntüye kodlamak için encode.py betiğini çalıştırın:
```
python3 encode.py
```


Bu betik, varsayılan olarak imgs/panda.png görüntüsüne "313131 lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua." mesajını kodlar. Kodlanmış görüntü imgs/encoded.png olarak kaydedilir.

#### Örnek çalıştırma:
```
$ python3 encode.py
INSERTION COMPLETED
```


### Orjinal Görüntü
![Orjinal Görüntü](docs/imgs/panda.png)

### Kodlanmış Görüntü
![Kodlanmıs Görüntü](docs/imgs/encoded.png)


### Çözme (Decoding)
Kodlanmış bir görüntüden mesajı çözmek için decode.py betiğini çalıştırın:
```
python3 decode.py
```


Bu betik, varsayılan olarak imgs/encoded.png dosyasından gizli mesajı çözer ve konsola yazdırır.

#### Örnek çalıştırma:
```
$ python3 decode.py
------------------------------
SECRET MESSAGE IS : 313131 lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
```


### Hata Ayıklama
Her iki betik de debug parametresini True olarak ayarlayarak ara adımları yazdırabilirsiniz. Bu, kodun nasıl çalıştığını anlamanıza yardımcı olabilir.
```
debug = True
insert_msg(img_path, msg, debug)

debug = True
secret_message = decode("imgs/encoded.png", debug)
```

### Pseudo Kod
#### Kodlama (Encoding)
- Başlat

- Görüntü dosyasını oku
- Görüntü verilerini ve maksimum bayt sayısını al

- Mesajın uzunluğu maksimum bayt sayısından büyükse
    - Hata mesajı yazdır
    - Çık

- Mesajı ikili gösterime dönüştür
- İkili mesajı 2 bitlik parçalara böl

- Görüntü verilerini değiştir:
    - Her piksel için:
        - En önemsiz 2 biti, bölünmüş ikili mesajın karşılık gelen 2 bitlik parçasıyla değiştir

- Değiştirilmiş görüntü verilerini yeni bir dosyaya kaydet
- "INSERTION COMPLETED" mesajını yazdır

- Bitir



#### Çözme (Decoding)
- Başlat

- Kodlanmış görüntü dosyasını oku
- Görüntü verilerini al

- Görüntü verilerini ikili gösterime dönüştür
- Her pikselin en önemsiz 2 bitini al
- Bu bitleri birleştir

- Birleştirilmiş bitleri ASCII karakterlerine dönüştür
- Gizli mesajı yazdır

- Bitir

Bu pseudo kodlar, projenin ana işlevlerini ve veri akışını özetlemektedir. Gerçek kod, OpenCV ve NumPy kütüphanelerini kullanarak görüntü işleme ve veri manipülasyonu işlemlerini gerçekleştirir.
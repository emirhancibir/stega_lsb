# GÖRÜNTÜ STEGANOGRAFİSİ İLE E-BELGE DOĞRULAMA

## Proje Açıklaması
Bu proje, görüntü steganografisi tekniğini kullanarak elektronik belgelerin (e-belge) doğrulanması için bir uygulama sunar. Uygulama, bir görüntü dosyasına rastgele oluşturulmuş bir doğrulama kodunu gizler ve bu kodu veritabanına kaydeder. Daha sonra, aynı görüntü dosyasından doğrulama kodunu çıkararak, veritabanındaki bilgileri doğrulayabilir. Bu sayede, belgelerin sahihliği ve bütünlüğü kontrol edilebilir.

## LSB Algoritması

![LSB](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgfSk6jWFUDw31Mreg87dmYghgWOytYmrq00kP_j58w0hdUz71hcczpoJeP6Uuw9Rzbpxy1c-jzb7xkRhTOjoMiB5dgrnAi407AhLPxXx7hYR6o3UzkZi-zMk2cWFN7h4jvuY8Z6M92jWs/s1600/encode.png)

LSB algoritması, bir görüntünün her pikselinin en önemsiz bitlerini değiştirerek gizli bir mesajı kodlamak için kullanılır. Bu algoritma, insan gözünün bu küçük değişiklikleri fark edemeyeceği varsayımına dayanır. Mesaj, her pikselin en önemsiz bitlerini değiştirerek kodlanır ve bu sayede görüntü neredeyse değişmeden kalır.

## Kurulum
Bu proje Python 3 ile geliştirilmiş ve test edilmiştir. Projeyi çalıştırmak için Python 3 ve aşağıdaki kütüphanelerin yüklü olması gerekir:

- OpenCV (cv2)
- NumPy (numpy)
- PyQt5 (GUI için)

Bu kütüphaneleri pip3 ile yükleyebilirsiniz:

```
pip3 install opencv-python numpy pyqt5
```


## Kullanım
Bu projeyi kullanmak için öncelikle GitHub'dan repoyu klonlamanız gerekir:

```
git clone https://github.com/emirhancibir/stega_lsb.git
```


Projeyi başlatmak için `e_document_validator/gui.py` dosyasını çalıştırın:

```
python3 e_document_validator/gui.py
```


Açılan GUI penceresinde, aşağıdaki işlevleri gerçekleştirebilirsiniz:

1. **Belge Seçme**: Doğrulanacak belgeyi (görüntü dosyası) seçmek için "Browse Document" düğmesini kullanın.

2. **Doğrulama Kodu Ekleme**: "Embed Random Verification Code" düğmesine tıklayarak, rastgele oluşturulmuş bir doğrulama kodunu belgeye gizleyebilirsiniz.

3. **Doğrulama Kodu Gösterme**: "Show Verification Code" düğmesine tıklayarak, belgedeki gizli doğrulama kodunu görebilirsiniz.

GUI, görüntü seçme, kodlama ve çözme işlemlerini kolayca gerçekleştirmenizi sağlar.

## Proje Yapısı
- `e_document_validator/gui.py`: Ana GUI uygulamasını içerir.
- `e_document_validator/src/encode.py`: Görüntü dosyasına doğrulama kodunu gizleme işlemini gerçekleştirir.
- `e_document_validator/src/decode.py`: Görüntü dosyasından gizli doğrulama kodunu çıkarma işlemini gerçekleştirir.

## Katkıda Bulunma
Bu proje açık kaynaklıdır ve katkıda bulunmak isterseniz, lütfen bir "Pull Request" gönderin. Ayrıca, herhangi bir sorun veya öneriniz varsa, lütfen "Issues" bölümünü kullanın.

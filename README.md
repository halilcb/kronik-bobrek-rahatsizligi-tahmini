# Kronik Böbrek Hastalığı Tahmini Projesi

Bu proje, **kronik böbrek hastalığı** teşhisini kolaylaştırmak amacıyla **Karar Ağacı (Decision Tree)** makine öğrenimi modeli kullanılarak geliştirilmiştir.

## Veri Seti

Bu projede kullanılan veri seti, Hindistan'da 2 ay boyunca toplanmış ve **400 satır ile 25 özellik** içermektedir. Hedef değişken **"class"** olup, **"ckd"** (kronik böbrek hastalığı) veya **"notckd"** (sağlıklı) olmak üzere iki sınıfa ayrılmıştır.

### Özellikler:
- **age**: Hastanın yaşı
- **blood_pressure**: Kan basıncı (mm Hg)
- **specific_gravity**: Spesifik yer çekimi
- **albumin**: Albümin seviyesi
- **sugar**: Şeker seviyesi
- **red_blood_cells**: Kırmızı kan hücreleri
- **pus_cell**: Pus hücresi
- **pus_cell_clumps**: Pus hücre kümeleri
- **bacteria**: Bakteri varlığı
- **blood_glucose_random**: Rastgele kan şekeri seviyesi
- **blood_urea**: Kan üre seviyesi
- **serum_creatinine**: Serum kreatinin seviyesi
- **sodium**: Sodyum seviyesi
- **potassium**: Potasyum seviyesi
- **hemoglobin**: Hemoglobin seviyesi
- **packed_cell_volume**: Hücre hacmi
- **white_blood_cell_count**: Beyaz kan hücresi sayısı
- **red_blood_cell_count**: Kırmızı kan hücresi sayısı
- **hypertension**: Hipertansiyon (Evet/Hayır)
- **diabetes_mellitus**: Diyabet (Evet/Hayır)
- **coronary_artery_disease**: Koroner arter hastalığı (Evet/Hayır)
- **appetite**: İştah durumu
- **peda_edema**: Ödem varlığı
- **aanemia**: Anemi durumu
- **class**: **Hedef değişken (ckd = 0, notckd = 1)**

## Proje Aşamaları

### 1. Veri Keşfi ve Görselleştirme
- Veri seti yüklenmiş, eksik veriler ve değişken türleri incelenmiştir (`df.info()`, `df.describe()`).
- Sayısal sütunlara ilişkin **histogram grafikleri** oluşturularak dağılımlar incelenmiştir.
- **Sınıf dağılımı** (CKD olan ve olmayan hastalar) incelenmiş ve görselleştirilmiştir.
- **KDE (Kernel Density Estimation)** grafikleri ile bazı önemli değişkenlerin dağılımları analiz edilmiştir.

### 2. Eksik Değer Yönetimi
- Eksik veriler incelenmiş (`df.isna().sum()`).
- Sayısal sütunlarda eksik değerler **rastgele örneklemleme** yöntemi ile doldurulmuştur.
- Kategorik değişkenlerde eksik değerler, **mod (en sık tekrar eden değer)** ile doldurulmuştur.

### 3. Veri Ön İşleme ve Kodlama
- Kategorik değişkenler, **LabelEncoder** kullanılarak sayısal formata dönüştürülmüştür.
- Hedef değişken (`class`), **0 (CKD) ve 1 (Sağlıklı)** olacak şekilde kodlanmıştır.

### 4. Karar Ağacı Modeli ile Sınıflandırma
- **Bağımsız değişkenler (X)** ve **bağımlı değişken (y)** ayrılmıştır.
- **%70 eğitim, %30 test** olacak şekilde veri seti bölünmüştür.
- **Karar Ağacı (Decision Tree Classifier)** modeli kullanılarak eğitim gerçekleştirilmiştir.
- **Test verileri üzerinde modelin doğruluğu** hesaplanmıştır.
- **Sınıflandırma raporu ve karmaşıklık matrisi** oluşturulmuştur.

### 5. Model Performansı ve Görselleştirme
- **Karar ağacının görselleştirilmesi** gerçekleştirilmiştir.
- **Özellik önem dereceleri (Feature Importance)** analiz edilmiştir.  

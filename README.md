# Python ile SQLite3 Kullanımı

## 📌 Proje Hakkında

Bu proje, saygıdeğer **Atıl Samancıoğlu'nun** _Veri Bilimi ve Makine Öğrenmesi 2025: 100 Günlük Kamp_ eğitim serisinden esinlenerek geliştirilmiştir.  
Amacı, **Python ile SQLite kullanarak SQL temellerini, veri modellemeyi ve ileri SQL konularını** öğrenmek ve pratik yapmaktır.

Bu proje, özellikle **CRUD işlemleri, JOIN, GROUP BY, AVG gibi SQL fonksiyonları** ve tablo ilişkilerini Python üzerinden uygulamalı olarak göstermektedir.

---

## 📂 Proje Yapısı

```
.
├── db/
├── src/
│   ├── main.py
│   ├── sql_quiz.py
│   └── 01-SQL_Basics.ipynb
├── README.md
├── requirements.txt
└── LICENCE
└── .gitignore

```

---

## 🚀 Kurulum ve Çalıştırma

1. Repo’yu klonlayın:

```bash
git clone https://github.com/UstubecEmre/PythonWithSQLite3.git
cd proje
```

2. Gerekli kütüphaneleri yükleyin (Python 3):

```bash
pip install -r requirements.txt
```

> Not: Bu proje yalnızca `sqlite3` ve `os` gibi standart Python kütüphanelerini kullanır.

3. `main.py` ile **Students & Courses** tablolarını deneyin:

```bash
python main.py
```

4. `sql_quiz.py` ile **Employee – Company – Country** yapısını oluşturun ve CRUD örneklerini çalıştırın:

```bash
python sql_quiz.py
```

---

## 🏗️ Veritabanı Yapısı

### 1️⃣ Students & Courses (`main.py`)

| Tablo    | Açıklama                                     |
| -------- | -------------------------------------------- |
| Students | id, name, surname, age, email, city          |
| Courses  | id, course_name, detail, instructor, credits |

---

### 2️⃣ Employee – Company – Country (`sql_quiz.py`)

| Tablo    | Sütunlar                                                              |
| -------- | --------------------------------------------------------------------- |
| COUNTRY  | ID, Country                                                           |
| COMPANY  | ID, CompanyName, CompanyVision, CountryID 🔑, EstablishedDate         |
| EMPLOYEE | ID, Name, Surname, Email, CompanyID 🔑, Salary, Experience, StartDate |

> 🔑 Foreign Key ilişkileri:
>
> - COMPANY.CountryID → COUNTRY.ID
> - EMPLOYEE.CompanyID → COMPANY.ID

**Ekleme sırası:** COUNTRY → COMPANY → EMPLOYEE  
**Silme sırası:** EMPLOYEE → COMPANY → COUNTRY

---

## 📊 Örnek Kayıtlar

### COUNTRY (İlk 10)

| ID  | Country    |
| --- | ---------- |
| 1   | Turkey     |
| 2   | Azerbaijan |
| 3   | Uzbekistan |
| 4   | Kyrgyzstan |
| 5   | Hungary    |
| 6   | USA        |
| 7   | Germany    |
| 8   | France     |
| 9   | Italy      |
| 10  | Spain      |

### COMPANY (İlk 5)

| ID  | CompanyName   |
| --- | ------------- |
| 1   | ASTOR         |
| 2   | Sabanci Group |
| 3   | Koc Group     |
| 4   | Microsoft     |
| 5   | Nvidia        |

### EMPLOYEE (İlk 5)

| ID  | Name  | Surname  |
| --- | ----- | -------- |
| 1   | Emre  | Ustubec  |
| 2   | Erol  | Ustubec  |
| 3   | Sule  | Ergin    |
| 4   | Fatma | Senol    |
| 5   | Emre  | Dildoker |

---

## 🔧 Örnek Fonksiyonlar

### main.py

- `create_database()` → SQLite veritabanı oluşturur
- `create_tables()` → Students & Courses tablolarını oluşturur
- `insert_sample_data()` → Örnek kayıt ekler
- `basic_sql_operations()` → SELECT, WHERE, ORDER BY, LIMIT örneklerini içerir
- `sql_update_operation()` → Kayıt günceller
- `sql_delete_operation()` → Kayıt siler

### sql_quiz.py

- `insert_samples_to_country/company/employee()` → Örnek veri ekler
- `get_employee(), get_company(), get_country()` → Veri sorgular
- `insert_sample_to_*()` → Yeni kayıt ekler
- `update_country(), update_company(), update_employee()` → Güncelleme işlemlerini gerçekleştiren fonksiyonlardır
- `del_country(), del_company(), del_employee()` → Silme işlemlerini gerçekleştiren fonksiyonlardır
- `join__example()` → JOIN ile çalışan-şirket-ülke ilişkisini getirir
- `get_avg_salary_grouped()` → GROUP BY ile şirkete ve ülkeye göre ortalama maaş sorgular

---

## 👨‍💻 Katkıda Bulunma

Pull request gönderebilir veya issue açabilirsiniz.

---

## 🧪 Gelecekte Testler

Projeye ilerleyen aşamalarda `tests/` klasörü eklenerek **pytest** ve **unittest** tabanlı testler yazılabilir.
Bu sayede tablolar, fonksiyonlar ve CRUD işlemleri otomatik olarak doğrulanabilir.
Bu biraz pytest ve unittest üzerine yoğunlaşabileceğim bir zamanı bulabilir:)

👨‍💻 Geliştirici
Adı: Emre Üstübeç
GitHub: UstubecEmre
E-posta: emresb1999@gmail.com
LinkedIn: Emre Üstübeç

## 📄 Lisans

MIT Lisansı altında paylaşılmıştır.

---

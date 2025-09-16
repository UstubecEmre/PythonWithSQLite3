# import libraries
import sqlite3
import os

# Veri tabanimizi goruntulemek istersek DBeaver aracini kullanabiliriz
# if you want to view students.db, you can install DBeaver

#%% create_database function
def create_database():
    # check database path (yolunu kontrol edelim)
    if os.path.exists("students.db"):
        os.remove("students.db")

    # use connect and create connection 
    conn = sqlite3.connect("students.db") 

    # create cursor
    cursor = conn.cursor() # imlec, baglantiyi kullanarak islemleri gerceklestirir
    return conn, cursor



#%% implement create_tables()
def create_tables(cursor):
    cursor.execute('''
    CREATE TABLE Students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(45) NOT NULL,
        surname VARCHAR(45),
        age INTEGER,
        email VARCHAR(100) UNIQUE,
        city VARCHAR(20)
        
    )    
                   ''')
    
    cursor.execute('''
    CREATE TABLE Courses(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        course_name VARCHAR(50) NOT NULL,
        course_detail TEXT,
        instructor varchar(50),
        instructor_detail VARCHAR(250),
        credits INTEGER
    )               
                   ''')



#%% insert_sample_data
def insert_sample_data(cursor):
    students = [
        # id, name, surname, age, email,city
        ("Emre","Ustubec",26,"emre@gmail.com","Tekirdag"),
        ("Can","Atak",22,"can@gmail.com","Samsun"),
        ("Selin","Sevcan",23,"selin@gmail.com","Ankara"),
        ("Cansu","Akilli",32,"cansu@outlook.com","Istanbul"),
        ("Ilknur","Akilli",28,"ilknur@yahoo.com","Istanbul"),
        ("Ilker","Haylaz",32,"ilker@gmail.com","Mersin"),
        ("Serdar","Kafadar",19,"skafadar@gmail.com","Elazig"),
        ("Fatih","Yorulan",12, "fatihyorulan@gmail.com","Edirne"),
        ("Umut","Pekin",56,"pekinumut@gmail.com","Izmir"),
        ("Yusuf","Tilke",72,"tilke@gmail.com","Eskisehir")
    ]

    #Birden fazla kayit eklemek icin cursor.executemany() 
    cursor.executemany(
        "INSERT INTO Students (name, surname, age, email, city) VALUES (?, ?, ?, ?, ?)", 
        students)
    
    courses = [
        # id, course_name, course_detail, instructor, instructor_detail, credits
        ("DS360","End-to-end data science project is waiting for you","Yasemin Arslan","She is a wonderful instructor",40),
        ("Data Science and Machine Learning","We are here with 100 days of comprehensive content","Atil Samancioglu","Always at the top",65),
        ("AI Integrated With C# .NET","Join us on this journey","Murat Yucedag","He always think of you",20),
        ("C# Fundamentals","If you want to learn C#, you can enroll this course","Murat Yucedag","He always think of you",40),
        ("Zero To Hero Python Course","Master Python by building 100 projects in 100 days. Learn data science, automation, build websites, games and apps!","Angela Yu","She is a developer with a passion for teaching.",100)
    ]
    cursor.executemany(
        "INSERT INTO Courses (course_name, course_detail, instructor, instructor_detail, credits) VALUES (?, ?, ?, ?, ?)",
        courses)
    
    print("Sample data inserted successfully")
    
#%% READ Operation
def basic_sql_operations(cursor):
    
    # 1:) Select all records
    print("*"*10,"SELECT ALL","*"*10)
    cursor.execute("SELECT * FROM Students")
    records = cursor.fetchall() # return a list
    
    # show each data
    for row in records:
        print(row) # row=> return tuple
        # print(f"ID: row[0], Name: {row[1]}, Surname: {row[2]}, Age: {row[3]}, Email:{row[4]}, City: {row[5]} )
    
    # 2:) Select columns
    print("*"*10,"SELECT NAME AND SURNAME COLUMNS","*"*10)
    cursor.execute("SELECT name, surname FROM Students")
    name_surname_list = cursor.fetchall()
    for row in name_surname_list:
        print(f"Name: {row[0]} Surname: {row[1]}")
    
    
    # 3:) Filtered Records
    print("*"*10, "Age Filtered Records","*"*10)
    cursor.execute("SELECT * FROM Students WHERE age <=30")
    filtered_records = cursor.fetchall()
    for row in filtered_records:
        #print(row)
        print(f"ID: {row[0]}, Name: {row[1]}, Surname: {row[2]}, Age: {row[3]}, Email:{row[4]}, City: {row[5]}")
    
    
    
    # 4:) Filter with string
    print("*"*10,"CITY = 'ISTANBUL'","*"*10)
    cursor.execute("SELECT * FROM Students WHERE city = 'Istanbul'")
    filtered_city_records = cursor.fetchall()
    for row in filtered_city_records:
        print(row)
        
        
    # 5:) Order by
    print("*"*10, "ORDER BY age Column","*"*10)
    cursor.execute("SELECT * FROM Students ORDER BY age")
    ordered_records = cursor.fetchall()
    for row in ordered_records:
        print(f"ID: {row[0]}, Name: {row[1]}, Surname: {row[2]}, Age: {row[3]}, Email:{row[4]}, City: {row[5]}")     
        
    # 6:) LIMIT
    print("*"*10, "GET FIRST ROW","*"*10)
    cursor.execute("SELECT * FROM Students LIMIT 1")
    record = cursor.fetchall()
    for row in record:
        print(f"ID: {row[0]}, Name: {row[1]}, Surname: {row[2]}, Age: {row[3]}, Email:{row[4]}, City: {row[5]}") 

#%% CRUD Operations
def sql_delete_operation(conn, cursor, student_id):
    try:
        # convert to integer => student_id
        try:
            student_id = int(student_id)
        except(ValueError, TypeError):
            raise ValueError("Student ID must be an integer or convertible to int")
    
        # Belirtilen sarta uygun ogrenci id var mi? (is there a )
        cursor.execute("SELECT 1 FROM Students WHERE id = ?", (student_id,))
        
        # kayit None donerse, demek ki o id'ye sahip kayit yoktur
        if cursor.fetchone() is None:
            return False
        
        # ilgili id degerine sahip olani sil ve kac satir oldugunu dondur
        cursor.execute("DELETE FROM Students WHERE id = ?", (student_id,))
        
        deleted_record = cursor.rowcount
        
        # islemi gerceklestir
        conn.commit()
        
        return deleted_record > 0
    #sqlite'dan kaynakli hata var mi kontrol edelim
    except sqlite3.Error as err:
        # conn.rollback()
        raise Exception("Ooops. We had a problem (Bir Hata ile Karsilasildi): {err}")


#%% Update operation
def sql_update_operation(conn, cursor, student_id: int, student_name: str = None, student_surname: str = None,student_age: int = None, student_email:str = None, student_city: str = None)-> bool:
    try:
        try:
            student_id = int(student_id)
        except (TypeError, ValueError):
            raise ValueError("Student ID must be an integer or convertible to integer")
            # raise ValueError("Ogrenci ID, Integer veya ona donusturulebilir veri tipinde olmali")
        # check is age numeric?
        if student_age is not None and not isinstance(student_age, int):
            raise ValueError("Student Age must be an integer")
            # raise ValueError("Ogrenci Yasi Tam Sayi Olmali")
        # check is there a record
        
        
        
        
        cursor.execute("SELECT * FROM Students WHERE id = ?", (student_id,))
        record = cursor.fetchone()
        if record is None:
            print(f"Student with id = {student_id} not found")
            # print(f"Ogrenci ID'si = {student_id} bulunamadi"")
            return False #bool donduracegimiz icin False vermesi iyi olur.
        
        # create empty lists
        # parametrelerimiz ve degerlerimiz icin bos liste olusturalim
        fields = []
        values = []
        # check arguments 
        if student_name is not None:
            fields.append("name = ?")
            values.append(student_name)
        
        if student_surname is not None:
            fields.append("surname = ?")
            values.append(student_surname) 
        
        if student_age is not None:
            fields.append("age = ?")
            values.append(student_age)
        
        if student_email is not None:
            fields.append("email = ?")
            values.append(student_email)
            
        if student_city is not None:
            fields.append("city = ?")
            values.append(student_city)
        
        if not fields:
            return False # hicbir deger girilmemis demektir
        
        values.append(student_id)
        
        # sql sorgumuzu yazalim. Burada parametrelerimiz , ile birlestirilecek. name, surname vb. gibi
        update_query = f"UPDATE Students SET {', '.join(fields)} WHERE id = ?"
        cursor.execute(update_query, values)
        updated = cursor.rowcount

        
        # islemi gerceklestir.
        conn.commit()
        
        # etkilenen satir sayisini karsilastiralim
        return updated > 0
         
    except sqlite3.Error as err:
        conn.rollback() # veri tabani guvenligi icin gerekli olabilir
        raise Exception(f"An unexpected error occurred: {err}")
        # raise Exception(f"Beklenmedik Bir Hata Meydana Geldi: {err}"")

#%% 
def main():
    #print("SQL With Python Created...")
    conn, cursor = create_database()
    
    # try-except kullanalim (use try-except-finally for error handling)
    try:
        # ilgili fonksiyonlari cagir (call the functions)        
        create_tables(cursor)
        insert_sample_data(cursor)
        basic_sql_operations(cursor=cursor)
        conn.commit() # imlecin gerceklesitirdigi isleri uygula 
        
    except sqlite3.Error as err:
        print(f"Error (Hata): {err}")
    
    finally:
        conn.close() # baglanti mutlaka kapatilmalidir




if __name__ == "__main__":
    main()
# %%

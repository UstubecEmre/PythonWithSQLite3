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

#%%
def main():
    #print("SQL With Python Created...")
    conn, cursor = create_database()
    
    # try-except kullanalim (use try-except-finally for error handling)
    try:
        # ilgili fonksiyonlari cagir (call the functions)        
        create_tables(cursor)
        insert_sample_data(cursor)
        conn.commit() # imlecin gerceklesitirdigi isleri uygula 
        
    except sqlite3.Error as err:
        print(f"Error (Hata): {err}")
    
    finally:
        conn.close() # baglanti mutlaka kapatilmalidir
    
if __name__ == "__main__":
    main()
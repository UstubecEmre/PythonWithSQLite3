#%% import libraries
import sqlite3
import os 
# from main import create_database, create_tables, insert_sample_data

#%% create a new database

db_path = "employees.db"
def create_database():
    if os.path.exists(db_path):
        print("Database already exists. Connecting ...")
    else:
        print(f"Database Not Found!!!! Create a new {db_path}")
    
    # create a conn and cursor
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    print("Connection successfully")
    return conn, cursor 
        

#%% create tables
def create_table_employee(cursor):
    cursor.execute('''
                   CREATE  TABLE IF NOT EXISTS EMPLOYEE(
                       ID INTEGER PRIMARY KEY AUTOINCREMENT,
                       Name VARCHAR(50) NOT NULL,
                       Surname VARCHAR(50) NOT NULL,
                       Email VARCHAR(100) UNIQUE,
                       CompanyID INTEGER,
                       Salary INT CHECK(Salary >= 0),
                       Experience INT CHECK(Experience >= 0),
                       StartDate TEXT CHECK('1950-01-01'<= StartDate AND StartDate < DATE('now','+1 day')),
                       FOREIGN KEY (CompanyID) REFERENCES COMPANY(ID)
                   )
                   
                   
                   ''')

def create_table_company(cursor):
    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS COMPANY(
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        CompanyName VARCHAR(50) NOT NULL UNIQUE,
                        CompanyVision TEXT NOT NULL,
                        CountryID INTEGER,
                        EstablishedDate TEXT CHECK('1850-01-01'<= EstablishedDate AND EstablishedDate < DATE('now','+1 day')),
                        FOREIGN KEY (CountryID) REFERENCES COUNTRY(ID)
                    )
                   
                   ''')

def create_table_country(cursor):
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS COUNTRY(
                       ID INTEGER PRIMARY KEY AUTOINCREMENT,
                       Country VARCHAR(100) NOT NULL UNIQUE
                   )
                   ''')



def create_tables(cursor):
# bagimliliklara gore siralama onemli
        create_table_country(cursor=cursor)
        create_table_company(cursor)
        create_table_employee(cursor)


#%% ınsert some samples
def insert_samples_to_country(cursor):
    countries = [
        ('Turkey',),
        ('Azerbaijan',),
        ('Uzbekistan',),
        ('Kyrgyzstan',),
        ('Hungary',),
        ('USA',),
        ('Germany',),
        ('France',),
        ('Italy',),
        ('Spain',),
        ('Portugal',),
        ('Poland',),
        ('Greece',),
        ('England',),
        ('Russia',),
        ('China',),
        ('South Korea',),
        ('North Korea',),
        ('Japan',),
        ('Singapore',),
        ('Qatar',),
        ('Saudi Arabia',),
        ('Egypt',),
        ('Norway',),
        ('Sweden',),
        ('Switzerland',),
        ('Argentina',),
        ('Brazil',),
        ('Uruguay',),
        ('Chile',),
        ('Mexico',)
    ]
    cursor.executemany(
        'INSERT OR IGNORE INTO COUNTRY(Country) VALUES (?)',countries,
    )
    
    
def insert_samples_to_company(cursor):
    # CompanyName, CompanyVision, CountryID, EstablishedDate, 
    companies = [
    # Turkiye
    ('ASTOR','To be a global brand representing our country by adopting innovative, continuous development as the most basic principle in the sector with the participation of all stakeholders.',1,'1983-07-29'),
    ('Sabanci Group','We unite Türkiye and the World for a sustainable life with leading enterprises.',1,'1967-04-17'),
    ('Koc Group','Lead.Together',1,'1923-05-31'),
    ('Microsoft','to help people and businesses throughout the world realize their full potential',6, '1975-04-04'),
    ('Nvidia','to solve problems that ordinary computers cannot',6, '1993-04-05'),
    # Azerbaycan
    ('SOCAR','To be a leading integrated energy company in the Caspian region',2,'1992-09-13'),
    ('Azercell','Connecting people across Azerbaijan with innovative telecommunication solutions',2,'1996-12-17'),

    # İngiltere
    ('BP','To provide energy products and services safely and sustainably for people worldwide',14,'1909-04-01'),
    ('Rolls-Royce','To deliver power systems that are reliable, efficient and sustainable',14,'1906-03-15'),

    # Almanya
    ('Siemens','To be the global leader in electrification, automation and digitalization',7,'1847-10-12'),
    ('Volkswagen','To create sustainable mobility for future generations',7,'1937-05-28'),

    # İtalya
    ('Fiat','To make innovative and stylish automobiles accessible to everyone',9,'1899-07-11'),
    ('Ferrari','To deliver the most exclusive and exciting sports cars in the world',9,'1939-09-13')
        
    ]
    cursor.executemany(
        'INSERT OR IGNORE INTO COMPANY(CompanyName, CompanyVision, CountryID, EstablishedDate) VALUES (?, ?, ?, ?)',companies
    )

'''
1 - ASTOR  
2 - Sabanci Group  
3 - Koc Group  
4 - Microsoft  
5 - Nvidia  
6 - SOCAR  
7 - Azercell  
8 - BP  
9 - Rolls-Royce  
10 - Siemens  
11 - Volkswagen  
12 - Fiat  
13 - Ferrari  
'''
def insert_samples_to_employee(cursor):
    # Name, Surname, Email, CompanyID, Salary, Experience, StartDate
    employees = [
        # Türkiye (CompanyID: 1, 2, 3) => ASTOR, Sabanci Group, Koc Group
        ('Emre','Ustubec','emre@gmail.com',1, 35000, 3, '2019-07-19'),
        ('Erol','Ustubec','erol@gmail.com',1, 65000, 6, '2010-10-12'),
        ('Sule','Ergin','sulergin@outlook.com',2, 25500, 0, '2022-11-18'),
        ('Fatma','Senol','fatma@yahoo.com',2, 45000, 2, '2022-02-21'),
        ('Emre','Dildoker','emredildoker@gmail.com',3, 75000, 6, '2019-03-30'),
        ('Cemre','Suberker','csuberker@outlook.com',3, 225000, 15, '2010-03-30'),
        ('Ahmet','Yilmaz','ahmet.yilmaz@gmail.com',1, 42000, 4, '2020-08-11'),
        ('Ayse','Demir','ayse.demir@yahoo.com',2, 38000, 2, '2021-09-15'),
        ('Mehmet','Kaya','mehmet.kaya@outlook.com',3, 56000, 7, '2015-04-25'),

        # USA (CompanyID: 4, 5) => Microsoft, Nvidia
        ('John','Smith','john.smith@microsoft.com',4, 95000, 10, '2012-03-18'),
        ('Zeynep','Canikli','caniklizeynek@yahoo.com',4, 27500, 2, '2023-11-24'),
        ('Zuleyha','Kirmizigul','zuleyhakgul@outlook.com',5, 37500, 3, '2021-06-14'),
        ('Emily','Johnson','emily.johnson@nvidia.com',5, 88000, 8, '2014-07-22'),
        ('Polen','Hacioglu','hacioglupolen@gmail.com',6, 47500, 4, '2020-05-01'),

        # Azerbaycan (CompanyID: 6, 7) => SOCAR, Azercell
        ('Rashad','Aliyev','rashad.aliyev@socar.az',6, 52000, 5, '2018-06-30'),
        ('Leyla','Mammadova','leyla.azercell@gmail.com',7, 41000, 3, '2020-12-05'),

        # İngiltere (CompanyID: 8, 9) => BP, Rolls-Royce
        ('Oliver','Brown','oliver.brown@bp.com',8, 78000, 9, '2013-11-19'),
        ('Sophia','Taylor','sophia.taylor@rollsroyce.co.uk',9, 99000, 12, '2010-01-07'),

        # Almanya (CompanyID: 10, 11) => Siemens - Volkswagen
        ('Hans','Müller','hans.mueller@siemens.de',10, 87000, 11, '2011-09-28'),
        ('Anna','Schmidt','anna.schmidt@vw.com',11, 65000, 6, '2016-05-14'),

        # İtalya (CompanyID: 12, 13) => Fiat, Ferrari
        ('Marco','Rossi','marco.rossi@fiat.it',12, 54000, 5, '2017-08-02'),
        ('Giulia','Bianchi','giulia.bianchi@ferrari.it',13, 125000, 14, '2009-10-11')
        
    ]
    cursor.executemany('''
                   INSERT OR IGNORE INTO EMPLOYEE(Name, Surname, Email, CompanyID, Salary, Experience, StartDate) VALUES(?, ?, ?, ?, ?, ?, ?)
                   
                   ''',employees)
    
#%% create main function
def main():
    """conn, cursor = create_database()
    conn.commit()
    conn.close()"""
    with sqlite3.connect(db_path) as conn:
        
        conn.execute("PRAGMA foreign_keys = ON;")
        cursor = conn.cursor()
        print("Connection successful.") 
        # call the function
        create_tables(cursor)
        
        # insert some samples
        insert_samples_to_country(cursor=cursor)
        insert_samples_to_company(cursor)
        insert_samples_to_employee(cursor)
        
        # save required operations (islemleri kaydet)
        conn.commit()
        print("Tables created successfully:)")     
#%% call the main() func
if __name__ == "__main__":
    """conn, cursor = create_database()
    conn.commit()
    conn.close()"""
    main()
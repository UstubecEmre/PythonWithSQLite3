#%% import libraries
import sqlite3
import os 
# from main import create_database, create_tables, insert_sample_data

#%% create a new database

db_folder = "db"
os.makedirs(db_folder, exist_ok= True) 
db_path = os.path.join(db_folder,"employees.db")

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
                       StartDate TEXT CHECK('1950-01-01'<= StartDate AND StartDate < '2025-09-17'),
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
                        EstablishedDate TEXT CHECK('1850-01-01'<= EstablishedDate AND EstablishedDate < '2025-09-17'),
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
def insert_samples_to_country(conn, cursor):
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
    conn.commit()
    
    country_ids = {}
    for row in cursor.execute('SELECT ID, Country FROM COUNTRY').fetchall():
        country_ids[row[1]] = row[0]
    #country_ids = {row[1]: row[0] for row in cursor.execute('SELECT Country, ID FROM COUNTRY').fetchall()} #fetchall returns a list
    return country_ids
    
def insert_samples_to_company(conn,cursor,country_ids):
    # CompanyName, CompanyVision, CountryID, EstablishedDate, 
    companies = [
    # Turkiye
    # Employee tablosu olusurken hata aldim
    # ('ASTOR','To be a global brand representing our country by adopting innovative, continuous development as the most basic principle in the sector with the participation of all stakeholders.',1,'1983-07-29'),
    # 
    ('ASTOR','To be a global brand representing our country by adopting innovative, continuous development as the most basic principle in the sector with the participation of all stakeholders.',country_ids['Turkey'],'1983-07-29'),
    ('Sabanci Group','We unite Türkiye and the World for a sustainable life with leading enterprises.',country_ids['Turkey'],'1967-04-17'),
    ('Koc Group','Lead.Together',country_ids['Turkey'],'1923-05-31'),
    ('Microsoft','to help people and businesses throughout the world realize their full potential',country_ids['USA'], '1975-04-04'),
    ('Nvidia','to solve problems that ordinary computers cannot',country_ids['USA'], '1993-04-05'),
    # Azerbaycan
    ('SOCAR','To be a leading integrated energy company in the Caspian region',country_ids['Azerbaijan'],'1992-09-13'),
    ('Azercell','Connecting people across Azerbaijan with innovative telecommunication solutions',country_ids['Azerbaijan'],'1996-12-17'),

    # İngiltere
    ('BP','To provide energy products and services safely and sustainably for people worldwide',country_ids['England'],'1909-04-01'),
    ('Rolls-Royce','To deliver power systems that are reliable, efficient and sustainable',country_ids['England'],'1906-03-15'),

    # Almanya
    ('Siemens','To be the global leader in electrification, automation and digitalization',country_ids['Germany'],'1847-10-12'),
    ('Volkswagen','To create sustainable mobility for future generations',country_ids['Germany'],'1937-05-28'),

    # İtalya
    ('Fiat','To make innovative and stylish automobiles accessible to everyone',country_ids['Italy'],'1899-07-11'),
    ('Ferrari','To deliver the most exclusive and exciting sports cars in the world',country_ids['Italy'],'1939-09-13')
        
    ]
    cursor.executemany(
        'INSERT OR IGNORE INTO COMPANY(CompanyName, CompanyVision, CountryID, EstablishedDate) VALUES (?, ?, ?, ?)',companies
    )
    conn.commit()
    print("Inserted Companies:")
    inserted_companies = cursor.execute('SELECT CompanyName FROM COMPANY').fetchall()
    for company in inserted_companies:
        print(company[0])
        
    company_ids = {row[1]: row[0] for row in cursor.execute('SELECT ID, CompanyName FROM COMPANY').fetchall()} # dict
    
    return company_ids
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
def insert_samples_to_employee(conn, cursor,company_ids):
    # Name, Surname, Email, CompanyID, Salary, Experience, StartDate
    employees = [
        # Türkiye (CompanyID: 1, 2, 3) => ASTOR, Sabanci Group, Koc Group
        ('Emre','Ustubec','emre@gmail.com',company_ids['ASTOR'], 35000, 3, '2019-07-19'),
        ('Erol','Ustubec','erol@gmail.com',company_ids['ASTOR'], 65000, 6, '2010-10-12'),
        ('Sule','Ergin','sulergin@outlook.com',company_ids['Sabanci Group'], 25500, 0, '2022-11-18'),
        # ('Fatma','Senol','fatma@yahoo.com',2, 45000, 2, '2022-02-21'),
        ('Fatma','Senol','fatma@yahoo.com',company_ids['Sabanci Group'], 45000, 2, '2022-02-21'),
        
        ('Emre','Dildoker','emredildoker@gmail.com',company_ids['Koc Group'], 75000, 6, '2019-03-30'),
        ('Cemre','Suberker','csuberker@outlook.com',company_ids['Koc Group'], 225000, 15, '2010-03-30'),
        ('Ahmet','Yilmaz','ahmet.yilmaz@gmail.com',company_ids['ASTOR'], 42000, 4, '2020-08-11'),
        ('Ayse','Demir','ayse.demir@yahoo.com',company_ids['Sabanci Group'], 38000, 2, '2021-09-15'),
        ('Mehmet','Kaya','mehmet.kaya@outlook.com',company_ids['Koc Group'], 56000, 7, '2015-04-25'),

        # USA (CompanyID: 4, 5) => Microsoft, Nvidia
        ('John','Smith','john.smith@microsoft.com',company_ids['Microsoft'], 95000, 10, '2012-03-18'),
        ('Zeynep','Canikli','caniklizeynek@yahoo.com',company_ids['Microsoft'], 27500, 2, '2023-11-24'),
        ('Zuleyha','Kirmizigul','zuleyhakgul@outlook.com',company_ids['Nvidia'], 37500, 3, '2021-06-14'),
        ('Emily','Johnson','emily.johnson@nvidia.com',company_ids['Nvidia'], 88000, 8, '2014-07-22'),

        # Azerbaycan (CompanyID: 6, 7) => SOCAR, Azercell
        ('Polen','Hacioglu','hacioglupolen@gmail.com',company_ids['SOCAR'], 47500, 4, '2020-05-01'),
        ('Rashad','Aliyev','rashad.aliyev@socar.az',company_ids['SOCAR'], 52000, 5, '2018-06-30'),
        ('Leyla','Mammadova','leyla.azercell@gmail.com',company_ids['Azercell'], 41000, 3, '2020-12-05'),

        # İngiltere (CompanyID: 8, 9) => BP, Rolls-Royce
        ('Oliver','Brown','oliver.brown@bp.com',company_ids['BP'], 78000, 9, '2013-11-19'),
        ('Sophia','Taylor','sophia.taylor@rollsroyce.co.uk',company_ids['Rolls-Royce'], 99000, 12, '2010-01-07'),

        # Almanya (CompanyID: 10, 11) => Siemens - Volkswagen
        # ('Hans','Muller','hans.mueller@siemens.de',company_ids['Siemens'], 87000, 11, '2011-09-28'), # Hata verdi
        ('Anna','Schmidt','anna.schmidt@vw.com',company_ids['Volkswagen'], 65000, 6, '2016-05-14'),

        # İtalya (CompanyID: 12, 13) => Fiat, Ferrari
        ('Marco','Rossi','marco.rossi@fiat.it',company_ids['Fiat'], 54000, 5, '2017-08-02'),
        ('Giulia','Bianchi','giulia.bianchi@ferrari.it',company_ids['Ferrari'], 125000, 14, '2009-10-11')
        
    ]
    cursor.executemany('''
                   INSERT OR IGNORE INTO EMPLOYEE(Name, Surname, Email, CompanyID, Salary, Experience, StartDate) VALUES(?, ?, ?, ?, ?, ?, ?)
                   ''',employees)
    conn.commit()
    
    
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
        print("Tables created successfully:)")   
        # insert some samples
        
        country_ids = insert_samples_to_country(conn,cursor=cursor)
        company_ids = insert_samples_to_company(conn,cursor,country_ids)
                
        insert_samples_to_employee(conn,cursor,company_ids)
        print("All Data Inserted Successfully:)")
        # save required operations (islemleri kaydet)
        conn.commit()
          

#%% call the main() func
if __name__ == "__main__":
    """conn, cursor = create_database()
    conn.commit()
    conn.close()"""
    main()
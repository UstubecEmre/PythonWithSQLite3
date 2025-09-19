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
    



# Question 1: Şirketi Microsoft olan kayitlari getiren sorguyu yaziniz.
def get_company(cursor, company_name: str):
    try:
        cursor.execute('''
                    SELECT * FROM COMPANY WHERE CompanyName = '?' 
                    ''',(company_name,))
        records = cursor.fetchall()
        #ID, CompanyName, CompanyVision, CountryID, EstablishedDate, 
        if not records:
            return False
        
        for record in records:
            print(f"Emplyee's ID: {record[0]}, Company's Name: {record[1]},Company's Vision: {record[2]}, Country ID: {record[3]}, Established Date: {record[4]}")
        return True
    except sqlite3.Error as err:
        print(f"Database Error Occured: {err}")
        return False

def get_country(cursor, country_id: int):
    try:
        try:
             country_id = int(country_id)
        except (TypeError, ValueError):
                raise ValueError('Country ID must be an integer or convertible to integer')
        
        cursor.execute('SELECT * FROM COUNTRY WHERE ID = ?',(country_id,))
        
        record = cursor.fetchone() # return a tuple
        
        if not record:
            print("Not Found")
            return False
        print(f"Country ID: {record[0]}, Country Name: {record[1]}")
        return True
    except sqlite3.Error as err:
        return Exception(f"An unexpected error occured: {err}")

    
def get_employee(cursor, employee_id):
    try:
        try:
            employee_id = int(employee_id)
        except(TypeError, ValueError):
            raise ValueError('Employee ID must be an integer or conversible to integer')
            #if employee_id is None or isinstance(employee_id, int):
                #return False   
        cursor.execute('SELECT * FROM EMPLOYEE WHERE ID = ?', (employee_id,))
        record = cursor.fetchone() # return a tuple
        if record is None:
            print("Record Not Found")
            return False 
        '''
        Employee Data: if you want to define a dict, you can do it 
          employee_data = {
            "ID": record[0],
            "Name": record[1],
            "Surname": record[2],
            "Email": record[3],
            "CompanyID": record[4],
            "Salary": record[5],
            "Experience": record[6],
            "StartDate": record[7],
        }
        '''
        
        # Name, Surname, Email, CompanyID, Salary, Experience, StartDate
        print(f"Employee ID: {record[0]}, Employee's Name: {record[1]}, Employee's Surname: {record[2]},Employee's Email: {record[3]}, Company ID: {record[4]}, Salary: {record[5]}, Experience{record[6]}, Start Date: {record[7]} ")
            
    
    except sqlite3.Error as err:
        # conn.rollback() # veri tabani guvenligi icin gerekli olabilir
        raise Exception(f"An unexpected error occurred: {err}")
    

# insert into
#%% insert some records to country
def insert_sample_to_country(conn,cursor, country_name: str = None):
    try:
        # is there any record (daha onceden o isimde var mi)
        cursor.execute('SELECT * FROM COUNTRY WHERE Country = ?',(country_name,))
        record = cursor.fetchone()
        if record is not None:
            print(f"This Country {record[1]} Already exists")
            return False
        
        
        cursor.execute('INSERT INTO COUNTRY(Country) VALUES (?)', (country_name,))
        # save and apply
        conn.commit()
        
        
        inserted_id = cursor.lastrowid
        print(f"Country Inserted... CountryID: {inserted_id} - Country Name: {country_name}")
        
        #effected_row = cursor.rowcount
        
        return cursor.rowcount > 0
                    
    except sqlite3.Error as err:
        print(f"An unexpected Error Occured: {err}")        

#%% insert some records to company 
#ID, CompanyName, CompanyVision, CountryID, EstablishedDate, 
def insert_sample_to_company(conn, cursor, company_name: str = None, company_vision:str = None, country_id: int = None, established_date: str = None) ->bool:
    try:
        try:
            country_id = int(country_id)
        except (ValueError, TypeError):
            raise ValueError("country_id must be an integer or conversible to integer")
            
        if company_name is None  or not isinstance(company_name, str) or len(company_name) <0:
            print("company_name column must be a non-empty string")
            return False
        
        if company_vision is None or not isinstance(company_vision,str) or len(company_vision) < 3 :
            print("company_vision column must be a string format with length at least 3 characters")
            return False
        
        if established_date is None or not isinstance(established_date, str) or len(established_date) < 8: 
            print("established_date must be a valid string (e.g., '2020-01-01')")
            return False
        
        
        # check duplicates
        cursor.execute('SELECT ID FROM COMPANY WHERE CompanyName = ?', (company_name,))
        if cursor.fetchone(): #return a tuple
            print(f"{company_name} Company Already Exists")
            return False
        
        cursor.execute('SELECT ID FROM COUNTRY WHERE ID = ?', (country_id,))
        if cursor.fetchone():
            print(f"CountryID: {country_id} already exists")
            return False
        
        cursor.execute('''
                       INSERT INTO COMPANY(CompanyName, CompanyVision, CountryID, EstablishedDate)
                       VALUES (?, ?, ?, ?)
                       
                       ''', (company_name.strip(), company_vision.strip(), country_id, established_date.strip()))
        # save changes and apply 
        conn.commit()   
        print(f"Company inserted successfully: {company_name}")
        return True
        
    except sqlite3.Error as err:
        raise Exception(f"An unexpected error occured: {err}")


#%% insert records to employee
# Name, Surname, Email, CompanyID, Salary, Experience, StartDate
import re 
def insert_sample_to_employee(conn,cursor, employee_id:int =None,employee_name: str = None, employee_surname : str = None, employee_email: str = None, company_id:int = None, salary:int = None, experience: int = None, start_date:str = None):
    try:
        
        try:
            employee_id = int(employee_id)
        except (TypeError, ValueError):
            raise ValueError('Employee ID must be an integer or convertible to integer')
        
        try:
            company_id = int(company_id)
        except (TypeError, ValueError):
            raise ValueError("Company ID must be an integer or convertible to integer")
        
        try:
            salary = int(salary)
            if salary < 0:
                print("Salary must be greater than zero")
        except (TypeError, ValueError):
            raise ValueError("Salary must be an integer or convertible to integer")
        
        
        if experience is None or not isinstance(experience, int) or experience <0:
            print("Experience must be a non-negative integer")
        
    
        if employee_name is None or not isinstance(employee_name, str) or len(employee_name) < 3:
            print(f"Employee name must be string format with length at least 3 characters")
            return False
            
        
        if employee_surname is None or not isinstance(employee_surname, str) or len(employee_surname) < 3:
            print(f"Employee surname must be string format with length at least 3 characters")
            return False
        
        
        email_regex = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
        if employee_email is None  or not email_regex.match(employee_email.strip()):
            print("Invalid email format")
            return False
        # return bool(email_regex.match(employee_email))
        
        
        # check already exists => Employee zaten var mi?
        cursor.execute('SELECT ID FROM EMPLOYEE WHERE ID= ?', (employee_id,))
        if cursor.fetchone():
            print(f"{employee_id} already exists. Please, use update function")
            return False


        # check company id
        cursor.execute('SELECT ID FROM COMPANY WHERE ID = ?', (company_id,))
        if cursor.fetchone() is None:
            print(f"Company with ID {company_id} does not exist")
            return False

        cursor.execute(
            ''' INSERT INTO EMPLOYEE(Name, Surname, Email, CompanyID, Salary, Experience, StartDate)
            VALUES(?, ?, ?, ?, ?, ?, ?)
            ''',(employee_name.strip(), employee_surname.strip(), employee_email.strip(), company_id, salary, experience, start_date.strip())
        )
        
        # save changes and apply 
        conn.commit()   
        print(f"Employee inserted successfully: {employee_id} {employee_name} {employee_surname}")
        return True
    
    except sqlite3.Error as err:
        raise Exception(f"An unexpected error occured: {err}")
    



#%% update records
def update_country(conn, cursor, country_id: int = None, new_country_name : str = None):
    try:
        try:
            country_id = int(country_id)
        except (ValueError, TypeError) as err:
            raise ValueError("Country ID must be an integer or convertible to integer")
    
        if new_country_name is None or not isinstance(new_country_name, str) or len(new_country_name.strip()) < 3:
            print("New country_name must be string with at least 3 characters")
            return False
            
        cursor.execute('SELECT ID FROM COUNTRY WHERE ID = ?', (country_id,))
        if cursor.fetchone() is None:
            print(f"{country_id} with ID {country_id} does not exist")
            return False 
        
        cursor.execute('''
                       UPDATE COUNTRY SET Name = ? WHERE ID = ?
                       ''', (new_country_name.strip(), country_id,))
        conn.commit()   
        
        # control effected row
        if cursor.rowcount > 0:
            print(f"Country updated successfully: {country_id} - {new_country_name}")
            return True
        else:
            print(f"No update performed for ID {country_id}")
            return False
           
    except sqlite3.Error as err:
        raise Exception(f"An unexpected error occured: {err}")


# ID, CompanyName, CompanyVision, CountryID, EstablishedDate, 
def update_company(conn, cursor, company_id:int = None, company_name : str = None, company_vision: str = None, country_id : int = None, established_date : str = None):
    try:
        try:
            company_id = int(company_id)
        except (ValueError, TypeError):
            raise ValueError("company_id must be an integer or convertible to integer")
        
        try:
            country_id = int(country_id)
        
        except (ValueError, TypeError):
            raise ValueError("country_id must be an integer or convertible to integer")

        if company_name is None or not isinstance(company_name, str) or len(company_name.strip()) < 1:
            print("company_name must be string with at least one character")
            return False
        
        if company_vision is None or not isinstance(company_vision, str) or len(company_vision.strip()) < 3:
            print("company_vision must be string with at least three characters")
            return False
        
        if established_date is None or not isinstance(established_date, str) or not 8 < len(established_date.strip()) < 11:
            print("established_date must be a valid string (e.g., '2020-01-01')")
            return False
        
        cursor.execute('SELECT ID FROM COMPANY WHERE ID = ?',(company_id,)) 
        if cursor.fetchone() is None:
            print(f"ID with {company_id} does not exists")
            return False   
        
        cursor.execute('SELECT ID FROM COUNTRY WHERE ID = ?',(country_id,))
        if cursor.fetchone() is None:
            print(f"ID with {country_id} does not exists")
            return False
        
        fields = []
        values = []
        
        if company_name:
            fields.append('Name = ?')
            values.append(company_name.strip())
        
        if company_vision:
            fields.append('CompanyVision = ?')
            values.append(company_vision.strip())
        
        if country_id is not None:
            fields.append('CountryID = ?')
            values.append(country_id)
        
        if established_date:
            fields.append('EstablishedDate = ?')
            values.append(established_date.strip())
        
        values.append(company_id)
        
        sql_query = f"UPDATE COMPANY SET {', '.join(fields)} WHERE ID = ?"
        cursor.execute(sql_query, tuple(values))
        
        #save changes and apply
        conn.commit()
        
        # check count of effected_rows
        
        if cursor.rowcount > 0:
            print(f"Company updated successfully: {company_id}")
            return True
        
        print(f"No update performed for ID {company_id}")
        return False 
            
        
    except sqlite3.Error as err:
        raise Exception(f"An unexpected error occured: {err}")


# Name, Surname, Email, CompanyID, Salary, Experience, StartDate

def update_employee(conn, 
                    cursor, 
                    employee_id: int = None,
                    employee_name:str = None,
                    employee_surname: str = None,
                    employee_email:str = None,
                    company_id:int = None,
                    salary:int = None,
                    experience:int = None,
                    start_date: str = None
                    ):
    try:
        try:
            employee_id = int(employee_id)
        except (TypeError, ValueError):
            raise ValueError("employee_id must be an integer or convertible to integer")
        
        if company_id is not None:
            try:
                company_id = int(company_id)
                if company_id < 1:
                    print("Company ID must be greater than 1")
                    return False
            except (TypeError, ValueError):
                raise ValueError("Company ID must be an integer or convertible to integer")
        
        if salary is not None:
            try:
                salary = int(salary)
                if salary < 0:
                    print("Salary must be greater than 0")
            except (TypeError, ValueError):
                raise ValueError("Salary must be an integer or convertible to integer")
        
        if experience is not None:
            try:
                experience = int(experience)
                if experience < 0:
                    print("Experience must be greater than 0")
                    return False
            except(ValueError, TypeError):
                raise ValueError("Experince must be an integer or convertible to integer")
    

        if employee_name is None or not isinstance(employee_name, str) or len(employee_name.strip()) < 3:
            print("Employee name must be string format with length at least 3 characters")
            
            return False
        
        if employee_surname is None or not isinstance(employee_surname, str) or len(employee_surname.strip()) < 3:
            print(f"Employee surname must be string format with length at least 3 characters")
            return False
        
        email_pattern = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
        if employee_email is None or not isinstance(employee_email, str) or not email_pattern.match(employee_email.strip()):
            print("Invalid email format")
            return False
        
        if start_date is None or not isinstance(start_date, str):
            print("Start Date must be an string")
            return False
    
    
        cursor.execute('SELECT ID FROM EMPLOYEE WHERE ID = ?', (employee_id,))
        if cursor.fetchone() is None:
            print(f"ID with {employee_id} does not exists")
            return False
        # Name, Surname, Email, CompanyID, Salary, Experience, StartDate
        
        fields = []
        values = []
        
        if employee_name:
            fields.append('Name = ?')
            values.append(employee_name.strip())
            
        if employee_surname:
            fields.append('Surname = ?')
            values.append(employee_surname.strip())

        if employee_email:
            fields.append('Email = ?')
            values.append(employee_email.strip())
            
        if company_id:
            fields.append('CompanyID = ?')
            values.append(company_id)
        
        if salary:
            fields.append('Salary = ?')
            values.append(salary)
            
        if experience:
            fields.append('Experience = ?')
            values.append(experience)
        
        if start_date:
            fields.append('StartDate = ?')
            values.append(start_date.strip())
            
        if not fields:
            print("No fields provided to update")
            return False

        values.append(employee_id)
        sql_query = f"UPDATE EMPLOYEE SET {', '.join(fields)} WHERE ID = ?"
        
        cursor.execute(sql_query, tuple(values))
        
        #save changes and apply
        conn.commit()
        
        # check count of effected_rows
        
        if cursor.rowcount > 0:
            print(f"Employee updated successfully: {employee_id}")
            return True
        
        print(f"No update performed for ID {employee_id}")
        return False 
    except sqlite3.Error as err:
        raise Exception(f"An unexpected error occured: {err}")
    



#%% delete records





#%% select_five_rows




#%% order by 





#&& Group by and having => AGG Functions

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
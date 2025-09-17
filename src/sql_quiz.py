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
                        CompanyName VARCHAR(50) NOT NULL,
                        CompanyMission TEXT NOT NULL,
                        CountryID INTEGER,
                        EstablishedDate TEXT CHECK('1850-01-01'<= EstablishedDate AND EstablishedDate < DATE('now','+1 day')),
                        FOREIGN KEY (CountryID) REFERENCES COUNTRY(ID)
                    )
                   
                   ''')

def create_table_country(cursor):
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS COUNTRY(
                       ID INTEGER PRIMARY KEY AUTOINCREMENT,
                       Country VARCHAR(100)
                   )
                   ''')

def main():
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
                        CompanyName VARCHAR(50) NOT NULL,
                        CompanyMission TEXT NOT NULL,
                        CountryID INTEGER,
                        EstablishedDate TEXT CHECK('1850-01-01'<= EstablishedDate AND EstablishedDate < DATE('now','+1 day')),
                        FOREIGN KEY (CountryID) REFERENCES COUNTRY(ID)
                    )
                   
                   ''')

def create_table_country(cursor):
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS COUNTRY(
                       ID INTEGER PRIMARY KEY AUTOINCREMENT,
                       Country VARCHAR(100)
                   )
                   ''')


def create_tables(cursor):
# bagimliliklara gore siralama onemli
        create_table_country(cursor=cursor)
        create_table_company(cursor)
        create_table_employee(cursor)
        
#%% 
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
        # islemleri kaydet
        conn.commit()
        print("Tables created successfully:)")     
#%% 
if __name__ == "__main__":
    """conn, cursor = create_database()
    conn.commit()
    conn.close()"""
    main()
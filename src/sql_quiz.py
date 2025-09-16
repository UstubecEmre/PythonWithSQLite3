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
        


#%% 
if __name__ == "__main__":
    """conn, cursor = create_database()
    conn.commit()
    conn.close()"""
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        print("Connection successful.") 

        # islemleri kaydet
        conn.commit()
             
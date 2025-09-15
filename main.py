# import libraries
import sqlite3
import os



def create_database():
    # check database path (yolunu kontrol edelim)
    if os.path.exists("students.db"):
        os.remove("students.db")

    # use connect and create connection 
    conn = sqlite3.connect("students.db") 

    # create cursor
    cursor = conn.cursor() # imlec, baglantiyi kullanarak islemleri gerceklestirir
    return conn, cursor
    
def main():
    #print("SQL With Python Created...")
    conn, cursor = create_database()
    
if __name__ == "__main__":
    main()
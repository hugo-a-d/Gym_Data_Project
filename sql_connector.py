import sqlite3
from pathlib import Path

def sql_connection(db_path:str):
    db_file = Path(db_path)
    #if not db_file.exists():
    #    print(f"Database file not found: {db_path}")
    #    return False
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        cursor.execute("SELECT sqlite_version();")
        version = cursor.fetchone()[0]
        
        conn.close()
        return True
    
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
        return False
        
if __name__ == "__main__":
    sql_connection("sql_db/gym_data.db")
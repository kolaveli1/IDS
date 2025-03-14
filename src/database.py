import sqlite3


DB_NAME = "ids_logs.db"

def setup_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS attack_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            attack_type TEXT,
            source_ip TEXT,
            details TEXT
        )
    ''')
    conn.commit()
    conn.close()

def log_attack(attack_type, source_ip, details):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO attack_logs (attack_type, source_ip, details) VALUES (?, ?, ?)", 
                   (attack_type, source_ip, details))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_database()
    print("Database oprettet")

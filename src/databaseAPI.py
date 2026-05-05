import mysql.connector 
from config import DB_CONFIG

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

def get_all_members():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True) 
    cursor.execute("SELECT * FROM Members")
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results

def get_member_by_id(member_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Members WHERE MemberID = %s", (member_id))
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results

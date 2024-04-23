from dotenv import load_dotenv
import os
import mysql.connector as mysql

load_dotenv()
host_ = os.getenv('host')
user_ = os.getenv('user')
password_ = os.getenv('passwd')
database_ = os.getenv('database')

def execute_query(query, params, is_insert=False):
    db = mysql.connect(
            host=host_,
            user=user_,
            passwd=password_,
            database=database_
        )
    cursor = db.cursor()
    cursor.execute(query, params)
    
    if is_insert:
        db.commit()
        results = None
    else:
        results = cursor.fetchall()
    
    cursor.close()
    db.close()
    
    return results

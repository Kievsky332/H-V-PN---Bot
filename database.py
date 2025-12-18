import sqlite3;
 
con = sqlite3.connect("users.db")
cursor = con.cursor()
 
# создаем таблицу people
'''
cursor.execute("""CREATE TABLE people
                (id INTEGER ,  
                subscribe TEXT)
            """)
'''
def add_to_free(id):
    cursor.execute(f"""INSERT INTO `people` (`id`,`subscribe`)
    VALUES('{id}','yes'')""")

con.commit() 
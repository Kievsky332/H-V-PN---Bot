import sqlite3
import secret

con = sqlite3.connect(f"{secret.put}//user.db",check_same_thread=False)
cur = con.cursor()

#создание
#cur.execute("CREATE TABLE vpn(id int NOT NULL ,subscribe int NOT NULL)")

#Очистка
#cur.execute("DELETE FROM 'vpn'")
def have(id):
    res = cur.execute(f"SELECT COUNT(*) FROM `vpn` WHERE `id` ='{id}';")
    a = res.fetchone()
    return a[0]
def add_to_free(id, code):
    cur.execute(f"INSERT INTO `vpn` (`id`,`subscribe`)VALUES('{id}','{code}')")
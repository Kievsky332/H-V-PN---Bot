import sqlite3
import secret
import datetime 

con = sqlite3.connect(f"{secret.put}//user.db",check_same_thread=False)
cur = con.cursor()

#создание
cur.execute("CREATE TABLE IF NOT EXISTS vpn(id int NOT NULL ,subscribe int NOT NULL)")
cur.execute("CREATE TABLE IF NOT EXISTS otz(id INTEGER  PRIMARY KEY AUTOINCREMENT,date text NOT NULL ,id_user int NOT NULL , text TEXT NOT NULL)")

#Очистка
#cur.execute("DELETE FROM 'vpn'")
#cur.execute("DELETE FROM 'otz'")


def have(id):
    res = cur.execute(f"SELECT COUNT(*) FROM `vpn` WHERE `id` ='{id}'")
    a = res.fetchone()
    return a[0]

def add_to_free(id, code):
    cur.execute(f"INSERT INTO `vpn` (`id`,`subscribe`)VALUES('{id}','{code}')")
    con.commit()
def last_otz():
    res = cur.execute("SELECT text FROM `otz` WHERE `id` = (SELECT MAX(`id`) FROM `otz`)")
    a = res.fetchone()
    return a[0]
def usersendtext(id):
    res = cur.execute(f"SELECT COUNT(*) FROM `otz` WHERE `id_user` ='{id}'")
    a = res.fetchone()
    return id+": "+a[0]
def add_message(id,text):
    date = datetime.datetime.now() .strftime("%d.%m.%Y %H:%M:%S ")
    cur.execute(f"INSERT INTO `otz` (`date`,`id_user`,`text`)VALUES('{date}','{id}','{text}')")
    con.commit()
con.commit()
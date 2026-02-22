import sqlite3
import secret
import datetime 

con = sqlite3.connect(f"{secret.put}//user.db",check_same_thread=False)#Вместо secret.put замените на путь до вашей бд
cur = con.cursor()

#создание
cur.execute("CREATE TABLE IF NOT EXISTS vpn(id int NOT NULL ,subscribe int NOT NULL)") #Создание таблицы подписчиков
cur.execute("CREATE TABLE IF NOT EXISTS otz(id INTEGER  PRIMARY KEY AUTOINCREMENT,date text NOT NULL ,id_user int NOT NULL , text TEXT NOT NULL)")#Создание таблицы  отзывов

#Очистка
#cur.execute("DELETE FROM 'vpn'")
#cur.execute("DELETE FROM 'otz'")


def have(id):
    res = cur.execute(f"SELECT COUNT(*) FROM `vpn` WHERE `id` ='{id}'")
    a = res.fetchone()
    return a[0] #Проверяем что чел уже получал или нет

def add_to_free(id, code):
    cur.execute(f"INSERT INTO `vpn` (`id`,`subscribe`)VALUES('{id}','{code}')")
    con.commit() # Вставляем код
def last_otz(): #Получаем последний отзыв
    res = cur.execute("SELECT text FROM `otz` WHERE `id` = (SELECT MAX(`id`) FROM `otz`)")
    a = res.fetchone()
    try :
        return a[0]
    except:
        return None
def usersendtext(id):
    res = cur.execute(f"SELECT COUNT(*) FROM `otz` WHERE `id_user` ='{id}'")
    a = res.fetchone()
    return a[0] #Проверяем что пользователь не писал отзыв
def add_message(id,text):
    date = datetime.datetime.now() .strftime("%d.%m.%Y %H:%M:%S ")
    cur.execute(f"INSERT INTO `otz` (`date`,`id_user`,`text`)VALUES('{date}','{id}','{text}')")
    con.commit() #Отправляем  в бд отзыв
con.commit() #Комитим на всякий случай
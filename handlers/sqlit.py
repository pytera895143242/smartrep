import sqlite3

def reg_user(id):
    db = sqlite3.connect('server.db')
    sql = db.cursor()

    sql.execute(""" CREATE TABLE IF NOT EXISTS user_time (
        id BIGINT,
        status_ref
        ) """)
    db.commit()

    sql.execute(f"SELECT id FROM user_time WHERE id ='{id}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO user_time VALUES (?,?)", (str(id), '1'))
        db.commit()
        ret = 1
    else:
        ret = 0


    sql.execute(""" CREATE TABLE IF NOT EXISTS trafik (
            chanel,
            parametr,
            chat_channel
            ) """)

    db.commit()
    sql.execute(f"SELECT chanel FROM trafik WHERE chanel = 'channel1'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO trafik VALUES (?,?,?)", ('channel1', 'channel',-111)) #Ссылка на модель
        sql.execute(f"INSERT INTO trafik VALUES (?,?,?)", ('channel2', 'channel',-111)) #Ссылка на видосник
        sql.execute(f"INSERT INTO trafik VALUES (?,?,?)", ('channel3', 'channel',-111)) #Ссылка на приватку
        sql.execute(f"INSERT INTO trafik VALUES (?,?,?)", ('channel4', 'channel', -111)) #Ссылка на первый канал
        sql.execute(f"INSERT INTO trafik VALUES (?,?,?)", ('channel5', 'channel', 0)) #Ссылка на второй канал
        sql.execute(f"INSERT INTO trafik VALUES (?,?,?)", ('channel6', 'channel',0)) #Ссылка на третий канал
        sql.execute(f"INSERT INTO trafik VALUES (?,?,?)", ('channel7', 'channel', 0)) #Ссылка на четвертый канал
        sql.execute(f"INSERT INTO trafik VALUES (?,?,?)", ('channel8', 'channel', 0)) #Ссылка на пятый канал
        db.commit()
    return ret

def info_members():
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    all = sql.execute(f'SELECT COUNT(*) FROM user_time').fetchone()[0]
    finish = sql.execute(f"SELECT COUNT(*) FROM user_time WHERE status_ref = '0'").fetchone()[0]
    process = sql.execute(f"SELECT COUNT(*) FROM user_time WHERE status_ref = '1'").fetchone()[0]
    return all,finish,process

def delite_user(id):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute(f'DELETE FROM user_time WHERE id = "{id}"')
    db.commit()


def cheak_chat_id():
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    i1 = sql.execute(f"SELECT chat_channel FROM trafik WHERE chanel = 'channel1'").fetchone()[0]
    i2 = sql.execute(f"SELECT chat_channel FROM trafik WHERE chanel = 'channel2'").fetchone()[0]
    i3 = sql.execute(f"SELECT chat_channel FROM trafik WHERE chanel = 'channel3'").fetchone()[0]
    i4 = sql.execute(f"SELECT chat_channel FROM trafik WHERE chanel = 'channel4'").fetchone()[0]
    i5 = sql.execute(f"SELECT chat_channel FROM trafik WHERE chanel = 'channel5'").fetchone()[0]
    i6 = sql.execute(f"SELECT chat_channel FROM trafik WHERE chanel = 'channel6'").fetchone()[0]
    i7 = sql.execute(f"SELECT chat_channel FROM trafik WHERE chanel = 'channel7'").fetchone()[0]
    i8 = sql.execute(f"SELECT chat_channel FROM trafik WHERE chanel = 'channel8'").fetchone()[0]
    return i1,i2,i3,i4,i5,i6,i7,i8


def cheak_traf():
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    c1 = sql.execute(f"SELECT parametr FROM trafik WHERE chanel = 'channel1'").fetchone()[0]
    c2 = sql.execute(f"SELECT parametr FROM trafik WHERE chanel = 'channel2'").fetchone()[0]
    c3 = sql.execute(f"SELECT parametr FROM trafik WHERE chanel = 'channel3'").fetchone()[0]
    c4 = sql.execute(f"SELECT parametr FROM trafik WHERE chanel = 'channel4'").fetchone()[0]
    c5 = sql.execute(f"SELECT parametr FROM trafik WHERE chanel = 'channel5'").fetchone()[0]
    c6 = sql.execute(f"SELECT parametr FROM trafik WHERE chanel = 'channel6'").fetchone()[0]
    c7 = sql.execute(f"SELECT parametr FROM trafik WHERE chanel = 'channel7'").fetchone()[0]
    c8 = sql.execute(f"SELECT parametr FROM trafik WHERE chanel = 'channel8'").fetchone()[0]
    list = [c1,c2,c3,c4,c5,c6,c7,c8]
    return list


def obnova_status_all(): #Функция вызывается при перезапуске бота и ставит всем юзерам status = 0
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute(f"UPDATE user_time SET status_ref = '0'")
    db.commit()

def obnova_status(id): #Функция вызывается при перезапуске бота и ставит всем юзерам status = 0
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute(f"UPDATE user_time SET status_ref = '0' WHERE id = '{id}'")
    db.commit()


def obnovatrafika1(link_one,id_channel1):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute(f"UPDATE trafik SET parametr= '{link_one}' WHERE chanel = 'channel1'")
    sql.execute(f"UPDATE trafik SET chat_channel= '{id_channel1}' WHERE chanel = 'channel1'")
    db.commit()

def obnovatrafika2(link_one,id_channel1):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute(f"UPDATE trafik SET parametr= '{link_one}' WHERE chanel = 'channel2'")
    sql.execute(f"UPDATE trafik SET chat_channel= '{id_channel1}' WHERE chanel = 'channel2'")
    db.commit()


def obnovatrafika3(link_one,id_channel1):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute(f"UPDATE trafik SET parametr= '{link_one}' WHERE chanel = 'channel3'")
    sql.execute(f"UPDATE trafik SET chat_channel= '{id_channel1}' WHERE chanel = 'channel3'")
    db.commit()

def obnovatrafika4(link_one,id_channel1):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute(f"UPDATE trafik SET parametr= '{link_one}' WHERE chanel = 'channel4'")
    sql.execute(f"UPDATE trafik SET chat_channel= '{id_channel1}' WHERE chanel = 'channel4'")
    db.commit()

def obnovatrafika5(link_one,id_channel1):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute(f"UPDATE trafik SET parametr= '{link_one}' WHERE chanel = 'channel5'")
    sql.execute(f"UPDATE trafik SET chat_channel= '{id_channel1}' WHERE chanel = 'channel5'")
    db.commit()

def obnovatrafika6(link_one,id_channel1):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute(f"UPDATE trafik SET parametr= '{link_one}' WHERE chanel = 'channel6'")
    sql.execute(f"UPDATE trafik SET chat_channel= '{id_channel1}' WHERE chanel = 'channel6'")
    db.commit()

def obnovatrafika7(link_one,id_channel1):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute(f"UPDATE trafik SET parametr= '{link_one}' WHERE chanel = 'channel7'")
    sql.execute(f"UPDATE trafik SET chat_channel= '{id_channel1}' WHERE chanel = 'channel7'")
    db.commit()

def obnovatrafika8(link_one,id_channel1):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute(f"UPDATE trafik SET parametr= '{link_one}' WHERE chanel = 'channel8'")
    sql.execute(f"UPDATE trafik SET chat_channel= '{id_channel1}' WHERE chanel = 'channel8'")
    db.commit()
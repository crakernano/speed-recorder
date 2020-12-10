import sqlite3
from sqlite3 import Error

def sql_connection():
    try:
        con = sqlite3.connect('speeds_record.db')
        return con

    except Error:
        print(Error)




def sql_table(con):

    cursor = con.cursor()
    cursor.execute("create table if not exists speed_record(id integer PRIMARY KEY,\
                                                            download float,\
                                                            upload float,\
                                                            ping float,\
                                                            lat float,\
                                                            lon float,\
                                                            city text,\
                                                            country text,\
                                                            latency float,\
                                                            ip text,\
                                                            isp text,\
                                                            created_at date)")
    con.commit()

def sql_insert(con, data):

    cursor = con.cursor()
    cursor.execute('INSERT INTO speed_record(download,\
                                            upload,\
                                            ping,\
                                            lat,\
                                            lon,\
                                            city,\
                                            country,\
                                            latency,\
                                            ip,\
                                            isp,\
                                            created_at) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', data)
    con.commit()

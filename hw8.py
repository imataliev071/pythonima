import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error:
        print('Ошибка на create_conn')

    return conn


def reed(conn):
    try:
        sql = '''SELECT * FROM студент'''
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        for i in rows:
            print(i)
    except Error:
        print('ошибка reed')


def surn(conn):
    try:
        sql = '''SELECT * FROM студент WHERE length(фамилия) > 10 '''
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        for i in rows:
            print(i)
        conn.commit()
    except Error:
        print('ошибка surn')


def genius(conn):
    try:
        sql = '''UPDATE студент SET имя = 'genius' WHERE балы_за_дз > 10 '''
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        for i in rows:
            print(i)
        conn.commit()
    except Error:
        print('ошибка genius')


def num2(conn):
    try:
        sql = '''DELETE FROM студент WHERE id  % 2 = 0 '''
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        for i in rows:
            print(i)
        conn.commit()
    except Error:
        print('ошибка num2')


def create_table(conn, студент):
    try:
        cur = conn.cursor()
        cur.execute(студент)
    except Error:
        print('ошибка create table')


def create_stud(conn, студент):
    sql_v = '''INSERT INTO студент (имя, фамилия, год_рождения, хобби, балы_за_дз)
        VALUES (?, ?, ?, ?, ?)'''

    try:
        cur = conn.cursor()
        cur.execute(sql_v, студент)
        conn.commit()
    except Error:
        print('ошибка на values')


sql_table = '''CREATE TABLE IF NOT EXISTS студент (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    имя TEXT NOT NULL,
    фамилия TEXT NOT NULL,
    год_рождения INT,
    хобби TEXT,
    балы_за_дз INT
    );
    '''

database = r'студент_функ.db'
conection = create_connection(database)

if conection is not None:
    create_table(conection, sql_table)
    # create_stud(conection, ('Хасан', 'Тойчубеков', 2000, 'футбол', 9))
    # create_stud(conection, ('артур', 'артуров', 2000, 'футбол', 2))
    # create_stud(conection, ('алимбек', 'алтбеков', 2003, 'волейбол', 15))
    # create_stud(conection, ('абай', 'абайбеков', 2005, 'футбол', 6))
    # create_stud(conection, ('нурлан', 'нуланов', 2002, 'футбол', 9))
    # create_stud(conection, ('нурланбек', 'нурланбеков', 2006, 'тенис', 3))
    # create_stud(conection, ('али', 'алиев', 2003, 'футбол', 33))
    # create_stud(conection, ('антон', 'антонов', 2003, 'футбол', 28))
    # create_stud(conection, ('алибек', 'алтынбеков', 2004, 'футбол', 0))
    # create_stud(conection, ('алибек', 'алтынбеков', 2004, 'футбол', 0))
    # reed(conection)
    surn(conection)
    genius(conection)
    num2(conection)
    print('отлично')

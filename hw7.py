import sqlite3 as sql

with sql.connect('студент.db') as conn:
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS студент (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    имя TEXT NOT NULL,
    фамилия TEXT NOT NULL,
    год_рождения INT,
    хобби TEXT,
    балы_за_дз INT
    )''')

    # cur.execute('''INSERT INTO студент (имя, фамилия, год_рождения, хобби, балы_за_дз)
    # VALUES ('Хасан', 'Тойчубеков', 2000, 'футбол', 9),
    #        ('артур', 'артуров', 2000, 'футбол', 2),
    #        ('алимбек', 'алтбеков', 2003, 'волейбол', 15),
    #        ('абай', 'абайбеков', 2005, 'футбол', 6),
    #        ('нурлан', 'нуланов', 2002, 'футбол', 9),
    #        ('нурланбек', 'нурланбеков', 2006, 'тенис', 3),
    #        ('али', 'алиев', 2003, 'футбол', 33),
    #        ('антон', 'антонов', 2003, 'футбол', 28),
    #        ('алибек', 'алтынбеков', 2004, 'футбол', 0)
    #        ('алибек', 'алтынбеков', 2004, 'футбол', 0)
    # ''')
    cur.execute('''SELECT * FROM студент WHERE length(фамилия) > 10''')
    # cur.execute('''UPDATE студент SET имя = 'genius' WHERE балы_за_дз > 10''')
    # c = cur.execute('''DELETE FROM студент WHERE id  % 2 = 0''')
    # cur.execute('''SELECT * FROM студент''')
    wor = cur.fetchall()
    for i in wor:
        print(i)
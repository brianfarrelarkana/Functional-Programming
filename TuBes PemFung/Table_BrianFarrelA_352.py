import pymysql

conn = pymysql.connect(
    host = 'sql12.freesqldatabase.com',
    database = 'sql12677767',
    user = 'sql12677767',
    password = 'Af9MmddLEm',
    cursorclass = pymysql.cursors.DictCursor,
)
cursor = conn.cursor()

tabel = """CREATE TABLE ImplantOrgans (serialNum INT(10) NOT NULL AUTO_INCREMENT PRIMARY KEY, implantName VARCHAR(50) NOT NULL,
placement VARCHAR(50) NOT NULL, effect VARCHAR(100) NOT NULL, price INT(10) NOT NULL)"""

cursor.execute(tabel)
conn.close()
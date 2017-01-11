import pymysql as MySQLdb

db = MySQLdb.connect(
host='localhost',
user='newuser',
passwd='123',
db='new_schema',
charset = 'utf8',
use_unicode = True
);

c = db.cursor()
c.execute("INSERT INTO tovar (name, `desc`, cout) values (' Ромы', 'Романыч', 19)")
db.commit()

c.execute("SELECT * FROM tovar")

entries = c.fetchall()

for e in entries:
    print(e)

c.close()
db.close()
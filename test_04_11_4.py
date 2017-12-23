#coding: euc-kr


import sqlite3

db = sqlite3.connect("test.db")

cursor = db.cursor()

# ���� SQL
cursor.execute("""DELETE
                  FROM PHONEBOOK
                  WHERE EMAIL=?""",
               ("visual@naver.com",))

# �ݵ�� Ŀ���� �Ѵ�
db.commit()

cursor.execute("""SELECT NAME, PHONE, EMAIL
                  FROM PHONEBOOK""")

rows = cursor.fetchall()
print(rows)

cursor.close()

db.close()




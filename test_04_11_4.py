#coding: euc-kr


import sqlite3

db = sqlite3.connect("test.db")

cursor = db.cursor()

# 삭제 SQL
cursor.execute("""DELETE
                  FROM PHONEBOOK
                  WHERE EMAIL=?""",
               ("visual@naver.com",))

# 반드시 커밋을 한다
db.commit()

cursor.execute("""SELECT NAME, PHONE, EMAIL
                  FROM PHONEBOOK""")

rows = cursor.fetchall()
print(rows)

cursor.close()

db.close()




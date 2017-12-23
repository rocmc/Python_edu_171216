#coding: euc-kr


import sqlite3

db = sqlite3.connect("test.db")

cursor = db.cursor()

# 수정 SQL 실행
cursor.execute("""UPDATE PHONEBOOK
                  SET    PHONE=?, EMAIL=?
                  WHERE NAME=?"""
               , ("010-8888-9999", "psh@naver.cm", "박신혜"))

# 반드시 커밋을 한
db.commit()

cursor.execute("""SELECT NAME, PHONE, EMAIL
                  FROM   PHONEBOOK
                  WHERE  NAME=?"""
               , ("박신혜",))  # 튜플에 항목이 1개일때는 반드시 ,(콤마)를 뒤에 붙인다
rows = cursor.fetchall()
print(rows)

cursor.close()

db.close()


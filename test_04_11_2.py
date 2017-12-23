#coding: euc-kr


import sqlite3

db = sqlite3.connect("test.db")

# 한번에 한 row 씩 검색 - 튜플로 반환
cursor = db.cursor()
cursor.execute("SELECT NAME, PHONE, EMAIL FROM PHONEBOOK")

rows = cursor.fetchone()
print(rows)

cursor.close()

# 한번에 여러 row 검색 - 튜플의 리스트로 반환
cursor = db.cursor()
cursor.execute("SELECT NAME, PHONE, EMAIL FROM PHONEBOOK")

rows = cursor.fetchall()
print(rows)

cursor.close()

db.close()


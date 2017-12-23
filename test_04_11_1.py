#coding: euc-kr


import sqlite3

# DB 커넥션 객체
db = sqlite3.connect("test.db")

# DB 커서 생성
cursor = db.cursor()

# SQL 실행 - 레코드 추가
cursor.execute("""INSERT INTO PHONEBOOK (NAME, PHONE, EMAIL)
                                 VALUES (?, ?, ?)""",
               ("박신혜", "010-1234-1234", "shinhye@naver.com"))
id = cursor.lastrowid  # 마지막으로 추가되거나 변경된 레코드의 번호
print(id)

# SQL 실행 - 레코드 추가
cursor.execute("""INSERT INTO PHONEBOOK (NAME, PHONE, EMAIL)
                                 VALUES (?, ?, ?)""",
               ("김범수", "010-1111-2222", "visual@naver.com"))
id = cursor.lastrowid
print(id)

db.commit()  # 필수

# 커서 닫기
cursor.close()

# DB 커넥션 닫기
db.close()


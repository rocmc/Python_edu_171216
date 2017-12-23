# coding: euc-kr

# http://ghj1001020.tistory.com/214?category=656849

import sqlite3

# DB 커넥션객체
db = sqlite3.connect("test.db")  # DB 파일이 있으면 열고 없으면 새로 만든다.

# DB 커서 생성
cursor = db.cursor()

# SQL 실행
cursor.execute("""CREATE TABLE PHONEBOOK (
                    NAME CHAR(32),
                    PHONE CHAR(32),
                    EMAIL CHAR(64) PRIMARY KEY
                )""")

# DB 커서 닫기
cursor.close()

# DB 커넥션 닫기
db.close()


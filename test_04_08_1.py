#coding: euc-kr

# DB

# Python Shell에서 실행할 것.
# sqllite의 test.db에 접속하여 처리하기

import sqlite3
con = sqlite3.connect("pytest.db")
cur = con.cursor()

# 테이블 생성

cur.execute("CREATE TABLE cellphone(name TEXT, tel TEXT);")
# <sqlite3.Cursor object at 0x02D80760>

# insert 생성

cur.execute("INSERT INTO cellphone VALUES ('KimS','010-1234-1234');")
# <sqlite3.Cursor object at 0x02D80760>

# select  조회

cur.execute("select * from cellphone;")
# <sqlite3.Cursor object at 0x02D80760>

for i in cur:
    print(i)




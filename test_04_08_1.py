#coding: euc-kr

# DB

# Python Shell���� ������ ��.
# sqllite�� test.db�� �����Ͽ� ó���ϱ�

import sqlite3
con = sqlite3.connect("pytest.db")
cur = con.cursor()

# ���̺� ����

cur.execute("CREATE TABLE cellphone(name TEXT, tel TEXT);")
# <sqlite3.Cursor object at 0x02D80760>

# insert ����

cur.execute("INSERT INTO cellphone VALUES ('KimS','010-1234-1234');")
# <sqlite3.Cursor object at 0x02D80760>

# select  ��ȸ

cur.execute("select * from cellphone;")
# <sqlite3.Cursor object at 0x02D80760>

for i in cur:
    print(i)




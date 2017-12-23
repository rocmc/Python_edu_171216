# coding: euc-kr

# http://ghj1001020.tistory.com/214?category=656849

import sqlite3

# DB Ŀ�ؼǰ�ü
db = sqlite3.connect("test.db")  # DB ������ ������ ���� ������ ���� �����.

# DB Ŀ�� ����
cursor = db.cursor()

# SQL ����
cursor.execute("""CREATE TABLE PHONEBOOK (
                    NAME CHAR(32),
                    PHONE CHAR(32),
                    EMAIL CHAR(64) PRIMARY KEY
                )""")

# DB Ŀ�� �ݱ�
cursor.close()

# DB Ŀ�ؼ� �ݱ�
db.close()


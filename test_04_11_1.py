#coding: euc-kr


import sqlite3

# DB Ŀ�ؼ� ��ü
db = sqlite3.connect("test.db")

# DB Ŀ�� ����
cursor = db.cursor()

# SQL ���� - ���ڵ� �߰�
cursor.execute("""INSERT INTO PHONEBOOK (NAME, PHONE, EMAIL)
                                 VALUES (?, ?, ?)""",
               ("�ڽ���", "010-1234-1234", "shinhye@naver.com"))
id = cursor.lastrowid  # ���������� �߰��ǰų� ����� ���ڵ��� ��ȣ
print(id)

# SQL ���� - ���ڵ� �߰�
cursor.execute("""INSERT INTO PHONEBOOK (NAME, PHONE, EMAIL)
                                 VALUES (?, ?, ?)""",
               ("�����", "010-1111-2222", "visual@naver.com"))
id = cursor.lastrowid
print(id)

db.commit()  # �ʼ�

# Ŀ�� �ݱ�
cursor.close()

# DB Ŀ�ؼ� �ݱ�
db.close()


#coding: euc-kr


import sqlite3

db = sqlite3.connect("test.db")

# �ѹ��� �� row �� �˻� - Ʃ�÷� ��ȯ
cursor = db.cursor()
cursor.execute("SELECT NAME, PHONE, EMAIL FROM PHONEBOOK")

rows = cursor.fetchone()
print(rows)

cursor.close()

# �ѹ��� ���� row �˻� - Ʃ���� ����Ʈ�� ��ȯ
cursor = db.cursor()
cursor.execute("SELECT NAME, PHONE, EMAIL FROM PHONEBOOK")

rows = cursor.fetchall()
print(rows)

cursor.close()

db.close()


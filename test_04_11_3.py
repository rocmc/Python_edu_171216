#coding: euc-kr


import sqlite3

db = sqlite3.connect("test.db")

cursor = db.cursor()

# ���� SQL ����
cursor.execute("""UPDATE PHONEBOOK
                  SET    PHONE=?, EMAIL=?
                  WHERE NAME=?"""
               , ("010-8888-9999", "psh@naver.cm", "�ڽ���"))

# �ݵ�� Ŀ���� ��
db.commit()

cursor.execute("""SELECT NAME, PHONE, EMAIL
                  FROM   PHONEBOOK
                  WHERE  NAME=?"""
               , ("�ڽ���",))  # Ʃ�ÿ� �׸��� 1���϶��� �ݵ�� ,(�޸�)�� �ڿ� ���δ�
rows = cursor.fetchall()
print(rows)

cursor.close()

db.close()


#coding: euc-kr

# DB


# sqllite�� test.db�� �����Ͽ� ó���ϱ�
#
# >> > import sqlite3
# >> > con = sqlite3.connect("test.db")
# >> > cur = con.cursor()
#
# # ���̺� ����
#
# >> > cur.execute("CREATE TABLE PhoneBook(name TEXT, phonenum TEXT);")
# < sqlite3.Cursor object at 0x0146E0E0 >
#
# # insert ����
#
# >> > cur.execute("INSERT INTO PhoneBook VALUES('Dhal','010-1234-5678');")
# < sqlite3.Cursor object at 0x0146E0E0 >
# >> > cur.execute("INSERT INTO PhoneBook VALUES('Moon','010-1234-5678');")
# < sqlite3.Cursor object at 0x0146E0E0 >
#
# # select  ��ȸ
#
# >> > cur.execute("SELECT * FROM PhoneBook;")
# < sqlite3.Cursor object at 0x0146E0E0 >
# >> > for i in cur:
#     print(i)
#
# ('Dhal', '010-1234-5678')
# ('Moon', '010-1234-5678')
#
# # commit() ó���� ���ص� ��ȸ�� �����ϴ�.  ��ũ�� �����ϱ� ���ؼ��� commit�� ó���Ѵ�.
#
# >> > con.commit()
#
# # �ٸ� ���丮�� sqlite3 �� ��ġ�Ǿ� ���� ��� connect() �޼ҵ忡 ���� ��ġ�� �ۼ��Ѵ�.
#
# >> > import sqlite3
# >> > con = sqlite3.connect("C:\\sqlite3\\test.db")
# >> > cur = con.cursor()
# >> > cur.execute("SELECT * FROM t1")
# < sqlite3.Cursor object at 0x01428EE0 >
# >> > for i in cur:
#     print(i)
#
# (1, 'text ', 123456.0, '2013-07-17')
# (2, 'text ', 123456.0, '2013-07-17')
# (3, 'text ', 123456.0, '2013-07-17')
# (4, 'text ', 123456.0, '2013-07-17')
# >> >

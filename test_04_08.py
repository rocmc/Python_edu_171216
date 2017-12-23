#coding: euc-kr

# DB


# sqllite의 test.db에 접속하여 처리하기
#
# >> > import sqlite3
# >> > con = sqlite3.connect("test.db")
# >> > cur = con.cursor()
#
# # 테이블 생성
#
# >> > cur.execute("CREATE TABLE PhoneBook(name TEXT, phonenum TEXT);")
# < sqlite3.Cursor object at 0x0146E0E0 >
#
# # insert 생성
#
# >> > cur.execute("INSERT INTO PhoneBook VALUES('Dhal','010-1234-5678');")
# < sqlite3.Cursor object at 0x0146E0E0 >
# >> > cur.execute("INSERT INTO PhoneBook VALUES('Moon','010-1234-5678');")
# < sqlite3.Cursor object at 0x0146E0E0 >
#
# # select  조회
#
# >> > cur.execute("SELECT * FROM PhoneBook;")
# < sqlite3.Cursor object at 0x0146E0E0 >
# >> > for i in cur:
#     print(i)
#
# ('Dhal', '010-1234-5678')
# ('Moon', '010-1234-5678')
#
# # commit() 처리를 안해도 조회가 가능하다.  디스크에 저장하기 위해서는 commit을 처리한다.
#
# >> > con.commit()
#
# # 다른 디렉토리에 sqlite3 가 설치되어 있을 경우 connect() 메소드에 현재 위치를 작성한다.
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

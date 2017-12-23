# coding: euc-kr


import sqlite3

con = sqlite3.connect('student.db')
sql = '''
CREATE TABLE student
(name text, no integer, addr text)
'''
c = con.cursor()
c.EXECUTE(sql)
c.close()
con.commit

import sqlite3

con = sqlite3.connect(student.db)
sql = '''
INSERT INTO student VALUES ...


c=con.cursor()
x.EXECUTE (sql, ('학생2',2,'서울'))

data=[('학생3',3,'강원'),('학생4',4,'경기'),('학생5',5,'충청')]

c.EXECUTE madfsdfsdf
      gfddfhgdfjdfghjghk

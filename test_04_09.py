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
x.EXECUTE (sql, ('�л�2',2,'����'))

data=[('�л�3',3,'����'),('�л�4',4,'���'),('�л�5',5,'��û')]

c.EXECUTE madfsdfsdf
      gfddfhgdfjdfghjghk

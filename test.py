#coding=utf-8
from jsontomysql import mysqlhelper
a=mysqlhelper()
a.query('select * from test')
a.get('select * from test')
import json
# dataJson = json.load(open('format_file.json',encoding='UTF-8'))
f=open('results.json')
datajson=json.load(f)
demo=datajson[0]
for item in datajson:
    a.insert("insert into test(program,video,img,title)values('%s','%s','%s','%s')"%(item['program'],item['video'],item['img'],item['title']))
#
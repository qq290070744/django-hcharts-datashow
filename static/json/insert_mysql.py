#!/usr/bin/env python
#coding:utf-8
import pymysql,json
def execsql(sql):
    conn = pymysql.connect(host='rm-wz91lk2xv4e35nl66o.mysql.rds.aliyuncs.com',user='jiang',passwd='Jiangwenhui1@3',db='datashow',port=3399,charset='UTF8')
    cur = conn.cursor()
    reCount = cur.execute(sql)
    conn.commit()

    cur.close()
    conn.close()
    print (reCount)
# with open("pvuv",encoding='utf8') as f:
#     for i in f:
#         if ',' in i:
#             day,pv,uv=i.split(',')
#             sql="insert into app01_访问量 values (null,'{}','{}','{}')".format(day,pv,uv)
#             print(sql)
#             execsql(sql)

with open("可缩放的时间轴.json",encoding='utf8') as f:
    data=''
    for i in f:
        data+=i
    data = json.loads(data)
    for i in data:
        sql="insert into app01_时间轴 values (null,'{}','{}')".format(i[0],i[1])
        print(sql)
        execsql(sql)
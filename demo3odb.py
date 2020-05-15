import pymssql
import pyodbc
# sqlserver的连接
# ↓打开数据库连接 这里的host='.'也可用本机ip或ip+端口号(sqlserver默认端口号：1433)
conn = pymssql.connect(host="127.0.0.1:1133",user= "DESKTOP-7TIR796\AsamuCC",password= "19961016xiaobao", database="TEST_1",charset='GBK' )

cursor = conn.cursor()   # ↓使用cursor()方法获取操作游标

sql = input("输入操作语句：")   # ↓SQL 查询语句

try:
   cursor.execute(sql)  # 执行SQL语句
  
   results = cursor.fetchall()   # 获取所有记录列表

   print(results)
except:
   print(results)
# 关闭数据库连接
conn.close()


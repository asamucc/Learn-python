


"""
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
#创建数字识别方法↑
"""


"""
#循环+判断↓

while 1:
  a=input("输入一个数字")
  b=input("输入第二个数字")
  if is_number(a) is False or is_number(b) is False: #判断是否为数字
     print("重新输入") 
     continue
  else:
       A=float(a)
       B=float(b)
       if A>B:
          print(A,"大于",B)
       elif A<B:
          print(A,"小于",B)
       else:
          print(A,"等于",B)
"""



"""
def print_ED(N):
    try:
        __number__=N
        if __number__!=0:
           print("60分以上的：",c)
           print("60分以下的：",d)
    except ValueError:
        pass

c={}
d={}
while (len(c)+len(d))<10:

    print("=====已录入" ,len(c)+len(d),"人=====")
    print_ED(len(c)+len(d))
    NAME=input("输入姓名：")
    MARK=input("输入成绩：")

    if (is_number(MARK) is False):
       print("输入有误，重新输入")
       continue
    elif float(MARK)>100:
       print("不能超出范围")
       continue
    elif float(MARK)>=60 and is_number(MARK) is True:
       c[NAME]=MARK
    elif float(MARK)<60 and is_number(MARK) is True:
       d[NAME]=MARK
else:
    print("=====已录入" ,len(c)+len(d),"人=====") 
    print_ED(len(c)+len(d))
"""



# b=list(range(1,100,4)) #表示1-100的数列,步进为4
# print(b) #输出1，5，9，13，...93,97


"""
#乘法表
for i in range(1,10):
   for j in range(1,i+1):
       #第三步，限制计算区间
        print(j,"X",i,"=",j*i,end="   ") 
        #第一步，打印所有乘积且不换行
   print()
        #第二步，内循环9次结束后换行
"""



"""
红绿灯
import time  #时间库函数调用
while 1:
 for i in range(1,74):
  print("%d秒"%(i)) #如果i是数字，则用%d或%f代替
  i=int(i)
  if i<=35:
    print("RED灯第",(i%36),"秒闪烁")
  elif i>35 and i<=70:
    print("GREEN灯第",(i%36)+1,"秒闪烁")
  elif i>70 and i<=73:
    print("YELLOW灯"+"第",(i%70),"秒闪烁")
  time.sleep(1)
"""




"""
#异常捕获
NAME=input("NAME:")
AGE=input("AGE:")
try: #当try语句中运行报错时，执行expect
   if int(AGE)>18:  #int（）运行报错
      print(NAME,"成年了")
   else:
      print(NAME,"未成年")
except:
   print("年龄输入错误")
"""




#注册功能
print("========注册页面=========")
######先定义方法
def is_hefa(username,password):
   if 9>=len(username)>=6:
      if list(username)[0].islower():
         if 12>=len(password)>=8:
          return True
         else:
          print("密码必须8-12位数")

      else:
         print("账号必须小写字母开头")
   else:
      print("账号必须6-9位数")
######再执行方法
Userinfo={}
while 1:
  UserID=input("输入账号：")
  PassWord=input("输入密码：")
  if is_hefa(UserID,PassWord) is True:
     Userinfo[UserID]=PassWord
     print(Userinfo)
  else:
     continue


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
#创建数字识别方法↑

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

# e=[1,2,3,4,5,6,7,8,9,0]
# for i in e:
#     print(i)

# b=list(range(1,100,4)) #表示1-100的数列,步进为4
# print(b) #输出1，5，9，13，...93,97



for i in range(1,10):
   for j in range(1,i+1):
       #第三步，限制计算区间
        print(j,"X",i,"=",j*i,end="   ") 
        #第一步，打印所有乘积且不换行
   print()
        #第二步，内循环9次结束后换行

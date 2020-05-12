
"""
print("hello word")  #单个内容
print("你好！", 123) #多个内容
print("hh"+"！xx") #相同类型字符串内容拼接
print("HOLLE"*10)  #打印10次
print(((1+2)*100-299)/2)  #数学运算结果：0.5
print(2>3) #判断结果为：Fales
"""



"""
a=float(input("请输入内容1："))  #input默认输入内容为字符串
b=float(input("请输入内容2："))


print(type(a))  #结果显示位<class 'str'>

print("已经输入",a+b)   #此处字符串拼接
"""



"""
#print(len("123456"))  #输出结果位：6

# a=input("①：")
# b=input("②：")
# print("长度之和",len(a)+len(b))

#元组
"""



"""
a = (1,2,3,3,4,5,"hh","xx",True,False) #元组的形式
#批量取值满足数轴的左闭右开原则
print(a[-2]) #取倒数第二个
print(a[:4]) #取角标0到4的之前的，不包括4
print(a[6:8]) #结果为‘hh’‘XX’
print(a[8:])  #取角标8以后的值
"""



"""
# print(a.count(3))  #输出a元组中3的数量
# print(a.index(2))  #输出元组2的下标

# b=(a,"hh","XX")
# print(b[0][0]) #输出a[0]的值
# print(b[0].index(2)) #输出a元组中2的角标

"""



"""
c = [1,2,3,3,4,5,"hh","xx",True,False]
# d = c.pop(c.index("hh")) #数组c的hh提取出来赋值给d，c中的“hh”消失
# e = c.pop(c.index("xx")) #
# print(d)
# print(len(e+d))

i=[11,22,33,44]
# c.insert(0,"insert") #向下标0之前插入“insert”
# print(c[0])  #输出为insert

# c.append("append")  #c数组中追加“append”
c.extend(i) #数组中批量增加元素
print(c[-1]) #输出最后一个元素，结果为“append”
print(c+i)   #合并输出c和i数组
c.remove(c[10]) #删除c数组的“11”
print(c)
"""


"""
1.字典的值没有顺序
2.字典结构必须是键值对
"""


"""
a={
    "NAME":"ZHANG3",  #KEY:VALUES，
    "NUM":15520202220,
    "AGE":18,
    "MAJORNUM":0
   }
"""

"""
print(a["NAME"]) #输出结果为‘zhang3’
#######
a["HIGH"]="183CM" #新增身高“HIGH”键值
print(a) #a多了一项“HIHG”
b=a.get("NAME") #a的NAME键值赋值给b
print(a) #a不变
print(b) #b中有NAME的值
#######
b=b+a.pop("NAME") #提取a的NAME键值给b
print(a) #a减少一项“NAME”
print(b) #b有两个"NAME"的值
"""


"""
a["NAME"]="LI4"  #若有NAME,则修改值为”LI4“，否则直接新增一个键值

a.update(NAME="LI1") #若有NAME1,则修改值为”LI1“，否则直接新增一个键值
print(a)
"""




print("----空白字典已创建----")
A={}
global sss 
while A!=None:
 A["NAME"]=input("输入用户名：")
 A["AGE"]=input("输入年龄：")
 A["SEX"]=input("输入性别：")

 if len(A["NAME"])==0 or len(A["AGE"])==0 or len(A["SEX"])==0:
   print(A,"数据不完整")
   print(len(A))
   continue
 if len(A["NAME"])>0 and len(A["AGE"])>0 and len(A["SEX"])>0:  

   print(A)
   break

sss=input("是否修改(Y/N):")
print(A) 

while len(sss)!= 0:

  if sss!="Y" and sss!="N":
     print("错误选项，请重新输入：")
     
     sss=input("是否修改(Y/N):")
  if sss=="Y":
     a=input("请输入修改项（NAME/AGE/SEX）:")
     b=input("请输入值：")
     A[a]=b
     print("结果如下：")
     print(A)
     break
  if sss =="N":
     print("结果如下：")
     print(A)
     break
    
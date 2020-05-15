"""
t=input("读取哪个TXT：")
with open("J:\项目\%s"%t,"r",encoding="utf8") as f:
    text=f.readlines()
for i in text:
    print(i)
"""
while 1:
    a=int(input("a:"))
    b=int(input("b:"))
    x=0
    y=0
    for i in range(0,10):
        x=x+a
        if x==b:
            x=i
            y=1
            break
        # print(i)
    if y<1:
        x=-1
    print(x)
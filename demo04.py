"""
class 类名（）
类名的首字母必须大写
类里面的所有方法都要传参数self
"""
#第一步，类创建
class fatherClass():
    """
    # 信息：姓名，年龄，性别，专业
    # 日记本：
    # 爱好：
    # 工作
    """
    def __init__(self,stuname,age,sex,major):
        self.stuname=stuname
        self.age=age
        self.sex=sex
        self.major=major
    def dothing(self,NUM):
        """
        1，介绍；2，专业介绍
        """
        if NUM ==1:
         print("自我介绍：","我是",self.stuname,"年龄",self.age,"性别",self.sex)
        elif NUM==2:
         print("我的专业是：",self.major)
        else:
         print("你想问什么？")
    def interesting(self):
        print("唱跳rap篮球")
    def work(self):
        print("练习生")


"""
#第二步，实例化
Mrwang = MyfirstClass("WANG","23","男","物理学")
Mrwang.work()
Mrwang.dothing(1)
"""


#继承/重写类
class sonClass(fatherClass):
    def work(self): #类的重写，相当子类可改写父类方法
        print("我是厨师")
ZHANG=sonClass("ZHANG3","2","男","计算机") #子类实例化
ZHANG.work() #输出子类重写结果
ZHANG.dothing(1) #输出继承方法的结果

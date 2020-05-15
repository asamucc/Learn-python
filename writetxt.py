import time

while 1:
 s=time.strftime("----------"+"%Y-%m-%d  %H:%M:%S"+"----------")
 print(s)

 text = input("请输入文字，"+"close"+"退出：")
 if text=="close":
    break
 with open("J:\项目\记事本.txt","a",encoding="utf8") as f:  
  # 固定文件操作模板：with open（文件名，模式：w重输/a追加"，encoding="GBK"）as f。
    f.write(s+"\n")
    f.write(text+"\n") #执行写入方法：write（内容）。
    f.write("----------------------------------------\n")

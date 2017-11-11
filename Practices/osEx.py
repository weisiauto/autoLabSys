import os

a=[]
a.append(os.getcwd())
os.chdir("D:\\")
a.append(os.getcwd())
os.chdir(a[0])
a.append(os.getcwd())
a.append(os.listdir())
print(a)
'''
for i in os.walk("E:\\"):
    print(i)
'''
os.system("calc")


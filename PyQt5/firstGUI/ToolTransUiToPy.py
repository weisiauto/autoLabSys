import os
import os.path

#UI 文件所在路径
dir='./'

#列出当前目录下所有UI文件
def listUiFile():
    UiFiles=[]
    files=os.listdir(dir)
    for filename in files:
        if os.path.splitext(filename)[1]=='.ui':
            UiFiles.append(filename)
    return UiFiles

#把扩展名.ui的文件改成扩展名为.py的文件

def transPyFile(filename):
    return os.path.splitext(filename)[0]+'.py'

#调用系统命令把UI文件转换成python文件

def transUitoPy():
    listUi=listUiFile()
    for uifile in listUi:
        pyfile=transPyFile(uifile)
        cmd='pyuic5 -o {pyfile} {uifile}'.format(pyfile=pyfile,uifile=uifile)
        os.system(cmd)

#程序入口

if __name__=='__main__':
    transUitoPy()
    
        

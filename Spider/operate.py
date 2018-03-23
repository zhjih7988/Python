import os
import os.path
from MyFunFile import getNumber
l = []

def openPath(path=""):
    fileList = os.listdir(path)   #获取path目录下所有文件
    for filename in fileList:
        pathTmp = os.path.join(path,filename)   #获取path与filename组合后的路径
        if os.path.isdir(pathTmp):   #如果是目录
            openPath(pathTmp,l)        #则递归查找
        else:
        # if filename[-4:].lower()=='.pdf':   # 不是目录,则比较后缀名
            out = getNumber(filename)
            if out is not None:
                newPath = os.path.join(path,out) 
                os.renames(pathTmp,newPath)
            
            # shutil.move(pathTmp,out)

path=r"C:\Users\Pancras\Desktop\课件"
path = r'G:\安全\渗透教程\最新Kali渗透'
openPath(path)

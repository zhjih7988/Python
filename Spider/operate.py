import os
import os.path
from MyFunFile import getNumber, getTen
l = []

def openPath(path=""):
    fileList = os.listdir(path)   #获取path目录下所有文件
    for filename in fileList:
        pathTmp = os.path.join(path,filename)   #获取path与filename组合后的路径
        if os.path.isdir(pathTmp):   #如果是目录
            out = getTen(pathTmp[-1:])
            if out is not 10:
                newPath = os.path.join(path,str(out))
                os.renames(pathTmp,newPath)
            print(pathTmp)
            openPath(pathTmp)        #则递归查找
        else:
            print(filename)
            out = getNumber(filename)
            if out is not None:
                newPath = os.path.join(path,out) 
                os.renames(pathTmp,newPath)


def main():
    # path=r"C:\Users\Pancras\Desktop\课件"
    # path = r'G:\安全\渗透教程\最新Kali渗透'
    path = r'G:\fundamental  algorithms\12、程序猿的内功修炼，学好算法与数据结构'
    openPath(path)


if __name__ == '__main__':
    main()
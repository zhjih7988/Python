import os
import os.path
import re
from MyFunFile import getNumber, getTen

def openPath(path=""):
    fileList = os.listdir(path)   #获取path目录下所有文件
    for filename in fileList:
        pathTmp = os.path.join(path,filename)   #获取path与filename组合后的路径
        if os.path.isdir(pathTmp):   #如果是目录
            openPath(pathTmp)        #则递归查找
            
            out = getNumber(pathTmp)
            if out is not None:
                newPath = os.path.join(path,out) 
                print(newPath)
                os.renames(pathTmp,newPath)
            # out = getTen(pathTmp[-1:])
        #     if out is not 10:
        #         newPath = os.path.join(path,str(out))
        #         os.renames(pathTmp,newPath)
        #     print(pathTmp)
        
        else:
            print(filename)
            out = getNumber(filename)
            if out is not None:
                newPath = os.path.join(path,out) 
                os.renames(pathTmp,newPath)
        

def main():
    # path=r"C:\Users\Pancras\Desktop\课件"
    # path = r'G:\安全\渗透教程\最新Kali渗透'
    # path = r'G:\fundamental  algorithms\12、程序猿的内功修炼，学好算法与数据结构'
    # path = r'G:\CS\19、高性能可扩展MySQL数据库设计及架构优化 电商项目\高性能可扩展mysql'
    # path = r'G:\CS\63、前端跳槽面试必备技巧'
    # path = r'F:\数学\2019【启航数学】张宇\02 教材精讲班\线代'
    # path = r'F:\数学\2019【启航数学】张宇\02 教材精讲班\概率'
    path = r'C:\Users\Pancras\Desktop\a'
    openPath(path)


if __name__ == '__main__':
    main()
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
            # out = getNumber(pathTmp)
            # if out is not None:
            #     newPath = os.path.join(path,out) 
            #     print(newPath)
            #     os.renames(pathTmp,newPath)

            # out = getTen(pathTmp[-1:])
        #     if out is not 10:
        #         newPath = os.path.join(path,str(out))
        #         os.renames(pathTmp,newPath)
        #     print(pathTmp)
        
        else:
            # a = pathTmp.split('\\')[:-2]
            # newPath = ''
            # for i in a:
            #     newPath = newPath + i + '\\'
            # print(pathTmp)
            # newPath = os.path.join(newPath,filename)
            # print(newPath)
            # os.renames(pathTmp,newPath)
            '''

            '''
            out = getNumber(filename)
            if out is not None:
                newPath = os.path.join(path,out) 
                os.renames(pathTmp,newPath)

def main():
    path = r'C:\Users\Pancras\Desktop\概率'
    path = r'F:\数学\2019【启航数学】张宇\02 教材精讲班\概率'
    path = r'F:\数学\2019【启航数学】张宇\02 教材精讲班\高数\高数下'
    path = r'F:\数学\2019【启航数学】张宇\02 教材精讲班\线代'
    openPath(path)
    # count = 0
    # for root, dirs, files in os.walk(path):
    #     for each in files:
    #         count +=1
    # print(count)
    
if __name__ == '__main__':
    main()
# coding: utf-8
import time, sys, os
from pymouse import PyMouse

def GetPosition():
    while 1==1:
        m = PyMouse()
        tmp = m.position()
        print(tmp)
        time.sleep(2)

# 利用python实现对鼠标的移动点击操作
def ClickScreen(x,y):
    m = PyMouse()
    m.position()  # 获取当前坐标的位置
    while 0 == 0:
        # m.click(1087,730)
        m.click(x,y)
        time.sleep(1)
# m.move(x,y)#鼠标移动到xy位置
# m.click(x,y)#移动并且在xy位置点击
# m.click(x,y,1|2)#移动并且在xy位置点击,左右键点击


if __name__ == '__main__':
    x =1054
    y = 614
    ClickScreen(x,y)

    # GetPosition()
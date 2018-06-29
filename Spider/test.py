# coding: utf-8
import time
import datetime
from pymouse import PyMouse

def GetPosition():
    while 1==1:
        m = PyMouse()
        tmp = m.position()
        print(tmp)
        time.sleep(2)

# 利用python实现对鼠标的移动点击操作
def ClickScreen(x, y, minute):
    m = PyMouse()
    m.position()  # 获取当前坐标的位置
    minute = datetime.datetime.now().minute + minute
    while True:
        i = datetime.datetime.now()
        # h = i.hour
        min = i.minute
        if min < minute:
            # m.click(1087,730)
            m.click(x, y)
            time.sleep(1)
        else:
            break
        #取消
        # m.click(1146, 245)
# m.move(x,y)#鼠标移动到xy位置
# m.click(x,y)#移动并且在xy位置点击
# m.click(x,y,1|2)#移动并且在xy位置点击,左右键点击


if __name__ == '__main__':
    x = 726
    y = 225
    m = PyMouse()
    m.position()  # 获取当前坐标的位置
    for i in range(1,50):
        m.click(x, y)
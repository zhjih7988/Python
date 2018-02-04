# coding: utf-8
import time
from pymouse import PyMouse
m = PyMouse()
m.position()#获取当前坐标的位置

while 0==0:
    m.click(1087,730)
    time.sleep(0.8)
# m.move(x,y)#鼠标移动到xy位置
# m.click(x,y)#移动并且在xy位置点击
# m.click(x,y,1|2)#移动并且在xy位置点击,左右键点击

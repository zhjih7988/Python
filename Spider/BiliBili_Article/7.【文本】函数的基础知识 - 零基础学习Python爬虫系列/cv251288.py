# # 函数
#
# # def 函数名（参数列表）:
# #   函数体
#
# def myFirstFun(a,b):
#   return a+b
#
#
# c = 100 + myFirstFun(10,20)
# print(c)
# print("="*20)
#
# # 100 + (10 + 20) = 130
#
# # -----------------------
# def mySecondFun(a,b=50):
#   return a + b
#
# print(mySecondFun(10))
#
# print("="*30)
#
# # （一般情况下）参数有几个，我们就需要传入几个
# # 如果已经给予了默认值，那么则可以使用默认值，而不用传入必须个数
# # 默认函数参数是顺序一一对应的，但是我们可以把参数单独赋值
# # 默认值尽量往后放
#
# # 更多tips
#
# # 1,不定长参数
# # 1.1 将不定长的参数放入list或者tuple等中，然后传入
# # 1.2 如果不用1.1的方法，我们可以通过*号来实现，不定长的参数
# def myThirdFun(*b):
#   sum = 0
#   for eve in b:
#     sum = sum + eve
#   return sum
#
# print(myThirdFun(10,20,30,40,50))
# print("="*30)
#
# # ----------------------
#
#
# # 变量的生效区域
# # 从这里开始执行
# # 1-3-2
#
# num = 1
# def myForthFun():
#   global num
#   print(num)
#   num = 100
#   print(num)
#
# myForthFun()
# print(num)
#
#
#
# lambda 匿名函数
# sum = lambda a,b:a+b
# print(sum(10,20))
# lambda 参数1，参数2，参数....：表达式
lambda_data = lambda a,b,c:print(a+b)
lambda_data(10,20,30)

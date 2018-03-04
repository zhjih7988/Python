本文是视频av20131703的相关代码文档
# 异常
# 异常和错误
# 错误 （一般情况下指的是语法错误），我们在写一个程序的时候，出错了。
# 异常，一般情况下指程序运行过程中出错了。
# 处理异常
try:
  a = 100
  x = a + "a"
except:
  print("有错啦")
print("="*20)
# try:
#  语句
# except 异常的名字 as 异常赋值名字:
#  解决方法
# TypeError
# a = 100
# x = a + "a"
try:
  a = 100
  # x = a + "a" # TypeError
  c = a + b # NameError
except TypeError as e:
  print("TypeErroe,有错啦,错误是：",e)
except NameError as e:
  print("NameError,有错啦,错误是：",e)
# 异常有很多很多，TypeError,NameError,OSError,ValueError,IOError。。。。
print("="*20)
try:
  a = 100
  c = a + b
except Exception as e:
  print("Exception:",e)
print("="*20)
# 抛出异常
# raise NameError("temp test")
# a = 1
# b = 2
# c = a + b
# raise IOError("你就错了，我就让你错误")
print("="*20)
# 关键词finally的用法
try:
  a = 100
  # x = a + "a" # TypeError
  c = a + b # NameError
except TypeError as e:
  print("TypeErroe,有错啦,错误是：",e)
except NameError as e:
  print("NameError,有错啦,错误是：",e)
finally:
  print("finally")

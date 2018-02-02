# id="s4p0" --> s4p72
import re

# 逐行读 
file_object = open(r'C:\Users\Pancras\Desktop\Python\Spider\r.txt',encoding="utf-8") 
try: 
  for line in file_object: 
    #print(line, end = '') 
    for i in range(1, 74):
        s = "li4_" + i.__str__()
        if s in line:
            print(line)
            break
        # print(s)
finally: 
  file_object.close() 



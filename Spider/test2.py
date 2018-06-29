import time

import datetime

while True:
    i = datetime.datetime.now()
    h = i.hour
    m = i.minute
    if h == 22 and m < 5:
        print("hahhahah")
    else:
        break
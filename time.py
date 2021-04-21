#-*- coding: utf-8 -*-
import time
import random
print("Текущая дата: ",time.strftime("%d.%B.%Y"))
print("Текущее время: ",time.strftime("%H:%M:%S"))
start = time.time()
i = 0
while i<100:
    r = random.randrange(-500,500)
    ra = random.randrange(-450, 600)
    print(r, " + ",ra, " = ", r+ra)
    i+=1
    if i%20 == 0:
        print("Надо отдохнуть")
        time.sleep(5)
        print("Lets Do it!")
stop = time.time()
print(start - stop)
        

import math
for x in range(0,1000):
    for i in range(1,1000):
        if x+i+math.sqrt(x*x+i*i) == 1000:
            print(x*i*math.sqrt(x*x+i*i))

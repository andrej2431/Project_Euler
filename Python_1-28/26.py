d = 0
a = 0
from decimal import *
getcontext().prec = 100
def dec(n):
    a = Decimal(1)
    b = Decimal(n)
    t = str(a/b)
    print(t)
    rec = t[2]
    
    for x in range(len(t[2:])):
        print(x)
        for i in range(1,len(rec)+1):
            d =  rec[-i:]
            
            if len(d)<len(t[3+x:]):
                if t[3+x:3+x+len(d)] == d*(len(t[x+3:])//len(d)):
                    return len(d),t[3+x:3+x+len(d)]
            else:
                print('smaller',d)
        rec+=t[x+3]
        print(rec)
    return 0
   
##for x in range(2,1000):
##    t = dec(x)
##    print(t)
##    if t > d:
##        d = dec(x)
##        a = x
##
##print(a)

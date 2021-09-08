numbers = set(range(10000))
a_pair = 0

import math
def divisors(n) : 
    i = 2
    t = [1]
    while i <= math.sqrt(n): 
          
        if (n % i == 0) : 
            if (n / i == i) : 
                t.append(i) 
            else :  
                t.append(i)
                t.append(n/i) 
        i = i + 1
    return sum(t)
n = 0
k = 0
for i in numbers:
    x = divisors(i)
    l = divisors(x)
    if l == i and x!=i:
        print(x,i)
        n+=(x+i)

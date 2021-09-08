import math
def d(n) : 
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
abundants = set(i for i in range(1,28124) if d(i) > i)

def abundantsum(i):
    return any(i-a in abundants for a in abundants)

print (sum(i for i in range(1,28124) if not abundantsum(i)))

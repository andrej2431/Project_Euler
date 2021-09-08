mapping = {1:0}

def Collatz(n,ens,k = 1):
    if n == 1 :
        for z in ens:
            mapping[z]=k-mapping[z]
        return k
    
    if n not in mapping:
        mapping[n] = k
        ens.append(n)
    else:
        k=k+mapping[n]
        for z in ens:
            mapping[z]=k-mapping[z]
        return k
    
    if n%2==0:
        n//=2
    else:
        n=n*3+1
        
    return Collatz(n,ens,k+1)
t = 0
l = 0
for x in range(1000000-1,500000,-1):
    a = Collatz(x,[])
    if  a>t:
        t=a
        l=x
print(l)












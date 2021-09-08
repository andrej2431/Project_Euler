def fac(n):
    if n==1:
        return 1
    return n*fac(n-1)
def t(n,f):
    return n//fac(f),n%fac(9)
def find(n,t,k = 9):
    if n == 0:
        return t
    t.append(n//fac(k))
    return find(n%fac(k),t,k-1)

a = find(1000000-1,[])
a.extend((10-len(a))*[0])
answer = ''
b = list(range(10))
for number in a:
    answer+=str(b.pop(number))
print(answer)


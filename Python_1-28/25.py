f1 = 1
f2 = 1
x = 1
while len(str(f1))<1000:
    f1,f2 = f2,f1+f2
    x+=1
print(x)

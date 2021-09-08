t = 1
for x in range(1,501):
    l = x*2+1
    t+=(l*(4*l-6)+6)
print(t)



b = sum([((x*2+1)*(4*(x*2+1)-6)+6) for x in range(1,501)])+1
print(b)

import time
s= time.time()
triangle = open('pyramid.txt','r')
p_tree = []
for row in triangle:
    l = list(map(int,row.strip().split()))
    p_tree.append(l)
    
for x in range(len(p_tree)-2,-1,-1):
    for i in range(len(p_tree[x])):
        p_tree[x][i]+= max(p_tree[x+1][i],p_tree[x+1][i+1])
f = time.time() - s
print(p_tree[0][0],'took',round(f*1000,5),'miliseconds')

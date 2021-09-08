numbers = open('numbers_13.txt','r')
n_list = []
for line in numbers:
    n_list.append(int(line))
t = 0
for n in n_list:
    t+=n
k = len(str(t))-10
answer = int(t/(10**k))
print(answer)

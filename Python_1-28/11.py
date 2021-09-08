a = list(open('numbers.txt','r'))
nl = []
for x in a:
    nl.append(list(map(int,x.replace('/n','').split())))

def lprint(l):
    for row in l:
        print(row)

answer = 0
for x in range(20):
    for i in range(20):
        if x < 17:
            possible = nl[x][i]*nl[x+1][i]*nl[x+2][i]*nl[x+3][i]
            answer = max([answer,possible])

        if i < 17:
            possible = nl[x][i]*nl[x][i+1]*nl[x][i+2]*nl[x][i+3]
            answer = max([answer,possible])

            
        if x < 17 and i < 17:
            possible = nl[x][i]*nl[x+1][i+1]*nl[x+2][i+2]*nl[x+3][i+3]
            answer = max([answer,possible])


        if x > 2 and i < 17:
            possible = nl[x][i]*nl[x-1][i+1]*nl[x-2][i+2]*nl[x-3][i+3]
            answer = max([answer,possible])

print(answer)

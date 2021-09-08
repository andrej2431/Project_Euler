x = 1
y = 1
answer = 0
while x <4000000:
    x=x+y
    y=x-y
    if x%2 == 0:
        answer+=x
        
print(answer)

a = 999/3
b = 999//5
print(a+b)

al = 0
for x in range(1000):
    if x%3 == 0:
        al+=x
    elif x%5 == 0:
        al+=x
print(al)

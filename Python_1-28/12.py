def nu_f(n):
    result_set = set()
    for i in range(1, 1+int(n**0.5)):
        if n % i == 0:
            result_set.add(n // i)
            result_set.add(i)
    return len(result_set)
x = 0
n = 1
while True:
    x+=n
    n+=1
    t = nu_f(x)
    if t>500:
        print(x)
        break

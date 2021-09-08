primes = [2]
answer = 2
i = 3
while i < 2000000:
    for row in primes:
        if i % row == 0:
            break
    else:
        answer+=i
        primes.append(i)
        
    i+=2
    print(i)
print(answer)

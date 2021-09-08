x = 600851475143
def next_prime(number):
    for x in range(2,number):
        if number % x == 0:
            return next_prime(int(number/x))
    else:
        return number
print(next_prime(x))
            

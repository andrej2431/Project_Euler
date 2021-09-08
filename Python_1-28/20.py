def factorial(n):
    if n ==1:
        return 1
    return factorial(n-1)*n
print(sum(map(int,(list(str(factorial(100)))))))

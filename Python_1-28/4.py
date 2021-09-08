x = 3
def palindrome(number):
    palindrome = 0
    for x in range(10**number,0,-1):
        for i in range(10**number,0,-1):
            if str(x*i) == str(x*i)[::-1]:
                palindrome = max ([palindrome,x*i])
    return palindrome


print(palindrome(3))

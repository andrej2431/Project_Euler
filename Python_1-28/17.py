
numbers = [0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8]
tens = [0,3,6,6,5,5,5,7,6,6]

def num_to_word(x):
    t = 0
    number = list(list(map(int,str(x))))
    h = None
    print(number)
    if len(number)>2:
        h = number[0:1][0]
        x= x-h*100
    if h:
        t = 7+numbers[h]
        if x>0:
            t+=3
    if x<20:
        t+=numbers[x]
    else:
        
        t+=numbers[number[-1]]+tens[number[-2]]
    return t
        
l = 0      
for x in range(1,1000):
    l+=num_to_word(x)
    print(l)
print(l+11)

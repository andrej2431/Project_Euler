sum_square = 0
square_sum = 0
for x in range(101):
    sum_square+= x*x
    square_sum+= x

print(square_sum**2-sum_square)

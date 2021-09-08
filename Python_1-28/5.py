
list_ = []
number = 1
def whatever():
    for x in range(1,20):
        if number % x == 0:
            pass
        else:
            for row in all_numbers(number,[]):
                if row not in list_:
                    list_.append(row)
    print(list_)




def all_numbers(number,that_list):
    for x in range(2,number):
        if number % x == 0:
            that_list.append(x)
            number,that_list = all_numbers(number_that_list)
    else:
        return number,that_list

    
            
whatever()

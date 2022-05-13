def factorial(a,b):

    if a == 1:
        b ='0'
        return b
    elif a == 0:
        b = '1'
        return b
    else:
        for i in range(1, a+1):
            b = b*i
        return b

result = factorial(int(input('enter_number')),1)
print(result)

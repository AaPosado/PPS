def max3():
    if num1 > num2 and num1 > num3:
        if num2 > num3:
            return num1,num2,num3
        else:
            return num1,num3,num2
    elif num2 > num1 and num2 > num3:
        if num1 > num3:
            return num2,num1,num3
        else:
            return num2,num3,num1
    elif num3 > num1 and num3 > num2:
        if num1 > num2:
            return num3,num1,num2
        else:
            return num3,num2,num1


num1 = int(input('Dame un primer número: '))
num2 = int(input('Dame un segundo número: '))
num3 = int(input('Dame un tercer número: '))

print(max3())
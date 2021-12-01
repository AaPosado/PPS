def ma():
    num1 = int(input('Dame un número: '))
    num2 = int(input('Dame un número: '))
    if num1 < num2:
        return num2
    else:
        return num1

print(ma())
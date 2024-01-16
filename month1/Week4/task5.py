

while True:
    try:
        a = int(input("enter number a: "))
        b = int(input("enter number b: "))
    except ValueError:
        print("number must be integer")
        continue
    
    try:
        print(a/b)
    except ZeroDivisionError:
        print("b must be different from 0")
    else:
        break

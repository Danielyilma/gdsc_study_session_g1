
while True:
    try:
        a = int(input("enter a number: "))
        b = int(input("enter a number: "))
    except ValueError:
        print("The number must be integer")
    else:
        print(f"a + b is {a + b}")
        break

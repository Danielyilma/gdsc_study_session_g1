
sum, count = 0, 0
for i in range(1, 51):
    sum += i

    if sum % 3 == 0:
        count += 1
        print("Three", end="")
    elif sum % 5 == 0:
        count += 1
        print("Five", end="")
    else:
        print(sum, end="")
    if i != 50:
        print(end=", ")

print(f"\nsum : {sum}, count of divisiblity: {count}")

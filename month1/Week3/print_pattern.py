
vowel = ['a','e','i','o','u']
while True:
    char = input("Please enter the patttern to be printed: ")
    if len(char) != 1:
        print("length should be one")
        continue
    if char.lower() in vowel:
        print("char should not be vowel")
        continue

    for i in range(1, 6):
        for j in range(0, i):
            print(char, end="")
        print()
    break

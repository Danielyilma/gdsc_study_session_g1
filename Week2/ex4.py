

print("enter your full name")

name = str(input())

print(len(name))
print(name.upper())

print(name.find("smith"))

if name.find("smith") != -1:
    print("sub string found")
else:
    print("sub string not found")


def greet(person):
    print("hello", person)

def add_numbers(a, b):
    return a + b

def print_args(*args):
    print(args)


name = input("enter your name: ")
greet(name)

a = int(input("enter a number: "))
b = int(input("enter a number: "))
print(add_numbers(a, b))

print_args("hello", name)


list1 = [1, 2 , 3, 4, 5, 6]

res = list(filter(lambda x : x % 2 == 0, list1))
double = list(map(lambda x: 2 * x, list1))

print(res)
print(double)
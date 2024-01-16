

def calc_ave(*args):
    sum = 0
    for i in args:
        sum += i
    print(sum/len(args))



calc_ave(1,5,10)

fun = lambda x,y:x + y
fun2 = lambda x: x ** 2
fun3 = lambda x : True if x % 2 == 0 else False


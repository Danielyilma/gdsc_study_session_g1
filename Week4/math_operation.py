
#A
def basic_operations(a, b):
    result = {"add": a + b,
              "sub": a - b,
              "mul": a * b,
              "div": a // b
              }
    return result

#B

def power_opration(base, exponent, **kwargs):
    if kwargs:
        return base % int(kwargs["modulo"])
    else:
        return base ** exponent

#C

def apply_operations(lis_tup):
    result = []

    for fun, val in lis_tup:
            result.append(list(map(fun, (val[0], ), (val[1], ))))
    return result

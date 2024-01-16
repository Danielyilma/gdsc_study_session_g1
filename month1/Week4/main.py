from math_operation import basic_operations, power_opration, apply_operations

# Test basic_operations
result_basic = basic_operations(10, 5)
print("basic Operations Result", result_basic)

#Test power_operations
result_power = power_opration(2, 3)
print("power Operation Result", result_power)

#Test power_operations with modulo
result_power = power_opration(2, 3, modulo=5)
print("power Operation with modulo Result", result_power)

#Test apply_operations
oprations = [
    (lambda x, y: x + y, (3, 4)),
    (lambda x, y: x * y, (2, 5))
]

result_apply = apply_operations(oprations)
print("apply oprations Result", result_apply)
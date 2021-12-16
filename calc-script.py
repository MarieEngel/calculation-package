from calculations.addition import sum_operation
from calculations.absolute import absolute_operation
from calculations.floor import floor_operation
from calculations.power import power_operation

iterable = [15, 4, 23, 8]
sum_iterable = sum_operation(iterable)
print(f"The result of the addition is {sum_iterable}.")


number = -56.78
absolute_number = absolute_operation(number)
print(f"The absolute value of {number} is {absolute_number}.")


floor_number = floor_operation(number)
print(f"The floor of {number} is {floor_number}.")


base = 4
exponent = 3
powered = power_operation(base, exponent)
print(f"The {4} to the power of {exponent} is {powered}.")

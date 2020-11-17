import copy
import math

int_array = [int(i) for i in input("Enter a comma-separated list of integers:\n> ").replace(" ", "").split(sep=",")]

new_array = []

for index in range(len(int_array)):
    copied_array = copy.deepcopy(int_array)
    copied_array.pop(index)
    new_array.append(math.prod(copied_array))

print(new_array)

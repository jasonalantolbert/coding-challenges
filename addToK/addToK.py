import itertools

numbers = [int(x) for x in input("Enter a comma-separated list of numbers:\n> ").replace(" ", "").split(sep=",")]
k_value = int(input("Enter the k-value:\n> "))

solutions = [x for x in itertools.combinations(numbers, r=2) if sum(x) == k_value]

print(bool(solutions))

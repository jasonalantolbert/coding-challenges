def lowest_missing_positive(array):
    for i in range(min([i for i in array if i > 0]), max(array)):
        if i not in array:
            return i

    return max(array) + 1


array = [int(i) for i in input("Enter a comma-separated list of numbers:\n> ").replace(" ", "").split(sep=",")]
print(lowest_missing_positive(array))

import math


def non_adj_sum(ints: list):
    def prohibit(index):
        ints.insert(index, -math.inf)
        ints.pop(index + 1)

    sumnums = []
    while True:
        highest = max(ints)
        if highest == -math.inf:
            break
        high_index = ints.index(highest)
        for index in [i for i in [high_index - 1, high_index, high_index + 1] if 0 <= i < len(ints)]:
            prohibit(index)
        sumnums.append(highest)

    return sum(sumnums)


if __name__ == '__main__':
    ints = [int(i) for i in input("Enter a comma-separated list of integers:\n> ").replace(" ", "").split(",")]
    print(non_adj_sum(ints))

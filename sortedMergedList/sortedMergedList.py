def sort_and_merge(array):
    new_list = []
    for i in array:
        new_list.extend(i)
    return sorted(new_list)


lists = [[1], [1, 3, 5], [1, 10, 20, 30, 40]]
print(sort_and_merge(lists))

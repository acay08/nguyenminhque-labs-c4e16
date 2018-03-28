def get_even_list(lists):
    new_lists = []
    for i in range(len(lists)):
        if lists[i] % 2 == 0:
            new_lists.append(lists[i])
    return new_lists

lists = [1, 2, -1, 4, 8, 9, 10]
new_lists = get_even_list(lists)
print(new_lists)

items = [("product1", 8), ("product2", 7), ("product3", 10)]


def sort_Iteams(item):
    return item[1]


items.sort(key=sort_Iteams)
print("sorted tuple type list:", items)

numbers = [5, 4, 8, 6, 2, 7, 9]
# numbers.sort()
# print("Normal sort:", numbers)

# doses not sort tehe original list:

print(sorted(numbers))

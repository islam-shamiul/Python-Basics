items = [("product1", 8), ("product2", 7), ("product3", 10)]


items.sort(key=lambda items: items[1])
print("sorted tuple type list:", items)

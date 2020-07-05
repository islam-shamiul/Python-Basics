items = [("product1", 12),
         ("product2", 7),
         ("product3", 10)]

x = list(filter(lambda items: items[1] >= 10, items))
print(x)

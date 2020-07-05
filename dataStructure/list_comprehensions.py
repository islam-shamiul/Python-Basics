# syntex:
# [expression for item in item]
items = [("product1", 12),
         ("product2", 7),
         ("product3", 10)]


# x = [items[1] for items in items]
#       |                       |
#       |                       |  
    #expression               itearable
# print(x)

x = [items for items in items if items[1] >= 10]
#        |                 |            |
#        |                 |            |
    #expression         itearable  condition
print(x)

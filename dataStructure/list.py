from collections import deque
fruits=['orange','apple','banana','pear','apple','banana']
print(fruits.count('banana'))
print(fruits.index('banana'))
print(fruits.index('banana',3))
fruits.reverse()
print(fruits)
fruits.append('grape')
print(fruits)
fruits.sort()
print(fruits)
print('-'*40)
#List Comprehensions
squres=[x**2 for x in range(10)]
print(squres)
a=[(x,y) for x in [1,2,3] for y in [3,4,5] if x!=y]
print(a)
print('-'*40)
#list as stacks

stack=[3,4,5]
stack.append(6)
stack.append(7)
print(stack.pop())
print(stack.pop())
print(stack)
print('-'*40)

#list as queues
queue=deque(['war','killings','Jhon'])
queue.append('Rahim')
queue.append('Ram')
print(queue.popleft())
print(queue.popleft())
print(queue)
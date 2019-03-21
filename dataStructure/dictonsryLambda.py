tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
del tel['sape']
print(tel)
print(list(tel))
print(sorted(tel))
a={x:x**2 for x in range(5)}
print(a)
for k,v in a.items():
    print('Key={} :value={}'.format(k,v))
words=['cat','window','defenestrate']
for n in words:
    print(n,len(n))
print('-'*20) 
for w in words[:]:
    if len(w)>6:
        words.insert(0,w)
print(words)
print('-'*20) 
for i in range(5):
    print(i)
print('-'*20)  
for i in range(5,100,5):
    print(i)
print('-'*20) 
a=['Mary', 'had', 'a', 'little', 'lamb']   
for i in range(len(a)):
    print(i,a[i])   
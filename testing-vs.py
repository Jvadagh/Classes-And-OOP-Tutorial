def test():
    a = ['javad','aghajanaloo', 'javad-aghajanloo' , 18 , 19]
    print(a)

test()
items = [ 2,4,5,4,7,4,6,2,5,2]
stats = {}
for i in items: 
    if i in stats:
        stats[i]  +=1
    else:
        stats[i] = 1

print(stats)
A = {11,18,2,3,4,6,8,10}
print(A)
b = [x**2 for x in range(6)]
print(b)

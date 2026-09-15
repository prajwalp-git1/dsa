def find(num,x):
    while num[x]!=x:
        x=num[x]
    return x

num=[0,0,1,3,4,5]
print(find(num,2))
print(find(num,6))
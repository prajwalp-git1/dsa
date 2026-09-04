from collections import deque

def array_rotate(arr, k, direction):
    d=deque(arr)
    if direction=='left':
        d.rotate(-k)
    elif direction=='right':
        d.rotate(k)
    return list(d)


num=[1,2,3,4,5]
print(array_rotate(num,3,'left'))
print(array_rotate(num,2,'right'))
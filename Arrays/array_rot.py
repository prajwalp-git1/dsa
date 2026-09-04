
def array_rotate(arr, d, direction):
    n = len(arr)
    d = d % n  # Handle cases where d >= n

    if direction == 'left':
        return arr[d:] + arr[:d]
    elif direction == 'right':
        return arr[-d:] + arr[:-d]
    else:
        raise ValueError("Direction must be 'left' or 'right'.")

num=[1,2,3,4,5]
print(array_rotate(num, 2, 'left'))
print(array_rotate(num, 2, 'right'))
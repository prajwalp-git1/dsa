def max_subarray_sum(arr):
    max_global = max_current = arr[0]
    for i in arr[1:]:
        max_current = max(i, max_current + i)
        if max_current > max_global:
            max_global = max_current
    return max_global


num=[-2,1,-3,4,-1,2,1,-5,4]
print("Maximum subarray sum is:", max_subarray_sum(num))
def build_prefix_sum(arr):
    pref=[0] * (len(arr)+1)
    for i in range(len(arr)):
        pref[i+1]=pref[i]+arr[i]
    return pref

def range_sum(pref, l, r):
    return pref[r+1]-pref[l]



numbers=[2,4,5,1,3]
prefix_list=build_prefix_sum(numbers)
result=range_sum(prefix_list, 1, 3)
print("Prefix sum array:", prefix_list)
print("Sum of elements from index 1 to 3:", result)
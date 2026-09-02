def create_diff_and_update(arr, updates):
    n=len(arr)
    # Create a difference array initialized to 0
    diff=[0]*(n+1)

    for(l,r,val) in updates:
        diff[l]+=val
        if r+1<n:
            diff[r+1]-=val

    result=[0]*n
    current_val=0
    for i in range(n):
        current_val+=diff[i]
        result[i]=arr[i]+current_val
    return result

arr=[10,20,30,40,50]
my_updates=[[1,3,5]]
new_arr=create_diff_and_update(arr, my_updates)
print("Original array:", arr)
print("Updated array after applying difference array technique:", new_arr)
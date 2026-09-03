#Remove duplicates from a sorted list in-place.

def remove_duplicates(nums):
    if not nums:
        return 0
        
    write = 1 
    for read in range(1, len(nums)):
        if nums[read] != nums[read - 1]:
            nums[write] = nums[read]  
            write += 1               
            
    return write 


duplicate_list = [1, 1, 2, 2, 3, 4, 4]
length = remove_duplicates(duplicate_list)
print(duplicate_list[:length])  

#Find two numbers in a sorted list that add up to a target sum.
def has_target_sum(nums, target):
    # Initialize pointers at opposite ends
    left = 0
    right = len(nums) - 1
    
    while left < right:
        current_sum = nums[left] + nums[right]
        
        if current_sum == target:
            return [nums[left], nums[right]] 
        elif current_sum < target:
            left += 1  
        else:
            right -= 1  
            
    return None 


numbers = [1, 2, 4, 6, 8, 11]
print(has_target_sum(numbers, 10))  
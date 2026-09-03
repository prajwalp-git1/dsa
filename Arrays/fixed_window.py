#Finding the highest sum of 3 numbers in a row.

def max_of_three(nums):
    # Start with the sum of the first 3 numbers
    current_sum = nums[0] + nums[1] + nums[2]
    max_sum = current_sum
    
    # Slide the window across the rest of the list
    for i in range(3, len(nums)):
       
        current_sum = current_sum + nums[i] - nums[i - 3]
        max_sum = max(max_sum, current_sum)
        
    return max_sum


print(max_of_three([1, 2, 3, 4, 1]))

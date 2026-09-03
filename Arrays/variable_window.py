#Find the length of the longest chain of numbers without any duplicates.

def longest_unique_chain(nums):
    seen = set()
    left = 0
    max_len = 0
    
    for right in range(len(nums)):
        # If we see a duplicate, shrink the window from the left
        while nums[right] in seen:
            seen.remove(nums[left])
            left += 1
            
        seen.add(nums[right])
        # Measure how wide the window currently is
        max_len = max(max_len, right - left + 1)
        
    return max_len

print(longest_unique_chain([1, 2, 3, 2, 4])) 

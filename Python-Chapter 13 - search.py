def search(x, nums):
    # binary search
    low = 0
    high = len(nums) - 1
    while low <= high:         # There is still a range to search
        mid = (low + high)//2  # position of middle item
        item = nums[mid]
        if x == item:          # found it! return the index
            return mid
        elif x < item:         # x is in lower half of range
            high = mid - 1     # move top marker down
        else:                  # x is in upper half
            low = mid + 1      # move bottom marker up
    return -1                  # x is not there
    

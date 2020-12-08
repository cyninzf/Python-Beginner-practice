# chapter 13: Binary search

def recBinSearch(x, nums, low, high):
    if low > high:             # no place left to look, return -1
        return -1
    mid = (low + high) // 2
    item = nums[mid]
    if item == x:              # found it! return the index
        return mid
    elif x < item:             # look in lower half
        return recBinSearch(x, nums, low, mid-1)
    else:                      # look in upper half
        return recBinSearch(x, nums, mid+1, high)

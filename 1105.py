def quickSort(nums, begin, end):
    if begin < end:
        pivot = partition(nums, begin, end)
        quickSort(nums, begin, pivot)
        quickSort(nums, pivot+1, end)

def partition(nums, begin, end):
    pivot_index = begin
    pivot = nums[pivot_index]
    l = pivot_index + 1
    r = end - 1

    while True:
        while l <= r and nums[l] < pivot:
            l += 1
        while l <= r and nums[r] >= pivot:
            r -= 1
        if l > r:
            break
        else:
            nums[l], nums[r] = nums[r], nums[l]

    nums[pivot_index], nums[r] = nums[r], nums[pivot_index]
    return r

nums = [4,5,4]
quickSort(nums , 0, len(nums))
print(nums)
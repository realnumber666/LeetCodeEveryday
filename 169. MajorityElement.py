class Solution:
    def partition(self, nums, begin, end):
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

    def quickSort(self, nums: List[int], begin, end) -> List[int]:
        if begin < end:
            pivot = self.partition(nums, begin, end)
            self.quickSort(nums, begin, pivot)
            self.quickSort(nums, pivot + 1, end)

    def majorityElement(self, nums: List[int]) -> int:
        #         dct = {}

        #         for num in nums:
        #             if num not in dct.keys():
        #                 dct[num] = 1
        #             else:
        #                 dct[num] += 1

        #         for key in dct.keys():
        #             if dct[key] > len(nums) // 2:
        #                 return key
        nums.sort()
        return nums[len(nums) // 2]
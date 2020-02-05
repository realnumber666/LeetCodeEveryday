class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #         dct = {}

        #         for n in nums:
        #             if n not in dct.keys():
        #                 dct[n] = 0
        #             else:
        #                 del dct[n]

        #         for n in dct.keys():
        #             return n

        return 2 * sum(set(nums)) - sum(nums)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        sum in window < 0: l = r+1 else r = l
        ---
        判断temp是否为None一定要用if temp is None, 不可以用if temp, 因为中间过程temp可能是0，会影响判断
        '''
        n = len(nums)

        if n == 0:
            return 0

        dp = [0] * n
        dp[0] = nums[0]
        maxSum = dp[0]

        for i in range(1, n):
            dp[i] = max(dp[i - 1], 0) + nums[i]
            maxSum = max(dp[i], maxSum)

        return maxSum


#         l = 0
#         r = 0
#         ret = None
#         temp = None

#         while r < len(nums):
#             temp = temp + nums[r] if temp is not None else nums[0]
#             ret = max(ret, temp) if ret is not None else temp

#             if temp < 0:
#                 temp = 0
#                 l = r + 1
#                 r = l
#             else:
#                 r += 1

#         return ret
'''
solution2
'''
#         if len(nums) == 0:
#             return 0

#         curSum = maxSum = nums[0]

#         for num in nums[1:]:
#             curSum = max(num, curSum+num)
#             maxSum = max(maxSum, curSum)

#         return  maxSum
'''
solution3
'''












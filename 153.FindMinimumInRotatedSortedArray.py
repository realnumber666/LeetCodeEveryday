class Solution:
    def findMin(self, A: List[int]) -> int:
        l = 0
        r = len(A) - 1
        while l < r:
            m = (l + r) // 2
            if A[m] < A[r]:
                r = m
            else:
                l = m + 1

        return A[l]
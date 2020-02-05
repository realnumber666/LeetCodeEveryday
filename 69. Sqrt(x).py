class Solution:
    def mySqrt(self, x: int) -> int:
        '''
        二分法
        找到第一个平方大于x的数字
        这个数字-1就是所要找的
        '''
        if x == 1:
            return 1
        l = 1
        r = x
        while l < r:
            m = l + (r - l) // 2
            ret = m * m
            if ret == x:
                return m
            if ret > x:
                r = m
            else:
                l = m + 1
        if l * l > x:
            return l - 1
        else:
            return l

# -*- coding: UTF-8 -*-
'''
注意min_res定义的位置
如果定义为类变量会有错
因为在小的多边形分割的时候，res一定比原四边形小，会直接覆盖我们想要的值
因此定义在递归函数中，每一层递归之和自己的兄弟作比较

大循环以不同的节点作为起始点
小循环以相同的起始点连接不同的顶点
'''
from collections import deque


class Solution:
    def minScoreTriangulation(self, A) -> int:
        def core(arr):
            min_res = 0
            if (len(arr) == 3):
                return arr[0] * arr[1] * arr[2]

            for j in range(len(arr) - 2):
                for i in range(2, len(arr) - 1):
                    left = arr[0:i + 1]
                    right = arr[i:]
                    r_q = deque(right)
                    r_q.appendleft(arr[0])
                    right = list(r_q)

                    if (min_res == 0):
                        min_res = core(left) + core(right)
                    else:
                        min_res = min(min_res, core(left) + core(right))

                q = deque(arr)
                head = q.popleft()
                q.append(head)
                arr = list(q)
            return min_res

        return core(A)

print(Solution().minScoreTriangulation([3,5,2,5,2,6]))
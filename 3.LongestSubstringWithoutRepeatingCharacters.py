class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # '''
        # 如果是相连的不同的，放进hash表，长度加一
        # 如果相连的相同的，从第二个开始重新计算
        # 维护最大长度
        # '''
        #         ret = 0
        #         s_dict = {}
        #         for i in range(len(s)):
        #             num = 0
        #             for j in range(i, len(s)):
        #                 c = s[j]
        #                 if c not in s_dict.keys():
        #                     s_dict[c] = 0
        #                     num += 1
        #                 else:
        #                     ret = max(num, ret)
        #                     s_dict.clear()
        #                     break
        #                 ret = max(num, ret)

        #         return ret

        '''
        如果下一个重复，更新左边界为index+1的位置，并且更新该重复元素在哈希表的index值
        若下一个不重复，存进哈希表，更新最大值
        '''
        max_so_far = 0
        i = j = 0
        s_dict = {}
        while j < len(s):
            c = s[j]
            if c not in s_dict.keys():
                s_dict[c] = j
            else:
                i = max(s_dict[c] + 1, i)
                s_dict[c] = j
            max_so_far = max(max_so_far, j - i + 1)
            j += 1

        return max(max_so_far, j - i)
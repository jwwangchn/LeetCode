#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现strStr()
#
# https://leetcode-cn.com/problems/implement-strstr/description/
#
# algorithms
# Easy (37.42%)
# Total Accepted:    34.9K
# Total Submissions: 93.2K
# Testcase Example:  '"hello"\n"ll"'
#
# 实现 strStr() 函数。
# 
# 给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置
# (从0开始)。如果不存在，则返回  -1。
# 
# 示例 1:
# 
# 输入: haystack = "hello", needle = "ll"
# 输出: 2
# 
# 
# 示例 2:
# 
# 输入: haystack = "aaaaa", needle = "bba"
# 输出: -1
# 
# 
# 说明:
# 
# 当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
# 
# 对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。
# 
#
class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        else:
            first_needle_str = needle[0]
            needle_len = len(needle)
            haystack_len = len(haystack)
            current_point = 0
            for idx, haystack_str in enumerate(haystack):
                if haystack_str == first_needle_str:
                    if idx + needle_len <= haystack_len:
                        if haystack[idx:idx + needle_len] == needle:
                            return idx
                        else:
                            continue
                    else:
                        return -1
                else:
                    continue
            return -1
        
if __name__ == '__main__':
    haystack = "mississippi"
    needle = "issip"
    solution = Solution()
    results = solution.strStr(haystack, needle)
    print(results)
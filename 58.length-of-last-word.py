#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#
# https://leetcode-cn.com/problems/length-of-last-word/description/
#
# algorithms
# Easy (28.52%)
# Total Accepted:    16.5K
# Total Submissions: 57.8K
# Testcase Example:  '"Hello World"'
#
# 给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。
# 
# 如果不存在最后一个单词，请返回 0 。
# 
# 说明：一个单词是指由字母组成，但不包含任何空格的字符串。
# 
# 示例:
# 
# 输入: "Hello World"
# 输出: 5
# 
# 
#
class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        str_len = len(s)
        s = ' ' + s + ' '
        front_space = 0
        back_space = 0
        idx = 1
        while True:
            if idx > str_len:
                break
            else:
                if s[idx] != ' ':
                    if s[idx - 1] == ' ':
                        front_space = idx - 1
                    if s[idx + 1] == ' ':
                        back_space = idx
                idx += 1

        return back_space - front_space

if __name__ == '__main__':
    s = "Hello World"
    solution = Solution()
    results = solution.lengthOfLastWord(s)
    print(results)

#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#
# https://leetcode-cn.com/problems/palindrome-number/description/
#
# algorithms
# Easy (55.90%)
# Total Accepted:    66.5K
# Total Submissions: 118.9K
# Testcase Example:  '121'
#
# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
# 
# 示例 1:
# 
# 输入: 121
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: -121
# 输出: false
# 解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
# 
# 
# 示例 3:
# 
# 输入: 10
# 输出: false
# 解释: 从右向左读, 为 01 。因此它不是一个回文数。
# 
# 
# 进阶:
# 
# 你能不将整数转为字符串来解决这个问题吗？
# 
#
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        nums = []
        new_num = x
        while True:
            last_num = new_num % 10
            new_num = new_num // 10
            nums.append(last_num)
            if new_num == 0:
                break
        while True:
            idx = 0
            if len(nums) <= 1:
                return True
            first_num = nums.pop(idx)
            last_num = nums.pop(len(nums) - 1)
            if first_num == last_num:
                continue
            else:
                return False

if __name__ == '__main__':
    solution = Solution()
    x = 121
    result = solution.isPalindrome(x)
    print(result)
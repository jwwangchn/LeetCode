#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#
# https://leetcode-cn.com/problems/reverse-integer/description/
#
# algorithms
# Easy (31.34%)
# Total Accepted:    77.5K
# Total Submissions: 247.3K
# Testcase Example:  '123'
#
# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
# 
# 示例 1:
# 
# 输入: 123
# 输出: 321
# 
# 
# 示例 2:
# 
# 输入: -123
# 输出: -321
# 
# 
# 示例 3:
# 
# 输入: 120
# 输出: 21
# 
# 
# 注意:
# 
# 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
# 
#
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        neg_flag = False
        
        if x < 0:
            neg_flag = True
            x = abs(x)
        temp_x = x
        nums = []
        
        while True:
            last_num = temp_x % 10
            temp_x = temp_x // 10
            nums.append(last_num)
            if temp_x == 0:
                break
        new_num = 0
        
        for idx in range(len(nums)):
            new_num = new_num + nums[len(nums) - 1 - idx] * 10**idx
        
        if new_num < -2**31 or new_num > 2**31 - 1:
            return 0
        
        if neg_flag:
            new_num = -new_num
        return new_num

if __name__ == '__main__':
    solution = Solution()
    x = 1534236469
    result = solution.reverse(x)
    print(result)
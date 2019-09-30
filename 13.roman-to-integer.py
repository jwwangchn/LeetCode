#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#
# https://leetcode-cn.com/problems/roman-to-integer/description/
#
# algorithms
# Easy (56.40%)
# Total Accepted:    37.1K
# Total Submissions: 65.9K
# Testcase Example:  '"III"'
#
# 罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。
# 
# 字符          数值
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# 
# 例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V +
# II 。
# 
# 通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5
# 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：
# 
# 
# I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
# X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
# C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
# 
# 
# 给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。
# 
# 示例 1:
# 
# 输入: "III"
# 输出: 3
# 
# 示例 2:
# 
# 输入: "IV"
# 输出: 4
# 
# 示例 3:
# 
# 输入: "IX"
# 输出: 9
# 
# 示例 4:
# 
# 输入: "LVIII"
# 输出: 58
# 解释: L = 50, V= 5, III = 3.
# 
# 
# 示例 5:
# 
# 输入: "MCMXCIV"
# 输出: 1994
# 解释: M = 1000, CM = 900, XC = 90, IV = 4.
# 
#
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman2int_dict = {'I':1, 'V':5, "X":10, "L":50, 'C':100, 'D':500, "M":1000, 'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM': 900}
        roman_strs = [_ for _ in s]
        new_roman_strs = []
        
        idx = 0
        while True:
            if idx > len(roman_strs)-1:
                break
            s = roman_strs[idx]
            if s == 'I' and idx != len(roman_strs) - 1:
                if roman_strs[idx+1] == 'V':
                    new_roman_strs.append('IV')
                    idx = idx + 2
                    continue
                if roman_strs[idx+1] == 'X':
                    new_roman_strs.append('IX')
                    idx = idx + 2
                    continue
            if s == 'X' and idx != len(roman_strs) - 1:
                if roman_strs[idx+1] == 'L':
                    new_roman_strs.append('XL')
                    idx = idx + 2
                    continue
                if roman_strs[idx+1] == 'C':
                    new_roman_strs.append('XC')
                    idx = idx + 2
                    continue
            if s == 'C' and idx != len(roman_strs) - 1:
                if roman_strs[idx+1] == 'D':
                    new_roman_strs.append('CD')
                    idx = idx + 2
                    continue
                if roman_strs[idx+1] == 'M':
                    new_roman_strs.append('CM')
                    idx = idx + 2
                    continue
            
            new_roman_strs.append(s)
            idx = idx + 1
        num = 0
        for idx, value in enumerate(new_roman_strs):
            num = num + roman2int_dict[value]
        return num
        
if __name__ == '__main__':
    solution = Solution()
    s = 'MCMXCIV'
    result = solution.romanToInt(s)
    print(result)
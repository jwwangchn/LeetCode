#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#
# https://leetcode-cn.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (36.13%)
# Total Accepted:    43.5K
# Total Submissions: 120.2K
# Testcase Example:  '"()"'
#
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
# 
# 有效字符串需满足：
# 
# 
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 
# 
# 注意空字符串可被认为是有效字符串。
# 
# 示例 1:
# 
# 输入: "()"
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: "()[]{}"
# 输出: true
# 
# 
# 示例 3:
# 
# 输入: "(]"
# 输出: false
# 
# 
# 示例 4:
# 
# 输入: "([)]"
# 输出: false
# 
# 
# 示例 5:
# 
# 输入: "{[]}"
# 输出: true
# 
#
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "":
            return True
        else:
            left = ['(', "{", "[", '"', "'"]
            right = [')', "}", "]", '"', "'"]
            valid_dict = {"(":")", "[":"]", "{":"}", "'":"'", '"':'"'}
            idx = 0
            str_len = len(s)
            find_right = False
            while True:
                if idx >= str_len:
                    break
                current_value = s[idx]
                if current_value in right:
                    find_right = True
                    if idx == 0:
                        return False
                    else:
                        left_value = s[idx - 1]
                        if valid_dict[left_value] == current_value:
                            s = s[:idx] + s[idx+1:]
                            s = s[:idx-1] + s[idx:]
                            idx=0
                            str_len = len(s)
                            find_right = False
                        else:
                            return False
                else:
                    idx += 1
            if len(s) != 0 and find_right == False:
                return False
        return True
        
if __name__ == '__main__':
    solution = Solution()
    s = '()'
    result = solution.isValid(s)
    print(result)
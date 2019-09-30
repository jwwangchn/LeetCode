#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
# https://leetcode-cn.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (31.55%)
# Total Accepted:    47.9K
# Total Submissions: 151.9K
# Testcase Example:  '["flower","flow","flight"]'
#
# 编写一个函数来查找字符串数组中的最长公共前缀。
# 
# 如果不存在公共前缀，返回空字符串 ""。
# 
# 示例 1:
# 
# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 
# 
# 示例 2:
# 
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
# 
# 
# 说明:
# 
# 所有输入只包含小写字母 a-z 。
# 
#
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        
        ref_str = strs[0]

        common_str = ''
        for idx, s in enumerate(ref_str):
            for str_ in strs:
                if len(str_) < idx + 1:
                    return common_str

                if s == str_[idx]:
                    continue
                else:
                    if idx == 0:
                        return ""
                    else:
                        return common_str
            common_str = common_str + s
        return common_str


if __name__ == '__main__':
    solution = Solution()
    strs = ["",""]
    result = solution.longestCommonPrefix(strs)
    print(result)
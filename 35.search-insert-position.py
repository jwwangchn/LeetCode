#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#
# https://leetcode-cn.com/problems/search-insert-position/description/
#
# algorithms
# Easy (42.39%)
# Total Accepted:    27.9K
# Total Submissions: 65.7K
# Testcase Example:  '[1,3,5,6]\n5'
#
# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
# 
# 你可以假设数组中无重复元素。
# 
# 示例 1:
# 
# 输入: [1,3,5,6], 5
# 输出: 2
# 
# 
# 示例 2:
# 
# 输入: [1,3,5,6], 2
# 输出: 1
# 
# 
# 示例 3:
# 
# 输入: [1,3,5,6], 7
# 输出: 4
# 
# 
# 示例 4:
# 
# 输入: [1,3,5,6], 0
# 输出: 0
# 
# 
#
class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target <= nums[0]:
            return 0
        for idx, value in enumerate(nums):
            if idx == len(nums) - 1:
                if target == value:
                    return idx
                else:
                    return idx + 1
            else:
                if value == target:
                    return idx
                else:
                    if value < target and nums[idx+1] > target:
                        return idx + 1
                    else:
                        continue



# if __name__ == '__main__':
#     nums = [1,3,5,6]
#     target = 7
#     solution = Solution()
#     results = solution.searchInsert(nums, target)
#     print(results)
        

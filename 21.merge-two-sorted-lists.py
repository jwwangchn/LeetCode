#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#
# https://leetcode-cn.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (52.00%)
# Total Accepted:    41.1K
# Total Submissions: 79K
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
# 
# 示例：
# 
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

if __name__ == '__main__':
    l1 = ListNode(1)
    l1_2 = ListNode(2)
    l1_3 = ListNode(4)
    l1.next = l1_2
    l1_2.next = l1_3

    l2 = ListNode(1)
    l2_2 = ListNode(3)
    l2_3 = ListNode(4)
    l2.next = l2_2
    l2_2.next = l2_3

    solution = Solution()
    result = solution.mergeTwoLists(l1, l2)
    print(result)

#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# @lc code=start
# Definition for singly-linked list.


class Solution:
    # 递推解
    def addTwoNumbers(
        self,
        l1: Optional[ListNode],
        l2: Optional[ListNode],
        lr: Optional[ListNode] = None,
    ) -> Optional[ListNode]:
        l1 = l1 if l1 else ListNode(0)
        l2 = l2 if l2 else ListNode(0)
        lr = lr if lr else ListNode(0)

        r = l1.val + l2.val
        if lr.val + r < 10:
            lr.val += r
            lr.next = ListNode(0)
        else:
            lr.val += r - 10
            lr.next = ListNode(1)

        if l1.next is None and l2.next is None and lr.next.val == 0:
            lr.next = None
            return lr
        else:
            lr.next = self.addTwoNumbers(
                l1.next,
                l2.next,
                lr.next,
            )
            return lr

    # 迭代解
    # def addTwoNumbers(
    #     self,
    #     l1: Optional[ListNode],
    #     l2: Optional[ListNode],
    # ) -> Optional[ListNode]:
    #     dummy = ListNode(0)
    #     current = dummy
    #     carry = 0
    #     while l1 or l2 or carry:
    #         val1 = l1.val if l1 else 0
    #         val2 = l2.val if l2 else 0
    #         total = val1 + val2 + carry
    #         carry = total // 10
    #         current.next = ListNode(total % 10)
    #         current = current.next
    #         if l1:
    #             l1 = l1.next
    #         if l2:
    #             l2 = l2.next
    #     return dummy.next


# @lc code=end

if __name__ == "__main__":
    solution = Solution()

    ans = solution.addTwoNumbers(
        ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))),
        ListNode(9, ListNode(9, ListNode(9))),
    )

    print(ans)

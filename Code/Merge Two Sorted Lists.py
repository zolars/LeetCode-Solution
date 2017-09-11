# Merge Two Sorted Lists
# Definition for singly-linked list.


class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self is None:
            return "Nil"
        else:
            return "{} -> {}".format(self.val, repr(self.next))


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        list = []
        while l1:
            list.append(l1.val)
            l1 = l1.next
        while l2:
            list.append(l2.val)
            l2 = l2.next

        list = sorted(list)

        right = None
        for i in list[::-1]:
            left = ListNode(i)
            left.next = right
            right = left

        return right


if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(4)

    l2 = ListNode(3)
    l2.next = ListNode(4)
    l2.next.next = ListNode(5)
    l2.next.next.next = ListNode(6)
    print(Solution().mergeTwoLists(l1, l2))

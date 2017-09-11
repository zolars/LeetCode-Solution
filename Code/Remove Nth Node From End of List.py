# Remove Nth Node From End of List
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
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        ans = ListNode(-1)
        ans.next = head
        left, right = ans, ans

        for i in xrange(n):
            right = right.next

        while right.next:
            right = right.next
            left = left.next

        left.next = left.next.next

        return ans.next


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    print Solution().removeNthFromEnd(head, 5)

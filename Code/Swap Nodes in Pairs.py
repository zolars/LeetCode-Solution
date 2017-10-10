# Swap Nodes in Pairs
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
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        ans = ListNode(-1)
        temp = ans
        while True:
            if head:
                right = head.val
            else:
                break

            if head.next:
                left = head.next.val
                temp.next = ListNode(left)
                temp.next.next = ListNode(right)
                temp = temp.next.next
                head = head.next.next

            else:
                temp.next = ListNode(right)
                break
        return ans.next


if __name__ == '__main__':
    lists = [1, 2, 3, 4, 5, 6]

    r = None
    for i in reversed(lists):
        l = ListNode(i)
        l.next = r
        r = l

    print Solution().swapPairs(r)

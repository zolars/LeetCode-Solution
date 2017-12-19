# Reverse Nodes in k-Group
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
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        nums = []
        while head.next != None:
            nums.append(head.val)
            head = head.next
        else:
            nums.append(head.val)

        for i in xrange(len(nums) / k):
            temp = nums[
                (i + 1) * k - 1:
                i * k - 1 if i * k != 0 else None:
                -1
            ]
            nums = nums[:i * k] + temp + nums[(i + 1) * k:]

        ans = ListNode(nums[-1])
        for i in nums[-2::-1]:
            temp = ListNode(i)
            temp.next = ans
            ans = temp

        return ans


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)
    head.next.next.next.next.next.next = ListNode(7)
    head.next.next.next.next.next.next.next = ListNode(8)
    head.next.next.next.next.next.next.next.next = ListNode(9)
    print Solution().reverseKGroup(head, 2)

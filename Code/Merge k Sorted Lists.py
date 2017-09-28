# Merge k Sorted Lists
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
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if lists == []:
            return 0

        list = []
        for num, i in enumerate(lists):
            while i:
                list.append(i.val)
                i = i.next

        list = sorted(list)

        right = None
        for i in list[::-1]:
            left = ListNode(i)
            left.next = right
            right = left

        return right


if __name__ == '__main__':
    list1 = ListNode(1)
    list1.next = ListNode(3)
    list1.next.next = ListNode(6)
    list2 = ListNode(2)
    list2.next = ListNode(4)
    list3 = ListNode(2)
    list3.next = ListNode(4)

    print Solution().mergeKLists([list1, list3])

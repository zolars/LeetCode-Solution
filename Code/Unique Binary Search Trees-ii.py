# Unique Binary Search Trees-ii
# Definition for a  binary tree node


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        if self:
            serial = []
            queue = [self]

            while queue:
                cur = queue[0]

                if cur:
                    serial.append(cur.val)
                    queue.append(cur.left)
                    queue.append(cur.right)
                else:
                    serial.append("#")

                queue = queue[1:]

            while serial[-1] == "#":
                serial.pop()

            return repr(serial)

        else:
            return None


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.generateTreesDo(1, n)

    def generateTreesDo(self, l, r):
        """
        :type left: int
        :type right: int
        :rtype: List[TreeNode]
        """
        result = []
        if l > r:
            result.append(None)
        for i in xrange(l, r + 1):
            left = self.generateTreesDo(l, i - 1)
            right = self.generateTreesDo(i + 1, r)
            for j in left:
                for k in right:
                    temp = TreeNode(i)
                    temp.left = j
                    temp.right = k
                    result.append(temp)

        return result


if __name__ == "__main__":
    print Solution().generateTrees(2)

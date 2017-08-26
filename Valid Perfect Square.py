# Valid Perfect Square


class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        i = 0
        j = 1
        while i < num:
            if i + j == num:
                return(True)
            elif i + j > num:
                return(False)
            else:
                i = i + j
                j = j + 2


if __name__ == '__main__':
    print(Solution().isPerfectSquare(257))

# Compare Version Numbers


class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = []
        v2 = []

        left = 0
        for i, char in enumerate(version1):
            right = i
            if char == '.':
                v1.append(int(version1[left:right]))
                left = i + 1
        else:
            v1.append(int(version1[left:]))

        left = 0
        for i, char in enumerate(version2):
            right = i
            if char == '.':
                v2.append(int(version2[left:right]))
                left = i + 1
        else:
            v2.append(int(version2[left:]))

        l = min(len(v1), len(v2))
        for i in xrange(l):
            if v1[i] > v2[i]:
                return(1)
            elif v1[i] < v2[i]:
                return(-1)
        else:
            if sum(v1) > sum(v2):
                return(1)
            elif sum(v1) < sum(v2):
                return(-1)
            else:
                return(0)


if __name__ == '__main__':
    print(Solution().compareVersion('1.2', '1.2.0'))

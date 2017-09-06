class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == [] or len(strs) == 1:
            strs.append('')
            return strs[0]

        for i in xrange(len(strs)):
            strs[i] += '*'

        ans, n = '', 0
        while True:
            temp = strs[0][n]
            for i in strs[1:]:
                if i[n] != temp or n == len(i) - 1:
                    return ans

            ans += temp
            n += 1


if __name__ == '__main__':
    print(Solution().longestCommonPrefix(["1111"]))

#  Longest Palindromic Substring


class Solution(object):
    def longestPalindrome1(self, s):
        """
        Method_one : Dynamic Programming
        :type s: str
        :rtype: str
        """
        global dic
        dic = {}

        def find(s, i, j):
            """
            :type s: str
            :type i: int
            :rtype: str
            """
            if j == len(s) - 1:
                dic[len(s[i:j + 1])] = s[i:j + 1]
                return

            if i == 0 and i != j:
                dic[len(s[i:j + 1])] = s[i:j + 1]
                return

            lookup = {len(s[i:j + 1]): s[i:j + 1]}
            if i == j and s[i] == s[j + 1]:
                find(s, i, j + 1)
            if s[i - 1] == s[j + 1]:
                find(s, i - 1, j + 1)
            else:
                dic[len(s[i:j + 1])] = s[i:j + 1]
                return

        for i in range(len(s)):
            find(s, i, i)

        return(dic[sorted(dic.keys())[-1]])

    def longestPalindrome2(self, s):
        """
        Method_two : Expand Around Center
        :type s: str
        :rtype: str
        """
        global dic
        dic = {}

        def find(s, i, j):
            """
            :type s: str
            :type i: int
            :rtype: str
            """
            while(i >= 0 and j < len(s) and s[i] == s[j]):
                i -= 1
                j += 1
            dic[j - i - 1] = s[i + 1:j]

        for i in range(len(s)):
            find(s, i, i)
            find(s, i, i + 1)
        return(dic[sorted(dic.keys())[-1]])


if __name__ == "__main__":
    print(Solution().longestPalindrome1("cbbd"))

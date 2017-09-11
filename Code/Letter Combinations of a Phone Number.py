# Letter Combinations of a Phone Number


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == '':
            return []

        dic = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        ans, lenght = [''], 1
        for i in digits:
            for j in xrange(len(ans)):
                for k in dic[i]:
                    ans.append(ans[j] + k)
            lenght *= len(dic[i])

        return ans[len(ans) - lenght:]


if __name__ == '__main__':
    print(Solution().letterCombinations("234"))

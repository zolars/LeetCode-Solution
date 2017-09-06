# Roman to Integer


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        ans = 0
        for i in range(len(s)):
            if i == len(s) - 1 or dic[s[i + 1]] <= dic[s[i]]:
                ans += dic[s[i]]
            else:
                ans += (-1) * dic[s[i]]

        return(ans)


if __name__ == '__main__':
    print(Solution().romanToInt('DCXXI'))

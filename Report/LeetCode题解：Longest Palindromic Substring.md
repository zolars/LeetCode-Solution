# LeetCode题解：Longest Palindromic Substring

## 题目

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

-   Example

    Input: "babad"
    Output: "bab"
    Note: "aba" is also a valid answer.

    Input: "cbbd"
    Output: "bb"

## 题解

本题解法众多，是处理字符串相关问题的基础。

### Dynamic Programming

动态规划算法，使用函数的递归来实现，AC。

### Expand Around Center

由中心向外边拓展边判断，这个比动态规划要快，因为减少了函数调用。

### Manacher's Algorithm

[详解](http://blog.csdn.net/zzran/article/details/8517653)

### 重要的优化

设一个字典为全局变量，将所有检索到的符合条件的字符串及其长度放入该字典。之后对字典排序后输出即可，可以减小复杂度。

## 代码

```python
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
```

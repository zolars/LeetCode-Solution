# LeetCode题解: Scramble String

## 题目

Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

        great
       /    \
      gr    eat

     / \    /  \
    g   r  e   at
               / \
              a   t

To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

        rgeat

       /    \
      rg    eat
     / \    /  \
    r   g  e   at
               / \
              a   t

We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

        rgtae
       /    \
      rg    tae
     / \    /  \
    r   g  ta  e
           / \
          t   a

We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.

## 题解

DP经典问题, 目前我真的想不出做法, 只好看大神的代码了.

那么让我们来分析一下:

首先, DP的想法是"将复杂的问题分散成简单的小问题", 可以想到一开始应当判断短子串是否为Scramble String(拼凑字符串). 举例说明, 看下面两个字符串:

"great", "rgtae"

将每个字符串先转化为长度为1的五个子串, 并在两组字符串中建立一一匹配关系. 下表中"1"代表匹配, "0"代表失配.

    [0, 1, 0, 0, 0]  

    [1, 0, 0, 0, 0]  

    [0, 0, 0, 0, 1]  

    [0, 0, 0, 1, 0]  

    [0, 0, 1, 0, 0]

之后将这个关系运用至n长度. 则我们有状态转移方程:

    (ans[k][i][j] and ans[n - k][i + k][j + k])
    or
    (ans[k][i][j + n - k] and ans[n - k][i + k][j])

从i, j开始, 在其后寻找n个元素
将(i, i+n), (j, j+n)的遍历分割为双区间
图例:

    ----------------------------------------------
    [1]:
    1   2   3   4   5   6   7   8   9  10 11 12 13
        i       i+k             i+n
                    j       j+k             j+n

    [2]:
    1   2   3   4   5   6   7   8   9  10 11 12 13
        i       i+k             i+n
                    i               j+n-k   i+n

    ----------------------------------------------

这样运行下去, 复杂度为O(n^4).

## 代码

```python
class Solution:
    # @return a boolean
    def isScramble(self, s1, s2):

        if not s1 or not s2 or len(s1) != len(s2):
            return False
        if s1 == s2:
            return True

        l = len(s1)

        ans = [[[False for j in xrange(l)] for i in xrange(l)]
               for n in xrange(l + 1)]

        for i in xrange(l):
            for j in xrange(l):
                if s1[i] == s2[j]:
                    ans[1][i][j] = True

        for n in xrange(2, l + 1):
            for i in xrange(l - n + 1):
                for j in xrange(l - n + 1):
                    for k in xrange(1, n):

                        if (ans[k][i][j] and ans[n - k][i + k][j + k]) or (ans[k][i][j + n - k] and ans[n - k][i + k][j]):
                            ans[n][i][j] = True
                            break

        for i in ans:
            print "---"
            for j in i:
                print " ", j, " "
                print

        return ans[n][0][0]


if __name__ == "__main__":
    s1, s2 = "great", "rgtae"
    print Solution().isScramble(s1, s2)
```

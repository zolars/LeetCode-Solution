# LeetCode题解：Climbing Stairs

## 题目

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

## 题解

这是一道经典的DP.

我起初做这题的时候, 自然想到了从顶端向下遍历, 但是会TLE. 这是就应当出现从底端向上遍历的想法了: 但是如何呢?

状态转移方程: dp[n]=dp[n-1]+dp[n-2]

看着很眼熟啊? 这不是斐波那契数列吗...

# 代码

```python
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1

        dp = [0 for i in xrange(n)]
        dp[0], dp[1] = 1, 2

        for i in xrange(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[-1]


if __name__ == '__main__':
    print(Solution().climbStairs(200))
```

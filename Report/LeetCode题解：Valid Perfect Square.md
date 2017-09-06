# LeetCode题解：Valid Perfect Square
## 题目
Given a positive integer num, write a function which returns True if num is a perfect square else False.
Note: Do not use any built-in library function such as sqrt.

* Example
Input: 16
Returns: True

## 题解
这是一道数学题：
1 + 3 + 5 + … + (2 * n - 1) = (1 + (2 * n - 1)) * n / 2 = n ^ 2
所以只需要遍历上述式子即可。
时间复杂度为：O(sqrt(n))

## 代码
```python
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
    print(Solution().isPerfectSquare(256))

```


#code/leetcode

# LeetCode题解：Longest Valid Parentheses
## 题目
Given a string containing just the characters`’(‘`and`’)’`, find the length of the longest valid (well-formed) parentheses substring.

* Example
For`“(()”`, the longest valid parentheses substring is`”()”`, which has length = 2.
Another example is`")()())"`, where the longest valid parentheses substring is`"()()"`, which has length = 4.

## 题解
基础的堆栈问题——回文字符串。
第一种方法是没有任何优化的栈模型，先将整体字符串整理为可观察数组，再通过该数组来判断连续子串的长度。超时。
第二种方法，在出栈时统一测量长度即可。

## 代码
```python
class Solution(object):
    def longestValidParentheses1(self, s):
        """
        Method_one
        :type s: str
        :rtype: int
        """
        pen = [-1] * len(s)
        left = 0
        for i in xrange(len(s)):
            if s[i] == '(':
                pen[i] += 1
            elif s[i] == ')':
                for j in range(i + 1)[::-1]:
                    if pen[j] == 0:
                        pen[j] += 1
                        pen[i] += 2
                        break
                else:
                    left = i
        lenght, maxlenght = 0, 0
        for i in pen:
            if i == -1 or i == 0:
                lenght = 0
            else:
                lenght += 1
                maxlenght = max(maxlenght, lenght)
        return(maxlenght)

    def longestValidParentheses2(self, s):
        """
        Method_two:Stacks
        :type s: str
        :rtype: int
        """
        stack = [-1]
        lenght, maxlenght = 0, 0
        for i, char in enumerate(s):
            if char == ')':
                if len(stack) == 1:
                    lenght = 0
                    stack[0] = i
                else:
                    stack.pop()
                    lenght = i - stack[-1]
                    maxlenght = max(maxlenght, lenght)
            else:
                stack.append(i)
        return(maxlenght)


if __name__ == '__main__':
    # print(Solution().longestValidParentheses1("()"))
    print(Solution().longestValidParentheses2("()"))
```


#code/leetcode
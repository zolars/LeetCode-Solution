# LeetCode题解：Regular Expression Matching

## 题目

Implement regular expression matching with support for`'.'`and`'*'`.

`'.'`Matches any single character. `'*'`Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be: bool isMatch(const char \*s, const char \*p)

-   Example

    isMatch("aa","a") → false isMatch("aa","aa") → true isMatch("aaa","aa") → false isMatch("aa", "a\*") → true isMatch("aa", ".\*") → true isMatch("ab", ".\*") → true isMatch("ab", "c\*ab") → true

## 题解

类似于正则表达式的匹配，但是题目有点坑：

1.  第一行字符串不会含有`'.'`和`'*'`，否则难度直线飙升。
2.  这里面的`'*'`是可以匹配0个字符的啊！开始没注意，白敲半小时。

那么这题的正确做法是什么呢？很明显是DP的递归，但是有很多边界要想清楚。一开始做这题就死在了边界上。

重要的优化：看了大神的代码，发现不需要单独判断尽头，可以一边走一边判断。

## 代码

```python
# -*- coding: utf-8 -*-
class Solution(object):
    def isMatch1(self, ss, pp):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # 预处理
        global s, p
        s = ss + '\n'
        p = pp + '\n'

        def match(sn, pn):
            if p[pn] == '\n':
                return s[sn] == '\n'

            else:
                if len(p) - pn == 1 or p[pn + 1] != "*":
                    if len(s) - 1 > sn and (s[sn] == p[pn] or p[pn] == '.'):
                        return match(sn + 1, pn + 1)
                    else:
                        return False
                else:
                    while sn < len(s) - 1 and (s[sn] == p[pn] or p[pn] == '.'):
                        if match(sn, pn + 2):
                            return True
                        else:
                            sn += 1
                    else:
                        return match(sn, pn + 2)

        return match(0, 0)

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
            return not s

        if len(p) == 1 or p[1] != '*':
            if len(s) > 0 and (p[0] == s[0] or p[0] == '.'):
                return self.isMatch(s[1:], p[1:])
            else:
                return False

        else:
            while len(s) > 0 and (p[0] == s[0] or p[0] == '.'):
                if self.isMatch(s, p[2:]):
                    return True
                s = s[1:]
            return self.isMatch(s, p[2:])


if __name__ == '__main__':
    print(Solution().isMatch("aab", "a*c*a*ab"))
```

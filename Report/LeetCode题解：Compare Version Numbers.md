# LeetCode题解：Compare Version Numbers

## 题目

Compare two version numbers version1 and version2. If version1 > version2 return 1, if version1 &lt; version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character. The `.` character does not represent a decimal point and is used to separate number sequences. For instance, `2.5` is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

-   Example `0.1 < 1.1 < 1.2 < 13.37`

## 题解

字符串切片的运用，简单题。

## 代码

```python
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = []
        v2 = []

        left = 0
        for i, char in enumerate(version1):
            right = i
            if char == '.':
                v1.append(int(version1[left:right]))
                left = i + 1
        else:
            v1.append(int(version1[left:]))

        left = 0
        for i, char in enumerate(version2):
            right = i
            if char == '.':
                v2.append(int(version2[left:right]))
                left = i + 1
        else:
            v2.append(int(version2[left:]))

        l = min(len(v1), len(v2))
        for i in xrange(l):
            if v1[i] > v2[i]:
                return(1)
            elif v1[i] < v2[i]:
                return(-1)
        else:
            if sum(v1) > sum(v2):
                return(1)
            elif sum(v1) < sum(v2):
                return(-1)
            else:
                return(0)


if __name__ == '__main__':
    print(Solution().compareVersion('1.2', '1.2.0'))
```

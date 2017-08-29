# LeetCode题解：Longest Substring
## 题目
### Without Repeating Characters
Given a string, find the length of the longest substring without repeating characters.

* Example
Given`"abcabcbb"`, the answer is `"abc"`, which the length is 3.
Given`"bbbbb"`, the answer is `"b"`, with the length of 1.
Given `"pwwkew"`, the answer is `"wke"`, with the length of 3. Note that the answer must be a substring,`"pwke"` is a subsequence and not a substring.

### With At Most K Distinct Characters
Given a string, find the length of the longest substring T that contains at most k distinct characters.

* Example
Given`s = "eceba"`, `k = 2`, The answer is`"ece"`, which the length is 3.

## 题解
使用队列的两道经典题目。python语言可以调用函数`deque`来构建操作便捷的队列，也可以使用列表指针来实现。

## 代码
### Without Repeating Characters
```python
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        Method_one : use the deque function
        :type s: str
        :rtype: int
        """
        from collections import deque
        queue = deque([])
        maxlenght = 0

        for i in s:
            if i in queue:
                while queue.popleft() != i:
                    pass
            queue.append(i)
            maxlenght = max(maxlenght, len(queue))
        else:
            return(maxlenght)

    def lengthOfLongestSubstring2(self, s):
        """
        Method_two : use the queue points.
        :type s: str
        :rtype: int
        """
        longest = 0
        start = 0
        visited = [False for _ in xrange(256)]

        for i, char in enumerate(s):
            if visited[ord(char)]:
                while char != s[start]:
                    visited[ord(s[start])] = False
                    start += 1
                start += 1
            else:
                visited[ord(char)] = True
            longest = max(longest, i - start + 1)
        return longest


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring("abcabcbb"))
```

### With At Most K Distinct Characters
```python
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        lookup = {}
        maxlenght = 0
        left = 0

        for i, char in enumerate(s):
            if char in lookup:
                lookup[char] = i
            else:
                if len(lookup) == k:
                    sorten = sorted(lookup.iteritems(), key=lambda d: d[1])
                    del lookup[sorten[0][0]]
                    if len(sorten) > 1:
                        left = sorten[1][1]
                    else:
                        left = i
                    lookup[char] = i
                else:
                    lookup[char] = i
            maxlenght = max(maxlenght, i - left + 1)
        else:
            return(maxlenght)


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstringKDistinct('eceba', 2))
```

#code/leetcode
# Longest Substring Without Repeating Characters


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
    print(Solution().lengthOfLongestSubstring("abcaabc"))

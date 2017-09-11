# Valid Parentheses


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = {'{', '[', '('}
        dic = {
            '}': '{',
            ']': '[',
            ')': '(',
        }

        stack = []

        for i in s:
            if i in left:
                stack.append(i)
            else:
                if stack == [] or stack[-1] != dic[i]:
                    return False
                else:
                    stack.pop()

        return not stack


if __name__ == '__main__':
    print(Solution().isValid("[(})}]"))

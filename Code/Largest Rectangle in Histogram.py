# Largest Rectangle in Histogram


class Solution(object):
    def largestRectangleArea1(self, heights):
        """
        Method One: TLE
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0

        n, ans, k, origin_heights = len(heights), 0, 1, []
        for i in heights:
            origin_heights.append(i)

        l = [0 for _ in xrange(n)]
        r = [n for _ in xrange(n)]
        h = [0 for _ in xrange(n)]

        while(k):
            k = 0
            left = 0

            for j in xrange(n):
                if heights[j] > 0:
                    l[j] = max(l[j], left)
                    h[j] += 1
                    k = 1
                else:
                    l[j] = 0
                    h[j] = 0
                    left = j + 1

            right = n
            for j in reversed(xrange(n)):
                if heights[j] > 0:
                    r[j] = min(r[j], right)
                    if (r[j] - l[j]) == 1:
                        print heights, j
                        ans = max(ans, origin_heights[j])
                        l[j] -= 1
                        heights[j] = -1

                    else:
                        ans = max(ans, h[j] * (r[j] - l[j]))
                else:
                    r[j] = n
                    right = j

                heights[j] -= 1

        return ans

    def largestRectangleArea2(self, heights):
        """
        Method Two
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0

        ans = 0

        heights = [0] + heights + [0]
        l = len(heights)

        num = 0
        for i in heights[1:-1]:

            num += 1
            width = 1

            for j in reversed(heights[0:num]):
                if j < i:
                    break
                else:
                    width += 1

            for j in heights[num + 1:-1]:
                if j < i:
                    break
                else:
                    width += 1

            ans = max(ans, i * width)

        return ans

    def largestRectangleArea3(self, heights):
        """
        Method Three
        :type heights: List[int]
        :rtype: int
        """
        def dp(heights):
            if not heights:
                return 0

            if len(heights) == 1:
                return heights[0]

            sorted_heights = sorted(heights)
            min_height = sorted_heights[0]
            min_num = heights.index(min_height)

            return max(dp(heights[:min_num]),
                       dp(heights[min_num + 1:]),
                       min_height * len(heights)
                       )

        return dp(heights)

    def largestRectangleArea4(self, heights):
        stack, ans, i = [], 0, 0
        while i <= len(heights):

            if not stack or (i < len(heights) and heights[i] > heights[stack[-1]]):
                stack.append(i)
                i += 1
            else:
                last = stack.pop()
                if stack:
                    ans = max(ans, heights[last] * (i - stack[-1] - 1))
                else:
                    ans = max(ans, heights[last] * i)
            print stack, ans

        return ans


if __name__ == '__main__':
    print(Solution().largestRectangleArea4([2, 1, 5, 6, 2, 3]))

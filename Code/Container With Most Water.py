# Container With Most Water


class Solution(object):
    def qsort(self, a, p, q):
        x = a[p]
        i = p

        for j in range(p + 1, q):
            if a[j] <= x:
                i += 1
                a[i], a[j] = a[j], a[i]

        a[p], a[i] = a[i], a[p]

        if p < i - 1:
            self.qsort(a, p, i)
        if q > i + 1:
            self.qsort(a, i + 1, q)

    def maxArea1(self, height):
        """
        Method_one: Brute Force
        :type height: List[int]
        :rtype: int
        """
        for num, i in enumerate(height):
            height[num] = (i, num)

        self.qsort(height, 0, len(height))

        ans = 0
        for num, i in enumerate(height[:-1]):
            temp = 0
            for j in height[num:]:
                temp = max(temp, abs(i[1] - j[1]))
            ans = max(ans, i[0] * temp)

        return ans

    def maxArea(self, height):
        """
        Method_two: Two Pointer Approach
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1
        ans = 0
        while r > l:
            ans = max(ans, min(height[l], height[r]) * (r - l))
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1

        return ans


if __name__ == '__main__':
    print(Solution().maxArea([1, 8, 3, 2, 9, 7, 3, 6]))

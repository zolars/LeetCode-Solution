# Maximum Product Subarray


class Solution(object):
    def maxProduct1(self, nums):
        """
        Method_1 : O(n^2)
        :type nums: List[int]
        :rtype: int
        """
        ans = -2 ** 32
        time = 0
        for i in xrange(len(nums)):
            temp = 1
            for j in xrange(i, len(nums)):
                temp *= nums[j]
                print temp, nums[j]
                ans = max(ans, temp)
                time += 1

        return ans, time, len(nums)

    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def calcu(l, r):
            first = False
            temp, left = 1, 0
            for i in xrange(l, r + 1):
                temp *= nums[i]
                if not first and nums[i] < 0:
                    left = temp
                    first = True
                    temp = 1

            right_temp = temp
            all_temp = right_temp * left
            temp = all_temp

            for i in xrange(r, l - 1, -1):
                temp /= nums[i]
                if nums[i] < 0:
                    print temp, all_temp, right_temp
                    return max(all_temp, right_temp, temp)

            return max(all_temp, right_temp, temp)

        if len(nums) == 1:
            return nums[0]

        nums += [0]
        ans = -2 ** 32
        left = 0
        for i in xrange(len(nums)):
            if nums[i] == 0:
                if i - left > 1:
                    ans = max(0, ans, calcu(left, i - 1))
                else:
                    ans = max(0, ans, nums[i - 1])
                left = i + 1

        return ans


if __name__ == '__main__':
    print Solution().maxProduct([1, 2, 3, 4])

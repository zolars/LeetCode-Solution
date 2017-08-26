#  Remove Element


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if nums == []:
            return 0
        j = len(nums)
        i = 0
        while i < j:
            if nums[i] == val:
                j -= 1
                nums[i], nums[j] = nums[j], nums[i]

            else:
                i += 1

        return i


if __name__ == '__main__':
    print(Solution().removeElement([1, 4, 1, 3, 2], 1))

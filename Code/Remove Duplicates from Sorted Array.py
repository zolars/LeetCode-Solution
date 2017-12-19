# Remove Duplicates from Sorted Array


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        point, lenght = 1, 0
        for i in xrange(1, len(nums)):
            if nums[i - 1] != nums[i]:
                nums[point] = nums[i]
                point += 1

        return point


if __name__ == '__main__':
    print Solution().removeDuplicates([1, 1, 2, 3, 4, 5, 5])

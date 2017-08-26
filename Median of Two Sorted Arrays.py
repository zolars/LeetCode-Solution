# Median of Two Sorted Arrays


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        key = (len(nums1) + len(nums2)) // 2
        ans = []
        n1, n2 = 0, 0
        for i in xrange(key + 1):
            if n1 == len(nums1):
                ans.append(nums2[n2])
                n2 += 1
            elif n2 == len(nums2):
                ans.append(nums1[n1])
                n1 += 1
            elif nums1[n1] <= nums2[n2]:
                ans.append(nums1[n1])
                n1 += 1
            else:
                ans.append(nums2[n2])
                n2 += 1

        if (len(nums1) + len(nums2)) % 2 == 0:
            return((ans[key - 1] + ans[key]) / 2.00000)
        else:
            return(ans[key])


if __name__ == '__main__':
    print(Solution().findMedianSortedArrays([1, 3], [2, 4]))

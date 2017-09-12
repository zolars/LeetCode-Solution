# LeetCode题解：Median of Two Sorted Arrays

## 题目

There are two sorted arrays nums1 and nums2 of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

- Example nums1 = [1, 3] nums2 = [2] The median is 2.0

## 题解

屡次调试之后才AC的一道很简单的队列题目。没有什么思考的难度，但是数组的边界要考虑清楚----这一点还很是有待加强。

## 代码

```python
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
```

# code/leetcode

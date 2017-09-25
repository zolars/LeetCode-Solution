# LeetCode题解：3Sum

## 题目

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero. Note: The solution set must not contain duplicate triplets.

-   Example

    given array S = [-1, 0, 1, 2, -1, -4], A solution set is: \[ [-1, 0, 1] , [-1, -1, 2] ]

## 题解

使用双指针法遍历。所以我的双指针玩的还是太差了，之前的有一道双指针的题目 Container With Most Water 我就没做出。

所谓双指针，一般是：一个在头，一个在尾，双向逼近。此题亦如此。

一个之前没发现过的优化：能写在 while 语句里的判断不要写 if ，有可能因此而超时，而这种超时是不可能检查出来的。

## 代码

```python
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)

        i, ans = 0, []

        for i in xrange(len(nums) - 2):
            if nums[i] > 0 or (i != 0 and nums[i] == nums[i - 1]):
                continue

            l, r = i + 1, len(nums) - 1

            print i, l, r

            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s > 0:
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1

            i += 1

        return ans


if __name__ == '__main__':
    print(Solution().threeSum([-1, -1, 0, 1]))
```

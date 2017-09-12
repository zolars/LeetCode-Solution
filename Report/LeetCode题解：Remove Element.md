# LeetCode题解：Remove Element

Given an array and a value, remove all instances of that value in place and return the new length. Do not allocate extra space for another array, you must do this in place with constant memory. The order of elements can be changed. It doesn't matter what you leave beyond the new length.

-   Example Given input array nums =`[3,2,2,3]`, val =`3` Your function should return length = 2, with the first two elements of nums being 2.

## 题解

双指针的运用。不要想当然的使用python自带的诸多列表操作函数了，因为空间复杂度的一些限制。

~~LeetCode的答案明明写着要int型，却反馈出来一个列表是什么鬼啊？~~

## 代码

```python
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
```

# code/leetcode

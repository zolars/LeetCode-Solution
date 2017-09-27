# LeetCode题解: Two Sum

> 今天开始刷刷题, 使用python2.7语言. 为何学了python3.6却要用2.7呢？因为python2.7的适用性更广（其实是因为LeetCode只支持python2.7的缘故）, 那么, 就此开始吧.

## 题目

Given an array of integers, return **indices** of the two numbers such that they add up to a specific target. You may assume that each input would have **exactly** one solution, and you may not use the same element twice.

-   Example

    Given nums = [2, 7, 11, 15], target = 9, Because nums[0] + nums[1] = 2 + 7 = 9, return [0, 1].

## 题解

### Brute Force

因为题目里说到每个输入有且只有一个解, 所以最简单的想法即逐一比较每一对数值.  此方法时间复杂度为$O(n)$

```python
k = 0
for i in nums:
    k += 1
    if target - i in nums[k:]:
        return(k - 1, nums[k:].index(target - i) + k)
```

### Hash Table

使用了python的优秀特性: python中的字典自带哈希表且索引速度很快, 在字典中查找的复杂度为$O(1)$, 而在列表中查找的复杂度为$O(n)$.  建立一个边构建边查找的哈希表（One-pass Hash Table）, 是一个很好的优化.

```python
lookup = {}
for i, num in enumerate(nums):
    if target - num in lookup:
        return([lookup[target - num], i])
        break
    lookup[num] = i
return([])
```

-   在序列中循环时, 索引位置和对应值可以使用`enumerate()`函数同时得到.  `for i, j in enumerate(list)`

## 代码

```python
class Solution(object):
    def twoSum(self, nums, target):
        """
        Method_one : Brute Force
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return([lookup[target - num], i])
                break
            lookup[num] = i
        return([])

    def twoSum2(self, nums, target):
        """
        Method_two : Hash Table
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        k = 0
        for i in nums:
            k += 1
            if target - i in nums[k:]:
                return(k - 1, nums[k:].index(target - i) + k)


if __name__ == '__main__':
    print Solution().twoSum([1, 2, 3, 4], 6)
```

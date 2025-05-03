"""
35. 搜索插入位置

给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

请必须使用时间复杂度为 O(log n) 的算法。


示例 1:
输入: nums = [1,3,5,6], target = 5
输出: 2

示例 2:
输入: nums = [1,3,5,6], target = 2
输出: 1

示例 3:
输入: nums = [1,3,5,6], target = 7
输出: 4

提示:

1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums 为 无重复元素 的 升序 排列数组
-10^4 <= target <= 10^4
"""
import unittest


# Definition for singly-linked list.
def search_insert(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2  # 防止溢出，计算中间索引

        if nums[mid] == target:
            return mid  # 找到目标，返回索引
        elif nums[mid] < target:
            left = mid + 1  # 目标在右边
        else:
            right = mid - 1  # 目标在左边
    # 如果没找到目标值，left 就是目标插入位置
    return left


class TestSearchInsert(unittest.TestCase):

    def test_search_insert(self):
        self.assertEqual(2, search_insert(nums=[1, 3, 5, 6], target=5))

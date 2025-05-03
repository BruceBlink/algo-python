"""
34. 在排序数组中查找元素的第一个和最后一个位置
给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。

你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。



示例 1：
输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]

示例 2：
输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]

示例 3：
输入：nums = [], target = 0
输出：[-1,-1]

提示：

0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
nums 是一个非递减数组
-10^9 <= target <= 10^9
"""
import unittest


# Definition for singly-linked list.
def search_range(nums: list[int], target: int) -> list[int]:
    # 辅助函数：修改的二分查找，用于寻找第一个或最后一个位置
    def find_boundary(nums, target, find_first):
        left, right = 0, len(nums) - 1
        ans = -1 # 初始化答案为 -1 (表示未找到)

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                ans = mid # 找到一个目标值，记录为当前可能的答案
                if find_first:
                    # 如果找第一个，继续向左搜索更靠前的目标值
                    right = mid - 1
                else:
                    # 如果找最后一个，继续向右搜索更靠后的目标值
                    left = mid + 1
            elif nums[mid] < target:
                # 中间值小于目标值，目标值在右侧
                left = mid + 1
            else: # nums[mid] > target
                # 中间值大于目标值，目标值在左侧
                right = mid - 1

        return ans # 返回找到的第一个或最后一个位置，如果未找到则返回 -1

    # 调用辅助函数分别寻找第一个和最后一个位置
    first_pos = find_boundary(nums, target, True)
    last_pos = find_boundary(nums, target, False)

    # 返回结果列表
    return [first_pos, last_pos]


class TestSearchRange(unittest.TestCase):

    def test_search_range(self):
        self.assertEqual([3, 4], search_range(nums=[5, 7, 7, 8, 8, 10], target=8))
        self.assertEqual([-1, -1], search_range(nums=[5, 7, 7, 8, 8, 10], target=6))
        self.assertEqual([-1, -1], search_range(nums=[], target=0))

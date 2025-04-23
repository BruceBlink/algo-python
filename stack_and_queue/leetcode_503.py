"""
下一个更大元素 II（LeetCode.503）
数字 x 的 下一个更大的元素 是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1 。
示例 1:
输入: nums = [1,2,1]
输出: [2,-1,2]
解释: 第一个 1 的下一个更大的数是 2；
数字 2 找不到下一个更大的数；
第二个 1 的下一个最大的数需要循环搜索，结果也是 2。

示例 2:
输入: nums = [1,2,3,4,3]
输出: [2,3,4,-1,4]
提示:
1 <= nums.length <= 104
-109 <= nums[i] <= 109

:param nums:
:return:
"""
import unittest


def next_greater_element(nums: list[int]) -> list[int]:
    n = len(nums)
    res = [-1] * n
    stack = []
    for i in range(2 * n):
        current_index = i % n
        while stack and nums[current_index] > nums[stack[-1]]:
            top = stack.pop()
            res[top] = nums[current_index]
        stack.append(current_index)
    return res


class TestDailyNextGreaterElement(unittest.TestCase):

    def test_next_greater_element(self):
        self.assertEqual(next_greater_element([1, 2, 3, 4, 3]), [2, 3, 4, -1, 4])

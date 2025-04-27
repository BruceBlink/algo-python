"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

请注意 ，必须在不复制数组的情况下原地对数组进行操作。



示例 1:

输入: nums = [0,1,0,3,12]
输出: [1,3,12,0,0]
示例 2:

输入: nums = [0]
输出: [0]


提示:
1 <= nums.length <= 10^4
-2^31 <= nums[i] <= 2^31 - 1
"""
import unittest


def move_zeroes(nums: list[int]) -> list[int]:
    """
    将所有 0 移动到数组末尾，保持非零元素相对顺序（双指针，两遍遍历）
    """
    n = len(nums)
    if n == 0:  # 数组为空直接返回
        return []
    # insert_pos 指针：指向下一个非零元素应该插入的位置
    insert_pos = 0

    # 第一遍遍历：将所有非零元素前移
    for i in range(n):
        # 如果当前元素 nums[i] 不是 0
        if nums[i] != 0:
            # 将当前非零元素放到 insert_pos 指向的位置
            nums[insert_pos] = nums[i]
            # 移动 insert_pos 指针，准备接收下一个非零元素
            insert_pos += 1

    # 第二遍遍历：将从 insert_pos 到末尾的所有位置填充为 0
    # 这些位置就是原数组中所有 0 最终应该在的位置
    for j in range(insert_pos, n):
        nums[j] = 0
    return nums


class TestMoveZeroes(unittest.TestCase):

    def test_move_zeroes(self):
        self.assertEqual(move_zeroes(nums=[0, 1, 0, 3, 12]), [1, 3, 12, 0, 0])
        self.assertTrue(move_zeroes(nums=[0]), [0])

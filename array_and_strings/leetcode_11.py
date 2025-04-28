"""
给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
返回容器可以储存的最大水量。
说明：你不能倾斜容器。

示例 1：
输入：[1,8,6,2,5,4,8,3,7]
输出：49
解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。

示例 2：
输入：height = [1,1]
输出：1
"""
import unittest


def maxArea(height: list[int]) -> int:
    left = 0  # 左指针
    right = len(height) - 1  # 右指针
    max_area = 0  # 存储最大面积

    # 当左指针在右指针左边时循环
    while left < right:
        # 计算当前容器的宽度
        current_width = right - left
        # 计算当前容器的高度 (取两边高度的最小值)
        current_height = min(height[left], height[right])

        # 计算当前容器的面积
        current_area = current_width * current_height

        # 更新最大面积
        max_area = max(max_area, current_area)

        # 移动指针：移动较矮的那一边
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    # 返回找到的最大面积
    return max_area


def maxArea1(height: list[int]) -> int:
    n = len(height)
    if n < 2:
        return 0
    max_area = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            current_width = j - i
            current_area = current_width * min(height[i], height[j])
            max_area = max(max_area, current_area)
    return max_area


class TestMaxArea(unittest.TestCase):

    def test_move_zeroes(self):
        self.assertEqual(49, maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]))
        self.assertEqual(1, maxArea(height=[1, 1]))
        self.assertEqual(16, maxArea(height=[4, 3, 2, 1, 4]))
        self.assertEqual(20, maxArea(height=[9, 8, 7, 6, 5]))
        self.assertEqual(12, maxArea(height=[1, 5, 3, 2, 4]))

    def test_move_zeroes1(self):
        self.assertEqual(49, maxArea1(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]))
        self.assertEqual(1, maxArea1(height=[1, 1]))
        self.assertEqual(16, maxArea1(height=[4, 3, 2, 1, 4]))
        self.assertEqual(20, maxArea1(height=[9, 8, 7, 6, 5]))
        self.assertEqual(12, maxArea1(height=[1, 5, 3, 2, 4]))
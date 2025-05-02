"""
350. 两个数组的交集 II
给你两个整数数组 nums1 和 nums2 ，请你以数组形式返回两数组的交集。
返回结果中每个元素出现的次数，应与元素在两个数组中都出现的次数一致（如果出现次数不一致，则考虑取较小值）。
可以不考虑输出结果的顺序。

示例 1：
输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2,2]
示例 2:
输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[4,9]

提示：

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000


进阶：
如果给定的数组已经排好序呢？你将如何优化你的算法？
如果 nums1 的大小比 nums2 小，哪种方法更优？
如果 nums2 的元素存储在磁盘上，内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？
"""
import unittest
from collections import Counter


def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
    # 计算两个数组的词频统计

    counter_nums1 = Counter(nums1)
    counter_nums2 = Counter(nums2)

    # 使用 & 运算符得到交集的词频统计 (取每个元素在两个 Counter 中的最小计数)
    intersection_counter = counter_nums1 & counter_nums2

    result = []
    # 遍历交集的词频统计结果
    for item, count in intersection_counter.items():
        # 将每个元素按照它在交集中的计数添加到结果列表
        result.extend([item] * count)  # 使用 extend 和 [item] * count 更高效地添加多个元素

    return result


def intersect1(nums1: list[int], nums2: list[int]) -> list[int]:
    # 优化：对较短的数组进行计数，可以节省空间
    if len(nums1) < len(nums2):
        nums1, nums2 = nums2, nums1  # 确保 nums1 是较长的或等长的那个，对 nums2 计数

    # 使用 Counter 统计 nums2 中元素的频率
    num_counts = Counter(nums2)

    result = []

    # 遍历 nums1
    for num in nums1:
        # 如果当前元素在计数中存在且计数大于 0
        if num in num_counts and num_counts[num] > 0:
            # 将元素添加到结果列表
            result.append(num)
            # 对应元素的计数减一
            num_counts[num] -= 1

    return result


def intersect2(nums1: list[int], nums2: list[int]) -> list[int]:
    # 1. 排序
    nums1.sort()
    nums2.sort()

    n1 = len(nums1)
    n2 = len(nums2)
    p1 = 0  # 指向 nums1 的指针
    p2 = 0  # 指向 nums2 的指针
    result = []

    # 2. 双指针遍历
    while p1 < n1 and p2 < n2:
        if nums1[p1] == nums2[p2]:
            # 找到交集元素，添加到结果
            result.append(nums1[p1])
            # 两个指针都向前移动
            p1 += 1
            p2 += 1
        elif nums1[p1] < nums2[p2]:
            # nums1 的元素较小，移动 nums1 指针
            p1 += 1
        else:  # nums1[p1] > nums2[p2]
            # nums2 的元素较小，移动 nums2 指针
            p2 += 1

    return result


class TestIntersect(unittest.TestCase):

    def test_example_1(self):
        # LeetCode 示例 1
        nums1 = [1, 2, 2, 1]
        nums2 = [2, 2]
        # 预期输出 [2, 2]，无需排序因为本身有序
        expected_output = [2, 2]

        actual_output = intersect(nums1, nums2)

        # 对实际结果和预期结果排序后比较
        self.assertEqual(sorted(actual_output), sorted(expected_output))

    def test_example_2(self):
        # LeetCode 示例 2
        nums1 = [4, 9, 5]
        nums2 = [9, 4, 9, 8, 4]
        # 预期输出 [4, 9] 或 [9, 4]。排序后是 [4, 9]
        expected_output = [4, 9]

        actual_output = intersect(nums1, nums2)

        self.assertEqual(sorted(actual_output), sorted(expected_output))

    def test_empty_arrays(self):
        # 两个数组都为空
        nums1 = []
        nums2 = []
        expected_output = []

        actual_output = intersect(nums1, nums2)

        self.assertEqual(sorted(actual_output), sorted(expected_output))

    def test_one_empty_array(self):
        # 其中一个数组为空
        nums1 = [1, 2, 3]
        nums2 = []
        expected_output = []

        actual_output = intersect(nums1, nums2)

        self.assertEqual(sorted(actual_output), sorted(expected_output))

    def test_no_common_elements(self):
        # 没有共同元素
        nums1 = [1, 2, 3, 4, 5]
        nums2 = [6, 7, 8, 9, 10]
        expected_output = []

        actual_output = intersect(nums1, nums2)

        self.assertEqual(sorted(actual_output), sorted(expected_output))

    def test_with_duplicates(self):
        # 包含大量重复元素
        nums1 = [1, 1, 1, 1, 2, 2]
        nums2 = [1, 1, 2, 3]
        # 1 在 nums1 中出现 4 次，在 nums2 中出现 2 次，取 min(4, 2) = 2 次
        # 2 在 nums1 中出现 2 次，在 nums2 中出现 1 次，取 min(2, 1) = 1 次
        # 预期输出 [1, 1, 2]
        expected_output = [1, 1, 2]

        actual_output = intersect(nums1, nums2)

        self.assertEqual(sorted(actual_output), sorted(expected_output))

    def test_identical_arrays(self):
        # 两个数组完全相同
        nums1 = [1, 2, 3, 4, 5]
        nums2 = [1, 2, 3, 4, 5]
        expected_output = [1, 2, 3, 4, 5]

        actual_output = intersect(nums1, nums2)

        self.assertEqual(sorted(actual_output), sorted(expected_output))

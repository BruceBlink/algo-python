"""
78. 子集
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。


示例 1：
输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

示例 2：
输入：nums = [0]
输出：[[],[0]]

提示：

1 <= nums.length <= 10
-10 <= nums[i] <= 10
nums 中的所有元素 互不相同
"""

import unittest
from collections import deque  # 虽然 subsets 不直接用 deque，但之前的辅助函数可能需要


# Helper function to sort a list of lists for comparison (only outer list sorted)
# 辅助函数：排序列表的列表，用于忽略排列结果的顺序 (只排序外层列表)
def sort_list_of_lists(list_of_lists: list[list]) -> list[list]:
    """
    Sorts the outer list of lists. Assumes elements within inner lists
    are in a consistent order (e.g., based on original nums order).
    This allows comparing two lists of subsets regardless of the order
    of subsets in the outer list.
    """
    # Create a copy to avoid modifying the original list if needed
    # The inner lists are assumed to be in a consistent order by the algorithm
    # We only sort the outer list
    sorted_outer = sorted(list_of_lists)
    return sorted_outer


# The Solution class with the subsets method (using iterative approach)
# Solution 类，包含 subsets 方法 (使用迭代法)
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        """
        迭代
        @param nums:
        @return:
        """
        # 初始化结果列表，包含一个空集
        results = [[]]

        # 遍历数组中的每一个数字
        for num in nums:
            # 对于当前的 num，创建一批新的子集
            # 遍历 results 中【当前】已有的所有子集
            # 注意这里使用切片 results[:] 或者遍历副本，避免在遍历过程中修改列表导致问题
            for subset in results[:]:  # 遍历 results 的一个副本
                # 创建一个新的子集：在当前子集 subset 的基础上添加 num
                new_subset = list(subset)  # 创建副本，避免修改 subset
                new_subset.append(num)

                # 将新的子集添加到结果列表
                results.append(new_subset)

        # 返回所有子集
        return results

    def subsets1(self, nums: list[int]) -> list[list[int]]:
        """
        回溯
        @param nums:
        @return:
        """
        # 初始化结果列表，用于存储所有找到的子集
        results = []

        # 定义回溯辅助函数
        # start_index: 在 nums 中，当前这一轮选择的起始索引
        # current_subset: 当前正在构建的部分子集
        def backtrack(start_index, current_subset):
            # 无论当前是什么样的 current_subset，它都是一个有效的子集
            results.append(list(current_subset))  # 添加当前子集的副本到结果列表

            # 遍历 nums 数组，从 start_index 开始选择元素
            for i in range(start_index, len(nums)):
                # --- 选择 (Choose) ---
                current_subset.append(nums[i])  # 将当前元素添加到子集

                # --- 探索 (Explore) ---
                # 递归调用，从下一个索引 i+1 开始，继续构建子集
                # 确保只选择当前元素后面的元素，避免重复子集
                backtrack(i + 1, current_subset)

                # --- 撤销选择 / 回溯 (Unchoose / Backtrack) ---
                # 移除刚刚添加的元素，以便尝试其他可能性
                current_subset.pop()

        # 从索引 0 开始，空子集 [] 初始化回溯过程
        backtrack(0, [])

        # 返回所有找到的子集
        return results

    def subsets2(self, nums: list[int]) -> list[list[int]]:
        """
        拓展法，每出现一个新元素，则把它添加到已有的所有子集上得到新的子集
        @param nums:
        @return:
        """
        res = [[]]  # 初始只有空集
        for num in nums:
            # 对现有的每个子集，都可以加上当前 num，形成新子集
            res += [curr + [num] for curr in res]
        return res

    def subsets3(self, nums: list[int]) -> list[list[int]]:
        """
        二进制位对应遍历
        @param nums:
        @return:
        """
        n = len(nums)
        res = []
        # 枚举 0..(2^n-1) 每个二进制数
        for mask in range(1 << n):
            subset = []
            for i in range(n):
                if mask & (1 << i):
                    subset.append(nums[i])
            res.append(subset)
        return res


# Unit tests using unittest.TestCase
# 使用 unittest.TestCase 编写单元测试
class TestSubsets(unittest.TestCase):

    def test_example_1(self):
        # LeetCode 示例 1
        nums = [1, 2, 3]
        # 预期的所有子集 (迭代法生成的顺序)
        expected_subsets_unsorted = [
            [],  # []
            [1],  # [] + [1]
            [2],  # [] + [2]
            [1, 2],  # [1] + [2]
            [3],  # [] + [3]
            [1, 3],  # [1] + [3]
            [2, 3],  # [2] + [3]
            [1, 2, 3]  # [1, 2] + [3]
        ]

        solution = Solution()
        actual_subsets = solution.subsets(nums)

        # 由于子集的顺序不重要，对实际和预期的列表进行排序后比较外层列表
        self.assertEqual(sort_list_of_lists(actual_subsets), sort_list_of_lists(expected_subsets_unsorted))

    def test_single_element_zero(self):
        # 只有一个元素的数组，包含 0
        nums = [0]
        expected_subsets_unsorted = [
            [],  # []
            [0]  # [] + [0]
        ]

        solution = Solution()
        actual_subsets = solution.subsets(nums)

        self.assertEqual(sort_list_of_lists(actual_subsets), sort_list_of_lists(expected_subsets_unsorted))

    def test_empty_array(self):
        # 输入为空数组 (根据约束 0 <= nums.length)
        nums = []
        expected_subsets_unsorted = [
            []  # 空数组的子集只有空集
        ]

        solution = Solution()
        actual_subsets = solution.subsets(nums)

        self.assertEqual(sort_list_of_lists(actual_subsets), sort_list_of_lists(expected_subsets_unsorted))

    def test_two_elements_one_zero(self):
        # 两个元素的数组，顺序不同
        nums = [1, 0]
        # 迭代法生成顺序:
        # Start: [[]]
        # Process 1: [[], [1]]
        # Process 0: [[], [1], [0], [1, 0]]
        expected_subsets_unsorted = [
            [], [1], [0], [1, 0]
        ]

        solution = Solution()
        actual_subsets = solution.subsets(nums)

        self.assertEqual(sort_list_of_lists(actual_subsets), sort_list_of_lists(expected_subsets_unsorted))


# This allows running the tests from the command line
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

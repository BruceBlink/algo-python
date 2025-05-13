"""
46. 全排列

给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
示例 1：
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

示例 2：
输入：nums = [0,1]
输出：[[0,1],[1,0]]

示例 3：
输入：nums = [1]
输出：[[1]]

提示：

1 <= nums.length <= 6
-10 <= nums[i] <= 10
nums 中的所有整数 互不相同
"""

import unittest
from collections import deque  # 虽然 permute 不直接用 deque，但之前的 TreeNode 辅助函数可能需要


# Helper function to sort a list of lists for comparison
# 辅助函数：排序列表的列表，用于忽略排列结果的顺序
def sort_list_of_lists(list_of_lists: list[list]) -> list[list]:
    """
    Sorts each inner list and then sorts the outer list of lists.
    This allows comparing two lists of permutations regardless of the order
    of permutations in the outer list.
    """
    # Create a copy to avoid modifying the original list if needed
    sorted_inner = [sorted(inner) for inner in list_of_lists]
    # Sort the outer list of lists
    sorted_outer = sorted(sorted_inner)
    return sorted_outer


# The Solution class with the permute method (using backtracking approach)
# Solution 类，包含 permute 方法 (使用回溯法)
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        # 初始化结果列表，用于存储所有找到的全排列
        results = []
        # 初始化布尔数组，用于标记 nums 中对应索引的数字是否已被使用
        used = [False] * len(nums)

        # 定义回溯辅助函数
        # current_permutation: 当前正在构建的部分排列
        # used: 标记 nums 中哪些数字已被使用
        def backtrack(current_permutation, used):
            # 基本情况：如果当前排列的长度等于 nums 的长度，说明已找到一个完整的排列
            if len(current_permutation) == len(nums):
                # 将当前排列的副本添加到结果列表
                results.append(list(current_permutation))  # 注意这里要添加副本
                return  # 返回上一层

            # 递归步骤：遍历 nums 中的每一个数字
            for i in range(len(nums)):
                # 如果当前数字还没有被使用过
                if not used[i]:
                    # --- 选择 (Choose) ---
                    used[i] = True  # 标记该数字已被使用
                    current_permutation.append(nums[i])  # 将该数字添加到当前排列

                    # --- 探索 (Explore) ---
                    # 递归调用，继续构建排列的下一个位置
                    backtrack(current_permutation, used)

                    # --- 撤销选择 / 回溯 (Unchoose / Backtrack) ---
                    # 移除刚刚添加的数字，以便尝试其他可能性
                    current_permutation.pop()
                    # 标记该数字为未使用，供其他路径选择
                    used[i] = False

        # 从空排列和全 false 的 used 数组开始回溯
        backtrack([], used)

        # 返回所有找到的全排列
        return results


# Unit tests using unittest.TestCase
# 使用 unittest.TestCase 编写单元测试
class TestPermute(unittest.TestCase):

    def test_example_1(self):
        # LeetCode 示例 1
        nums = [1, 2, 3]
        # 预期的所有全排列 (顺序不重要)
        expected_permutations = [
            [1, 2, 3], [1, 3, 2], [2, 1, 3],
            [2, 3, 1], [3, 1, 2], [3, 2, 1]
        ]

        solution = Solution()
        actual_permutations = solution.permute(nums)

        # 由于结果的顺序不重要，对实际和预期的列表进行排序后比较
        self.assertEqual(sort_list_of_lists(actual_permutations), sort_list_of_lists(expected_permutations))

    def test_two_elements_zero_one(self):
        # 两个元素的数组，包含 0
        nums = [0, 1]
        expected_permutations = [
            [0, 1], [1, 0]
        ]

        solution = Solution()
        actual_permutations = solution.permute(nums)

        self.assertEqual(sort_list_of_lists(actual_permutations), sort_list_of_lists(expected_permutations))

    def test_single_element(self):
        # 只有一个元素的数组
        nums = [1]
        expected_permutations = [
            [1]
        ]

        solution = Solution()
        actual_permutations = solution.permute(nums)

        self.assertEqual(sort_list_of_lists(actual_permutations), sort_list_of_lists(expected_permutations))

    def test_two_elements_one_zero(self):
        # 两个元素的数组，顺序不同于上一个测试
        nums = [1, 0]
        expected_permutations = [
            [1, 0], [0, 1]
        ]

        solution = Solution()
        actual_permutations = solution.permute(nums)

        self.assertEqual(sort_list_of_lists(actual_permutations), sort_list_of_lists(expected_permutations))

    # 根据题目约束 1 <= nums.length <= 6，空数组 [] 不是有效输入，所以不添加测试用例


# This allows running the tests from the command line
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

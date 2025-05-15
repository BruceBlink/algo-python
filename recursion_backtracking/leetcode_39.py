"""
39. 组合总和
给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates
中可以使数字和为目标数 target 的 所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。
candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。
对于给定的输入，保证和为 target 的不同组合数少于 150 个。

示例 1：
输入：candidates = [2,3,6,7], target = 7
输出：[[2,2,3],[7]]
解释：
2 和 3 可以形成一组候选，2 + 2 + 3 = 7 。注意 2 可以使用多次。
7 也是一个候选， 7 = 7 。
仅有这两种组合。

示例 2：
输入: candidates = [2,3,5], target = 8
输出: [[2,2,2,2],[2,3,3],[3,5]]

示例 3：
输入: candidates = [2], target = 1
输出: []

提示：

1 <= candidates.length <= 30
2 <= candidates[i] <= 40
candidates 的所有元素 互不相同
1 <= target <= 40
"""

import unittest


# Helper function to sort a list of lists for comparison
# 辅助函数：排序列表的列表，用于忽略组合结果的顺序
# 同时排序内部列表，以确保比较的是集合内容而不是顺序
def sort_list_of_lists(list_of_lists: list[list]) -> list[list]:
    """
    Sorts each inner list (combination) and then sorts the outer list of lists.
    This allows comparing two lists of combinations regardless of the order
    of combinations in the outer list.
    """
    # Create a copy to avoid modifying the original list if needed
    sorted_inner = [sorted(inner) for inner in list_of_lists]
    # Sort the outer list of lists
    sorted_outer = sorted(sorted_inner)
    return sorted_outer


# The Solution class with the combinationSum method (using backtracking approach)
# Solution 类，包含 combinationSum 方法 (使用回溯法)
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        # 初始化结果列表，用于存储所有找到的有效组合
        results = []
        # 对 candidates 数组进行排序，便于利用 start_index 避免重复组合
        candidates.sort()

        # 定义回溯辅助函数
        # remaining_target: 当前还需要达成的目标和
        # current_combination: 当前正在构建的部分组合
        # start_index: 在 candidates 中，当前这一轮循环选择数字的起始索引
        def backtrack(remaining_target, current_combination, start_index):
            # --- 基本情况 (Base Cases) ---

            # 1. 如果剩余目标和为 0，找到一个有效组合
            if remaining_target == 0:
                # 添加当前组合的副本到结果列表
                results.append(list(current_combination))
                return  # 返回上一层

            # 2. 如果剩余目标和小于 0，当前路径无效
            if remaining_target < 0:
                return  # 返回上一层

            # --- 递归步骤 (Recursive Step) ---

            # 遍历 candidates 数组，从 start_index 开始选择数字
            for i in range(start_index, len(candidates)):
                # 对于当前考虑的数字 candidates[i]

                # --- 选择 (Choose) ---
                # 将当前数字 candidates[i] 加入组合
                current_combination.append(candidates[i])
                # 计算新的剩余目标和 (直接在调用时计算)
                new_remaining_target = remaining_target - candidates[i]

                # --- 探索 (Explore) ---
                # 递归调用，继续寻找剩余目标和的组合
                # 注意这里传入的新的 start_index 仍然是 i，允许重复使用当前数字
                backtrack(new_remaining_target, current_combination, i)

                # --- 撤销选择 / 回溯 (Unchoose / Backtrack) ---
                # 移除刚刚添加的数字，以便尝试其他可能性
                current_combination.pop()
                # 剩余目标和的恢复是隐式的

        # 从初始目标和 target，空组合 []，从 candidates 索引 0 开始回溯
        backtrack(target, [], 0)

        # 返回所有找到的有效组合
        return results


# Unit tests using unittest.TestCase
# 使用 unittest.TestCase 编写单元测试
class TestCombinationSum(unittest.TestCase):

    def test_example_1(self):
        # LeetCode 示例 1
        candidates = [2, 3, 6, 7]
        target = 7
        # 预期的所有组合 (元素非递减，组合间顺序不重要)
        expected_combinations_unsorted = [
            [2, 2, 3],  # 2 + 2 + 3 = 7
            [7]  # 7 = 7
        ]

        solution = Solution()
        actual_combinations = solution.combinationSum(candidates, target)

        # 由于组合的顺序不重要，对实际和预期的列表进行排序后比较
        self.assertEqual(sort_list_of_lists(actual_combinations), sort_list_of_lists(expected_combinations_unsorted))

    def test_example_2(self):
        # LeetCode 示例 2
        candidates = [2, 3, 5]
        target = 8
        # 预期的所有组合 (元素非递减，组合间顺序不重要)
        expected_combinations_unsorted = [
            [2, 2, 2, 2],  # 2 + 2 + 2 + 2 = 8
            [2, 3, 3],  # 2 + 3 + 3 = 8
            [3, 5]  # 3 + 5 = 8
        ]

        solution = Solution()
        actual_combinations = solution.combinationSum(candidates, target)

        self.assertEqual(sort_list_of_lists(actual_combinations), sort_list_of_lists(expected_combinations_unsorted))

    def test_no_solution(self):
        # 没有找到组合的情况
        candidates = [2]
        target = 1
        expected_combinations_unsorted = []  # 没有组合能组成 1

        solution = Solution()
        actual_combinations = solution.combinationSum(candidates, target)

        self.assertEqual(sort_list_of_lists(actual_combinations), sort_list_of_lists(expected_combinations_unsorted))

    def test_single_candidate(self):
        # 只有一个候选数字
        candidates = [1]
        target = 5
        expected_combinations_unsorted = [
            [1, 1, 1, 1, 1]  # 1 + 1 + 1 + 1 + 1 = 5
        ]

        solution = Solution()
        actual_combinations = solution.combinationSum(candidates, target)

        self.assertEqual(sort_list_of_lists(actual_combinations), sort_list_of_lists(expected_combinations_unsorted))

    def test_multiple_candidates_with_reuse(self):
        # 多个候选数字，需要重复使用
        candidates = [1, 2]
        target = 4
        # 预期的所有组合 (元素非递减，组合间顺序不重要)
        # 1+1+1+1, 1+1+2, 2+2
        expected_combinations_unsorted = [
            [1, 1, 1, 1],
            [1, 1, 2],
            [2, 2]
        ]

        solution = Solution()
        actual_combinations = solution.combinationSum(candidates, target)

        self.assertEqual(sort_list_of_lists(actual_combinations), sort_list_of_lists(expected_combinations_unsorted))

    def test_candidates_need_sorting(self):
        # 候选数字需要排序的情况
        candidates = [3, 2]
        target = 6
        # Sorted candidates: [2, 3]
        # Expected: [2, 2, 2], [3, 3]
        expected_combinations_unsorted = [
            [2, 2, 2],
            [3, 3]
        ]

        solution = Solution()
        actual_combinations = solution.combinationSum(candidates, target)

        self.assertEqual(sort_list_of_lists(actual_combinations), sort_list_of_lists(expected_combinations_unsorted))


# This allows running the tests from the command line
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

"""
17. 电话号码的字母组合

给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

示例 1：
输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]

示例 2：
输入：digits = ""
输出：[]

示例 3：
输入：digits = "2"
输出：["a","b","c"]

提示：

0 <= digits.length <= 4
digits[i] 是范围 ['2', '9'] 的一个数字。

"""

import unittest
from collections import deque  # 导入 deque，虽然 letterCombinations 不直接用，但保留


# Helper function to sort a list of strings for comparison
# 辅助函数：排序字符串列表，用于忽略组合结果的顺序
def sort_list_of_strings(list_of_strings: list[str]) -> list[str]:
    """
    Sorts the list of strings.
    This allows comparing two lists of combinations regardless of their order.
    """
    # Create a copy to avoid modifying the original list if needed
    sorted_list = sorted(list_of_strings)
    return sorted_list


# The Solution class with the letterCombinations method (using iterative approach)
# Solution 类，包含 letterCombinations 方法 (使用迭代法)
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        # 创建数字到字母的映射
        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        # 处理输入为空字符串的情况
        if not digits:
            return []

        # 初始化结果列表，包含一个空字符串作为起点
        results = [""]

        # 遍历输入字符串中的每一个数字
        for digit in digits:
            # 获取当前数字对应的字母
            letters = phone_map[digit]

            # 创建一个新的临时列表，用于存储当前数字生成的新组合
            next_results = []

            # 遍历当前 results 中所有已有的组合
            for combination in results:
                # 遍历当前数字对应的所有字母
                for letter in letters:
                    # 将当前组合和字母连接，形成新的组合
                    next_results.append(combination + letter)

            # 更新 results 为新生成的组合列表
            results = next_results

        # 返回所有最终的字母组合
        return results


# Unit tests using unittest.TestCase
# 使用 unittest.TestCase 编写单元测试
class TestLetterCombinations(unittest.TestCase):

    def test_example_1(self):
        # LeetCode 示例 1
        digits = "23"
        # 预期的所有组合 (按字母序排序)
        expected_combinations = [
            "ad", "ae", "af", "bd", "be", "bf",
            "cd", "ce", "cf"
        ]

        solution = Solution()
        actual_combinations = solution.letterCombinations(digits)

        # 由于结果的顺序不重要，对实际和预期的列表进行排序后比较
        self.assertEqual(sort_list_of_strings(actual_combinations), sort_list_of_strings(expected_combinations))

    def test_empty_string(self):
        # 输入为空字符串
        digits = ""
        expected_combinations = []  # 空字符串没有组合

        solution = Solution()
        actual_combinations = solution.letterCombinations(digits)

        self.assertEqual(sort_list_of_strings(actual_combinations), sort_list_of_strings(expected_combinations))

    def test_single_digit_two(self):
        # 单个数字 2
        digits = "2"
        expected_combinations = ["a", "b", "c"]

        solution = Solution()
        actual_combinations = solution.letterCombinations(digits)

        self.assertEqual(sort_list_of_strings(actual_combinations), sort_list_of_strings(expected_combinations))

    def test_single_digit_nine(self):
        # 单个数字 9 (4个字母)
        digits = "9"
        expected_combinations = ["w", "x", "y", "z"]

        solution = Solution()
        actual_combinations = solution.letterCombinations(digits)

        self.assertEqual(sort_list_of_strings(actual_combinations), sort_list_of_strings(expected_combinations))

    def test_single_digit_seven(self):
        # 单个数字 7 (4个字母)
        digits = "7"
        expected_combinations = ["p", "q", "r", "s"]

        solution = Solution()
        actual_combinations = solution.letterCombinations(digits)

        self.assertEqual(sort_list_of_strings(actual_combinations), sort_list_of_strings(expected_combinations))

    def test_three_digits(self):
        # 三个数字
        digits = "234"
        # 2->abc, 3->def, 4->ghi
        # 所有组合
        expected_combinations = [
            "adg", "adh", "adi", "aeg", "aeh", "aei", "afg", "afh", "afi",
            "bdg", "bdh", "bdi", "beg", "beh", "bei", "bfg", "bfh", "bfi",
            "cdg", "cdh", "cdi", "ceg", "ceh", "cei", "cfg", "cfh", "cfi"
        ]

        solution = Solution()
        actual_combinations = solution.letterCombinations(digits)

        self.assertEqual(sort_list_of_strings(actual_combinations), sort_list_of_strings(expected_combinations))


# This allows running the tests from the command line
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

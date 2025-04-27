"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出和为目标值 target
的那两个整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。你可以按任意顺序返回答案。

示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
示例 2：

输入：nums = [3,2,4], target = 6
输出：[1,2]
示例 3：

输入：nums = [3,3], target = 6
输出：[0,1]
"""
import unittest


def two_sum(nums: list[int], target: int) -> list[int]:
    """
    使用哈希表（字典）解决两数之和问题
    """
    # 创建一个哈希表（字典），用于存储已经遍历过的元素和它们的索引
    # 键: 元素的值
    # 值: 元素的索引
    hashmap = {}

    # 遍历数组 nums，同时获取元素的索引和值
    for i, num in enumerate(nums):
        # 计算当前元素 num 的“互补数”
        # 即需要找到的另一个数，使得它与 num 相加等于 target
        complement = target - num

        # 检查哈希表中是否已经存在这个互补数
        # 如果存在，说明我们找到了符合条件的两个数
        if complement in hashmap:
            # 返回互补数在哈希表中存储的索引（之前遍历过的）
            # 和当前元素的索引 i
            return [hashmap[complement], i]

        # 如果哈希表中不存在互补数，
        # 将当前元素 num 及其索引 i 存入哈希表
        # 供后续遍历的元素查找
        hashmap[num] = i

    # 根据题目假设，每种输入都恰好只有一个答案，所以理论上代码不会执行到这里
    # 如果题目允许无解，可以在这里返回空列表或抛出异常
    return []


class TestTwoSums(unittest.TestCase):

    def test_two_sum(self):
        self.assertEqual(two_sum(nums=[2, 7, 11, 15], target=9), [0, 1])
        self.assertEqual(two_sum(nums=[2, 7, 11, 15], target=9), [0, 1])
        self.assertEqual(two_sum(nums=[3, 3], target=6), [0, 1])

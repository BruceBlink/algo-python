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
    n = len(nums) # 获取输入数组的长度
    res = [-1] * n # 初始化结果列表，长度与 nums 相同，默认值为 -1 (表示没有找到更大元素)
    stack = []     # 初始化一个空列表作为栈，用于存储待处理元素的索引

    # 循环遍历两次数组，i 从 0 到 2*n - 1
    # 第一次遍历 (i 从 0 到 n-1) 处理正常的非循环情况
    # 第二次遍历 (i 从 n 到 2*n - 1) 处理循环到数组开头的情况
    for i in range(2 * n):
        # 计算当前遍历到的元素在原数组 (长度为 n) 中的实际索引
        # 例如，当 n=5, i=0..4 时 current_index = i
        # 当 n=5, i=5 时 current_index = 0
        # 当 n=5, i=6 时 current_index = 1
        current_index = i % n

        # 当栈不为空 并且 当前元素 nums[current_index] 大于 栈顶索引对应的元素 nums[stack[-1]] 时：
        # 这说明当前元素 nums[current_index] 是栈顶索引 stack[-1] 对应的元素的右边第一个更大的元素 (考虑循环)
        while stack and nums[current_index] > nums[stack[-1]]:
            # 弹出栈顶的索引 top
            # top 是之前某个元素的原始索引 (0 到 n-1)
            top = stack.pop()

            # 将当前元素 nums[current_index] 作为索引 top 对应元素的下一个更大元素
            # 记录在结果列表的 res[top] 位置
            res[top] = nums[current_index]

        # 循环结束后（栈为空，或者当前元素不大于栈顶元素）：
        # 将当前元素的**原始索引** current_index 压入栈中
        # 它现在是一个新的待处理的索引，等待未来出现比它更大的元素
        # 栈中存储的索引对应的元素是单调递减的 (因为只有比栈顶大的元素才会被弹出)
        stack.append(current_index)

    # 遍历完 2*n 次后，结果列表 res (长度为 n) 中存储的就是每个原始位置的下一个更大元素
    return res


class TestDailyNextGreaterElement(unittest.TestCase):

    def test_next_greater_element(self):
        self.assertEqual(next_greater_element([1, 2, 3, 4, 3]), [2, 3, 4, -1, 4])

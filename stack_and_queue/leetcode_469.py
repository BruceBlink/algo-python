"""
Next Greater Element I (下一个更大元素 I)(leetcode.496)
nums1 中数字 x 的 下一个更大元素 是指 x 在 nums2 中对应位置 右侧 的 第一个 比 x 大的元素。
给你两个 没有重复元素 的数组 nums1 和 nums2 ，下标从 0 开始计数，其中nums1 是 nums2 的子集。
对于每个 0 <= i < nums1.length ，找出满足 nums1[i] == nums2[j] 的下标 j ，
并且在 nums2 确定 nums2[j] 的 下一个更大元素 。如果不存在下一个更大元素，那么本次查询的答案是 -1 。
返回一个长度为 nums1.length 的数组 ans 作为答案，满足 ans[i] 是如上所述的 下一个更大元素 。

示例 1：
输入：nums1 = [4,1,2], nums2 = [1,3,4,2].
输出：[-1,3,-1]
解释：nums1 中每个值的下一个更大元素如下所述：
- 4 ，用加粗斜体标识，nums2 = [1,3,4,2]。不存在下一个更大元素，所以答案是 -1 。
- 1 ，用加粗斜体标识，nums2 = [1,3,4,2]。下一个更大元素是 3 。
- 2 ，用加粗斜体标识，nums2 = [1,3,4,2]。不存在下一个更大元素，所以答案是 -1 。
示例 2：
输入：nums1 = [2,4], nums2 = [1,2,3,4].
输出：[3,-1]
解释：nums1 中每个值的下一个更大元素如下所述：
- 2 ，用加粗斜体标识，nums2 = [1,2,3,4]。下一个更大元素是 3 。
- 4 ，用加粗斜体标识，nums2 = [1,2,3,4]。不存在下一个更大元素，所以答案是 -1 。

提示：

1 <= nums1.length <= nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 104
nums1和nums2中所有整数 互不相同
nums1 中的所有整数同样出现在 nums2 中
"""
import unittest


def next_greater_element(nums1: list[int], nums2: list[int]) -> list[int]:
    """
    使用单调栈和哈希表解决下一个更大元素 I
    """
    # 哈希表用于存储 nums2 中元素及其下一个更大元素的关系: {元素: 下一个更大元素}
    greater_map = {}
    # 单调递减栈，存储 nums2 中还没有找到下一个更大元素的元素
    stack = []  # 栈中存储的是 nums2 的元素值

    # 遍历 nums2，找到每个元素的下一个更大元素
    for num in nums2:
        # 当栈不为空，并且当前元素 num 大于栈顶元素时：
        # 说明栈顶元素找到了它的下一个更大元素，就是当前的 num
        while stack and num > stack[-1]:
            # 弹出栈顶元素
            top_element = stack.pop()
            # 记录这对关系到哈希表中
            greater_map[top_element] = num

        # 将当前元素压入栈中，等待它右边第一个更大的元素出现
        stack.append(num)

    # 遍历 nums1，根据哈希表找到对应的下一个更大元素
    res = []
    for num1 in nums1:
        # 从 greater_map 中查找 num1 的下一个更大元素
        # 使用 get 方法，如果 num1 不在 map 中，则返回默认值 -1
        res.append(greater_map.get(num1, -1))

    return res


class TestNextGreaterElement(unittest.TestCase):

    def test_next_greater_element(self):
        self.assertEqual(next_greater_element([4, 1, 2], [1, 3, 4, 2]), [-1, 3, -1])
        self.assertEqual(next_greater_element([2, 4], [1, 2, 3, 4]), [3, -1])

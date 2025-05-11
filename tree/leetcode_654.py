"""
654. 最大二叉树
给定一个不重复的整数数组 nums 。 最大二叉树 可以用下面的算法从 nums 递归地构建:

创建一个根节点，其值为 nums 中的最大值。
递归地在最大值 左边 的 子数组前缀上 构建左子树。
递归地在最大值 右边 的 子数组后缀上 构建右子树。
返回 nums 构建的 最大二叉树 。


示例 1：
输入：nums = [3,2,1,6,0,5]
输出：[6,3,5,null,2,0,null,null,1]
解释：递归调用如下所示：
- [3,2,1,6,0,5] 中的最大值是 6 ，左边部分是 [3,2,1] ，右边部分是 [0,5] 。
    - [3,2,1] 中的最大值是 3 ，左边部分是 [] ，右边部分是 [2,1] 。
        - 空数组，无子节点。
        - [2,1] 中的最大值是 2 ，左边部分是 [] ，右边部分是 [1] 。
            - 空数组，无子节点。
            - 只有一个元素，所以子节点是一个值为 1 的节点。
    - [0,5] 中的最大值是 5 ，左边部分是 [0] ，右边部分是 [] 。
        - 只有一个元素，所以子节点是一个值为 0 的节点。
        - 空数组，无子节点。

示例 2：
输入：nums = [3,2,1]
输出：[3,null,2,null,1]


提示：

1 <= nums.length <= 1000
0 <= nums[i] <= 1000
nums 中的所有整数 互不相同

"""
import unittest
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"[{self.val}]"  # 正确写法


# Helper function to build a binary tree from a level-order list representation
# 辅助函数：从层序列表表示构建二叉树 (复制自之前的问题)
def list_to_tree(values: list) -> TreeNode:
    """
    从一个表示层序遍历的列表构建二叉树。None 表示该位置没有节点。
    例如: [3,9,20,None,None,15,7] -> 对应的二叉树结构。
    """
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    n = len(values)

    while queue and i < n:
        current_node = queue.popleft()

        # 添加左子节点
        if i < n and values[i] is not None:
            current_node.left = TreeNode(values[i])
            queue.append(current_node.left)
        i += 1

        # 添加右子节点
        if i < n and values[i] is not None:
            current_node.right = TreeNode(values[i])
            queue.append(current_node.right)
        i += 1

    return root


# Helper function to compare two tree structures recursively
# 辅助函数：递归比较两个树结构是否完全相同
def are_trees_equal(root1: TreeNode, root2: TreeNode) -> bool:
    # 如果两个节点都为空，认为相等
    if root1 is None and root2 is None:
        return True

    # 如果一个为空，另一个不为空，认为不相等
    if root1 is None or root2 is None:
        return False

    # 如果两个节点值不相等，认为不相等
    if root1.val != root2.val:
        return False

    # 递归比较左子树和右子树
    return are_trees_equal(root1.left, root2.left) and are_trees_equal(root1.right, root2.right)


class Solution:

    def constructMaximumBinaryTree(self, nums: list[int]) -> TreeNode | None:
        # 递归辅助函数，处理 _nums 数组在索引范围 [l, r] 内构建最大二叉树
        def construct(_nums: list[int], l: int, r: int) -> TreeNode | None:
            # 基本情况：如果左边界大于右边界，说明当前范围为空，返回 None
            if l > r:
                return None

            # 1. 在当前范围内 [l, r] 找到最大值及其索引
            max_val = _nums[l]
            max_index = l
            for i in range(l + 1, r + 1):
                if _nums[i] > max_val:
                    max_val = _nums[i]
                    max_index = i

            # 2. 创建根节点
            root = TreeNode(max_val)

            # 3. 递归构建左子树 (范围是 [l, max_index - 1])
            root.left = construct(_nums, l, max_index - 1)

            # 4. 递归构建右子树 (范围是 [max_index + 1, r])
            root.right = construct(_nums, max_index + 1, r)

            # 5. 返回当前根节点
            return root

        # 调用递归辅助函数，处理整个数组范围 [0, len(nums) - 1]
        return construct(nums, 0, len(nums) - 1)

    def constructMaximumBinaryTree1(self, nums: list[int]) -> TreeNode | None:
        # 使用栈存储节点，栈中节点值递减
        stack = []

        # 遍历数组中的每一个数字
        for num in nums:
            # 为当前数字创建一个新节点
            curr = TreeNode(num)

            # 用于存储从栈中弹出的最后一个节点 (它将成为 curr 的左孩子)
            last_popped_smaller = None

            # While 循环：当栈不为空且栈顶节点值小于当前节点值
            while stack and stack[-1].val < curr.val:
                # 弹出栈顶节点
                last_popped_smaller = stack.pop()

            # While 循环结束后：
            # 如果 last_popped_smaller 不为 None，说明有节点被弹出，
            # 最后一个弹出的节点 (last_popped_smaller) 成为当前节点 curr 的左孩子
            if last_popped_smaller:
                curr.left = last_popped_smaller

            # 如果栈不为空，新的栈顶节点 (stack[-1]) 是第一个大于当前节点 curr 的左侧节点
            # curr 将成为它的右孩子
            if stack:
                stack[-1].right = curr

            # 将当前节点入栈
            stack.append(curr)

        # 遍历完成后，栈中应该只剩下一个节点，即为根节点
        # 如果 nums 为空，stack 也为空，返回 None
        return stack[0] if stack else None


# 使用 unittest.TestCase 编写单元测试
class TestConstructMaximumBinaryTree(unittest.TestCase):

    def test_example_1(self):
        # LeetCode 示例 1
        # Input: nums = [3,2,1,6,0,5]
        # 预期树的层序表示: [6, 3, 5, None, 2, 0, None, None, None, 1] (length 10)
        # Manual verification: 6(max), Left [3,2,1] -> 3(max), Left [], Right [2,1] -> 2(max), Left [], Right [1] -> 1(max), Left/Right []
        # Right [0,5] -> 5(max), Left [0], Right [] -> 0(max), Left/Right []
        # Correct Level order: 6, 3, 5, None(from 3's left), 2(from 3's right), 0(from 5's left), None(from 5's right), None(from 2's left), 1(from 2's right), None(from 0's left), None(from 0's right), ...
        # Let's use the Level order list from the example output: [6,3,5,null,null,0,null,null,null,null,null] - length 11.
        # Okay, re-checking diagram and rules, the correct level order is indeed:
        # Level 0: 6
        # Level 1: 3, 5
        # Level 2: N (3.left), 2 (3.right), 0 (5.left), N (5.right)
        # Level 3: N (2.left), 1 (2.right), N (0.left), N (0.right)
        # Level order: [6, 3, 5, None, 2, 0, None, None, 1, None, None, None, None] - length 13!
        # Example output [6,3,5,null,null,0,null,null,null,null,null] is confusingly short.
        # Let's trust the diagram and rules.
        # Expected level order list based on rules and diagram up to depth 3 leaves:
        expected_values = [6, 3, 5, None, 2, 0, None, None, 1, None, None, None, None]  # Length 13

        nums = [3, 2, 1, 6, 0, 5]
        # Build the expected tree from the level order list
        expected_root = list_to_tree(expected_values)

        solution = Solution()
        actual_root = solution.constructMaximumBinaryTree(nums)

        # Compare the actual and expected tree structures
        self.assertTrue(are_trees_equal(actual_root, expected_root))

    def test_empty_array(self):
        # Input: nums = []
        nums = []
        expected_root = None

        solution = Solution()
        actual_root = solution.constructMaximumBinaryTree(nums)

        self.assertTrue(are_trees_equal(actual_root, expected_root))

    def test_single_element(self):
        # Input: nums = [3]
        # Expected: [3]
        nums = [3]
        expected_root = list_to_tree([3])

        solution = Solution()
        actual_root = solution.constructMaximumBinaryTree(nums)

        self.assertTrue(are_trees_equal(actual_root, expected_root))

    def test_two_elements_decreasing(self):
        # Input: [3, 1]
        # Expected: [3, null, 1]
        nums = [3, 1]
        expected_root = list_to_tree([3, None, 1])

        solution = Solution()
        actual_root = solution.constructMaximumBinaryTree(nums)

        self.assertTrue(are_trees_equal(actual_root, expected_root))

    def test_two_elements_increasing(self):
        # Input: [1, 3]
        # Expected: [3, 1]
        nums = [1, 3]
        expected_root = list_to_tree([3, 1])

        solution = Solution()
        actual_root = solution.constructMaximumBinaryTree(nums)

        self.assertTrue(are_trees_equal(actual_root, expected_root))

    def test_increasing_array(self):
        # Input: [1, 2, 3, 4, 5]
        # Expected: [5, 4, null, 3, null, null, null, 2, null, null, null, null, null, null, null, 1]
        # Tree structure: 5 -> 4 -> 3 -> 2 -> 1 (right spine)
        expected_values = [5, 4, None, 3, None, None, None, 2, None, None, None, None, None, None, None, 1]
        # Need to pad with enough Nones for tree_to_list to work for comparison
        # For a depth 4 tree (root=5, leaves at depth 4), needs 2^5 - 1 = 31 nodes in level order representation.
        # Let's use a simpler structure comparison.
        # expected_root = list_to_tree(expected_values) # This is error prone with many Nones

        # Let's manually construct the expected tree for this simple case
        expected_root = TreeNode(5)
        expected_root.left = TreeNode(4)
        expected_root.left.left = TreeNode(3)
        expected_root.left.left.left = TreeNode(2)
        expected_root.left.left.left.left = TreeNode(1)

        nums = [1, 2, 3, 4, 5]
        solution = Solution()
        actual_root = solution.constructMaximumBinaryTree(nums)

        self.assertTrue(are_trees_equal(actual_root, expected_root))

    def test_decreasing_array(self):
        # Input: [5, 4, 3, 2, 1]
        # Expected: [5, null, 4, null, 3, null, 2, null, 1]
        # Tree structure: 5 -> 4 -> 3 -> 2 -> 1 (left spine)

        # Manually construct the expected tree
        expected_root = TreeNode(5)
        expected_root.right = TreeNode(4)
        expected_root.right.right = TreeNode(3)
        expected_root.right.right.right = TreeNode(2)
        expected_root.right.right.right.right = TreeNode(1)

        nums = [5, 4, 3, 2, 1]
        solution = Solution()
        actual_root = solution.constructMaximumBinaryTree(nums)

        self.assertTrue(are_trees_equal(actual_root, expected_root))


# This allows running the tests from the command line
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

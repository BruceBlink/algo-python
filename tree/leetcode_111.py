"""
111. 二叉树的最小深度

给定一个二叉树，找出其最小深度。
最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
说明：叶子节点是指没有子节点的节点。

示例 1：
输入：root = [3,9,20,null,null,15,7]
输出：2

示例 2：
输入：root = [2,null,3,null,4,null,5,null,6]
输出：5

提示：

树中节点数的范围在 [0, 10^5] 内
-1000 <= Node.val <= 1000
"""
import unittest
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Helper function to build a binary tree from a level-order list representation
# 辅助函数：从层序列表表示构建二叉树
def list_to_tree(values: list) -> TreeNode | None:
    """
    从一个表示层序遍历的列表构建二叉树。None 表示该位置没有节点。
    例如: [3,9,20,None,None,15,7] -> 对应的二叉树结构。
    """
    if not values or values[0] is None:
        return None

    # 创建根节点
    root = TreeNode(values[0])
    # 使用队列进行 BFS 构建
    queue = deque([root])
    # 用于跟踪 values 列表中的索引
    i = 1
    n = len(values)

    while queue and i < n:
        current_node = queue.popleft()

        # 添加左子节点
        if i < n and values[i] is not None:
            current_node.left = TreeNode(values[i])
            queue.append(current_node.left)
        i += 1  # 移动到下一个值，无论是否为 None

        # 添加右子节点
        if i < n and values[i] is not None:
            current_node.right = TreeNode(values[i])
            queue.append(current_node.right)
        i += 1  # 移动到下一个值

    return root


def min_depth_loop(root: TreeNode | None) -> int:
    """
    迭代
    """
    # 如果根节点为空，最小深度为 0
    if root is None:
        return 0

    # 使用队列进行 BFS，存储元组 (节点, 当前层级)
    queue = deque([(root, 1)])

    # 当队列不为空时循环
    while queue:
        # 从队列头部取出一个节点和它所在的层级
        node, level = queue.popleft()

        # 检查当前节点是否为叶子节点 (没有左孩子也没有右孩子)
        if node.left is None and node.right is None:
            # 找到了最近的叶子节点，返回当前层级
            return level

        # 如果不是叶子节点，将其非空的子节点加入队列
        if node.left is not None:
            queue.append((node.left, level + 1))

        if node.right is not None:
            queue.append((node.right, level + 1))


def min_depth_recursion(root: TreeNode | None) -> int:
    """
    递归
    """
    # 基本情况：如果节点为空，最小深度为 0
    if root is None:
        return 0

    # 递归计算左右子树的最小深度
    left_depth = min_depth_recursion(root.left)
    right_depth = min_depth_recursion(root.right)

    # --- 关键的几种情况处理 ---

    # 情况 1: 如果当前节点是叶子节点
    # (左右子树递归都返回 0，表示左右孩子都是 None)
    if left_depth == 0 and right_depth == 0:
        return 1  # 叶子节点的最小深度是 1 (从自身到自身)

    # 情况 2: 如果左孩子不存在 (左子树递归返回 0)
    # 说明从当前节点到叶子的最短路径必须通过右子树
    if left_depth == 0:
        # 最小深度 = 1 (当前节点) + 右子树的最小深度
        return 1 + right_depth

    # 情况 3: 如果右孩子不存在 (右子树递归返回 0)
    # 说明从当前节点到叶子的最短路径必须通过左子树
    if right_depth == 0:
        # 最小深度 = 1 (当前节点) + 左子树的最小深度
        return 1 + left_depth

    # 情况 4: 如果左右孩子都存在 (左右子树递归返回都大于 0)
    # 最小深度 = 1 (当前节点) + 左右子树最小深度的较小值
    return 1 + min(left_depth, right_depth)


# Unit tests using unittest.TestCase
# 使用 unittest.TestCase 编写单元测试
class TestMinDepth(unittest.TestCase):

    def test_example_1(self):
        # LeetCode 示例 1
        # Input: root = [3,9,20,null,null,15,7]
        # 结构:   3
        #        / \
        #       9  20
        #          / \
        #         15  7
        # 最短路径到叶子是 3 -> 9 (深度 2)
        values = [3, 9, 20, None, None, 15, 7]
        root = list_to_tree(values)
        expected_output = 2

        actual_output = min_depth_loop(root)
        self.assertEqual(actual_output, expected_output)

        actual_output = min_depth_recursion(root)
        self.assertEqual(actual_output, expected_output)

    def test_example_2(self):
        # LeetCode 示例 2: 只有右子树的斜树
        # Input: root = [2,null,3,null,4,null,5,null,6]
        # 结构: 2 -> 3 -> 4 -> 5 -> 6
        # 最短路径到叶子是 2 -> 3 -> 4 -> 5 -> 6 (深度 5)
        values = [2, None, 3, None, 4, None, 5, None, 6]
        root = list_to_tree(values)
        expected_output = 5

        actual_output = min_depth_loop(root)
        self.assertEqual(actual_output, expected_output)

        actual_output = min_depth_recursion(root)
        self.assertEqual(actual_output, expected_output)

    def test_empty_tree(self):
        # 空树的最小深度是 0
        # Input: root = [] (表示 None)
        values = []
        root = list_to_tree(values)
        expected_output = 0

        actual_output = min_depth_loop(root)
        self.assertEqual(actual_output, expected_output)

        actual_output = min_depth_recursion(root)
        self.assertEqual(actual_output, expected_output)

    def test_single_node(self):
        # 单个节点本身就是叶子节点，深度是 1
        # Input: root = [1]
        values = [1]
        root = list_to_tree(values)
        expected_output = 1

        actual_output = min_depth_loop(root)
        self.assertEqual(actual_output, expected_output)

        actual_output = min_depth_recursion(root)
        self.assertEqual(actual_output, expected_output)

    def test_simple_complete_tree(self):
        # 简单完全二叉树
        # Input: [1, 2, 3]
        # 结构:   1
        #        / \
        #       2   3
        # 叶子节点是 2 和 3，最短路径是 1 -> 2 或 1 -> 3 (深度都是 2)
        values = [1, 2, 3]
        root = list_to_tree(values)
        expected_output = 2

        actual_output = min_depth_loop(root)
        self.assertEqual(actual_output, expected_output)

        actual_output = min_depth_recursion(root)
        self.assertEqual(actual_output, expected_output)

    def test_left_branch_shorter(self):
        # 左边分支最短
        # Input: [1, 2, 3, 4, 5, null, null]
        # 结构:   1
        #        / \
        #       2   3
        #      / \
        #     4   5
        # 叶子节点 3 (深度 2), 4 (深度 3), 5 (深度 3)。最短是到 3 (深度 2)
        values = [1, 2, 3, 4, 5, None, None]
        root = list_to_tree(values)
        expected_output = 2

        actual_output = min_depth_loop(root)
        self.assertEqual(actual_output, expected_output)

        actual_output = min_depth_recursion(root)
        self.assertEqual(actual_output, expected_output)

    def test_right_branch_shorter(self):
        # 右边分支最短
        # Input: [1, 2, 3, null, null, 4, 5]
        # 结构:   1
        #        / \
        #       2   3
        #          / \
        #         4   5
        # 叶子节点 2 (深度 2), 4 (深度 3), 5 (深度 3)。最短是到 2 (深度 2)
        values = [1, 2, 3, None, None, 4, 5]
        root = list_to_tree(values)
        expected_output = 2

        actual_output = min_depth_loop(root)
        self.assertEqual(actual_output, expected_output)

        actual_output = min_depth_recursion(root)
        self.assertEqual(actual_output, expected_output)

    def test_zig_zag_to_leaf(self):
        # Z 字形到叶子节点
        # Input: [1, 2, null, 3, null, 4, null, 5]
        # 结构:   1
        #        /
        #       2
        #        \
        #         3
        #        /
        #       4
        #        \
        #         5  (叶子)
        # 最短路径 1 -> 2 -> 3 -> 4 -> 5 (深度 5)
        values = [1, 2, None, 3, None, 4, None, 5]
        root = list_to_tree(values)
        expected_output = 5

        actual_output = min_depth_loop(root)
        self.assertEqual(actual_output, expected_output)

        actual_output = min_depth_recursion(root)
        self.assertEqual(actual_output, expected_output)

"""
101. 对称二叉树

给你一个二叉树的根节点 root ， 检查它是否轴对称。

示例 1：
输入：root = [1,2,2,3,4,4,3]
输出：true

示例 2：
输入：root = [1,2,2,null,3,null,3]
输出：false

提示：

树中节点数目在范围 [1, 1000] 内
-100 <= Node.val <= 100
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


def is_symmetric(root: TreeNode | None) -> bool:
    """
    迭代
    """
    # 空树是对称的
    if root is None:
        return True

    # 使用队列存储成对的节点
    queue = deque([root.left, root.right])  # 将根节点的左右孩子成对放入队列

    # 当队列不为空时循环
    while queue:
        # 每次取出成对的两个节点进行比较
        left_node = queue.popleft()
        right_node = queue.popleft()

        # 基本情况 1: 两个节点都为空，是对称的，继续下一对
        if left_node is None and right_node is None:
            continue

        # 基本情况 2: 一个为空，另一个不为空，不对称
        if left_node is None or right_node is None:
            return False

        # 基本情况 3: 两个节点的值不相等，不对称
        if left_node.val != right_node.val:
            return False

        # 将下一层对称位置的节点成对加入队列
        # 左子树的左孩子 与 右子树的右孩子
        queue.append(left_node.left)
        queue.append(right_node.right)

        # 左子树的右孩子 与 右子树的左孩子
        queue.append(left_node.right)
        queue.append(right_node.left)

    # 循环结束都没有发现不对称的情况，说明是对称的
    return True


def is_symmetric1(root: TreeNode | None) -> bool:
    """
    递归
    """

    # 辅助函数：检查两个节点是否互为镜像
    def is_mirror(left_node: TreeNode, right_node: TreeNode) -> bool:
        # 基本情况 1: 两个节点都为空，互为镜像
        if left_node is None and right_node is None:
            return True

        # 基本情况 2: 一个为空，另一个不为空，不互为镜像
        if left_node is None or right_node is None:
            return False

        # 基本情况 3: 两个节点的值不相等，不互为镜像
        if left_node.val != right_node.val:
            return False

        # 递归检查外侧节点对 (左子树的左孩子 vs 右子树的右孩子)
        outer_pair_is_mirror = is_mirror(left_node.left, right_node.right)

        # 递归检查内侧节点对 (左子树的右孩子 vs 右子树的左孩子)
        inner_pair_is_mirror = is_mirror(left_node.right, right_node.left)

        # 只有当外侧和内侧节点对都互为镜像时，当前这对节点才互为镜像
        return outer_pair_is_mirror and inner_pair_is_mirror

    if not root:
        return True
    return is_mirror(root.left, root.right)


class TestIsSymmetric(unittest.TestCase):

    def test_example_1(self):
        # LeetCode 示例 1: 标准对称树
        # Input: root = [1,2,2,3,4,4,3]
        values = [1, 2, 2, 3, 4, 4, 3]
        root = list_to_tree(values)
        expected_output = True

        actual_output = is_symmetric(root)

        self.assertEqual(actual_output, expected_output)

        actual_output = is_symmetric1(root)

        self.assertEqual(actual_output, expected_output)

    def test_example_2(self):
        # LeetCode 示例 2: 标准非对称树
        # Input: root = [1,2,2,null,3,null,3]
        # 结构:   1
        #        / \
        #       2   2
        #      / \ / \
        #     N  3 N  3
        values = [1, 2, 2, None, 3, None, 3]
        root = list_to_tree(values)
        expected_output = False

        actual_output = is_symmetric(root)

        self.assertEqual(actual_output, expected_output)

        actual_output = is_symmetric1(root)

        self.assertEqual(actual_output, expected_output)

    def test_empty_tree(self):
        # 空树是对称的
        # Input: root = [] (表示 None)
        values = []
        root = list_to_tree(values)
        expected_output = True

        actual_output = is_symmetric(root)

        self.assertEqual(actual_output, expected_output)

        actual_output = is_symmetric1(root)

        self.assertEqual(actual_output, expected_output)

    def test_single_node(self):
        # 单个节点是对称的
        # Input: root = [1]
        values = [1]
        root = list_to_tree(values)
        expected_output = True

        actual_output = is_symmetric(root)

        self.assertEqual(actual_output, expected_output)

        actual_output = is_symmetric1(root)

        self.assertEqual(actual_output, expected_output)

    def test_simple_symmetric(self):
        # 简单对称树 (只有根和两个子节点)
        # Input: [1, 2, 2]
        values = [1, 2, 2]
        root = list_to_tree(values)
        expected_output = True

        actual_output = is_symmetric(root)

        self.assertEqual(actual_output, expected_output)

        actual_output = is_symmetric1(root)

        self.assertEqual(actual_output, expected_output)

    def test_simple_asymmetric_values(self):
        # 简单非对称树 (子节点值不同)
        # Input: [1, 2, 3]
        values = [1, 2, 3]
        root = list_to_tree(values)
        expected_output = False

        actual_output = is_symmetric(root)

        self.assertEqual(actual_output, expected_output)

        actual_output = is_symmetric1(root)

        self.assertEqual(actual_output, expected_output)

    def test_asymmetric_structure_right_only(self):
        # 非对称结构 (只有右子节点)
        # Input: [1, null, 2]
        values = [1, None, 2]
        root = list_to_tree(values)
        expected_output = False

        actual_output = is_symmetric(root)

        self.assertEqual(actual_output, expected_output)

        actual_output = is_symmetric1(root)

        self.assertEqual(actual_output, expected_output)

    def test_asymmetric_structure_left_only(self):
        # 非对称结构 (只有左子节点)
        # Input: [1, 2, null]
        values = [1, 2, None]
        root = list_to_tree(values)
        expected_output = False

        actual_output = is_symmetric(root)

        self.assertEqual(actual_output, expected_output)

        actual_output = is_symmetric1(root)

        self.assertEqual(actual_output, expected_output)

    def test_complex_symmetric(self):
        # 复杂对称树 (LeetCode 例子之外)
        # Input: [9,-42,-42,null,76,76,null,null,13,null,13]
        # 结构:   9
        #        / \
        #      -42 -42
        #      / \ / \
        #     N  76 76 N
        #       / \/ \
        #      13 N 13 N  (left child of first 76 is 13, right is N; left of second 76 is 13, right is N)
        # Careful: [9,-42,-42,null,76,76,null,null,13,null,13] list means:
        # Level 0: 9
        # Level 1: -42, -42
        # Level 2: None (left of first -42), 76 (right of first -42), 76 (left of second -42), None (right of second -42)
        # Level 3: 13 (left of first 76), None (right of first 76), 13 (left of second 76), None (right of second 76)
        # Correct Structure:
        #        9
        #       / \
        #     -42 -42
        #     / \ / \
        #    N  76 76 N
        #       / \/ \
        #      13 N 13 N <--- My previous trace had the 13s misplaced based on the list.
        # Let's re-check symmetric pairs for the correct structure:
        # - Roots (-42,-42): Match.
        # - Left -42's left (N) vs Right -42's right (N): Match.
        # - Left -42's right (76) vs Right -42's left (76): Match.
        #   - Check is_mirror(node 76, node 76)
        #     - Values 76==76. Match.
        #     - Left 76's left (13) vs Right 76's right (N): NO MATCH! Values differ, structures differ. This should be False.
        # My previous trace was wrong. The list representation leads to an asymmetric tree.

        values = [9, -42, -42, None, 76, 76, None, None, 13, None, 13]
        root = list_to_tree(values)
        expected_output = False  # This tree is NOT symmetric

        actual_output = is_symmetric(root)

        self.assertEqual(actual_output, expected_output)

        actual_output = is_symmetric1(root)

        self.assertEqual(actual_output, expected_output)

"""
104. 二叉树的最大深度

给定一个二叉树 root ，返回其最大深度。

二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。


示例 1：
输入：root = [3,9,20,null,null,15,7]
输出：3

示例 2：
输入：root = [1,null,2]
输出：2

提示：

树中节点的数量在 [0, 104] 区间内。
-100 <= Node.val <= 100
"""
import unittest
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth_loop(root: TreeNode | None) -> int:
    """
    迭代
    """
    from collections import deque
    if not root:
        return 0
    depth, queue = 0, deque([root])
    while queue:
        depth += 1
        length = len(queue)  # 当前层的节点数
        for _ in range(length):
            current_level_node = queue.popleft()
            if current_level_node.left:
                queue.append(current_level_node.left)
            if current_level_node.right:
                queue.append(current_level_node.right)
    return depth


def max_depth_recursion(root: TreeNode | None) -> int:
    """
    递归
    """
    if not root:
        return 0
    return max(max_depth_recursion(root.left), max_depth_recursion(root.right)) + 1


class TestMaxDepth(unittest.TestCase):

    def test_empty_tree(self):
        # 空树应该返回深度 0
        self.assertEqual(max_depth_recursion(None), 0)
        self.assertEqual(max_depth_loop(None), 0)

    def test_single_node(self):
        # 单节点树深度为 1
        root = TreeNode(1)
        self.assertEqual(max_depth_recursion(root), 1)
        self.assertEqual(max_depth_loop(root), 1)

    def test_balanced_tree(self):
        # 平衡树:       1
        #             /   \
        #            2     3
        #           / \   / \
        #          4   5 6   7
        root = TreeNode(1,
                        TreeNode(2, TreeNode(4), TreeNode(5)),
                        TreeNode(3, TreeNode(6), TreeNode(7)))
        self.assertEqual(max_depth_recursion(root), 3)
        self.assertEqual(max_depth_loop(root), 3)

    def test_unbalanced_tree(self):
        # 不平衡树: 1 -> right -> right
        root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
        self.assertEqual(max_depth_recursion(root), 3)
        self.assertEqual(max_depth_loop(root), 3)

    def test_left_heavy_tree(self):
        # 左重树: 1 -> left -> left -> left
        root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
        self.assertEqual(max_depth_recursion(root), 4)
        self.assertEqual(max_depth_loop(root), 4)

    def test_mixed_tree(self):
        # 混合结构
        #      1
        #     / \
        #    2   3
        #         \
        #          4
        #         / \
        #        5   6
        root = TreeNode(1,
                        TreeNode(2),
                        TreeNode(3, None, TreeNode(4, TreeNode(5), TreeNode(6))))
        self.assertEqual(max_depth_recursion(root), 4)
        self.assertEqual(max_depth_loop(root), 4)

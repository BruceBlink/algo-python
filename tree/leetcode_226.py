"""
226. 翻转二叉树
给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。


示例 1：
输入：root = [4,2,7,1,3,6,9]
输出：[4,7,2,9,6,3,1]

示例 2：
输入：root = [2,1,3]
输出：[2,3,1]

示例 3：
输入：root = []
输出：[]


提示：

树中节点数目范围在 [0, 100] 内
-100 <= Node.val <= 100

"""
import unittest
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree_loop(root: TreeNode | None) -> TreeNode | None:
    """
    迭代 BFS
    """
    if root is None:
        return None
    from collections import deque
    queue = deque([root])
    while queue:
        current_node = queue.popleft()
        current_node.left, current_node.right = current_node.right, current_node.left
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
    return root


def invert_tree_recursion(root: TreeNode | None) -> TreeNode | None:
    """
    递归 DFS
    """
    if not root:
        return None
    left = invert_tree_recursion(root.left)
    right = invert_tree_recursion(root.right)
    root.left, root.right = right, left
    return root


def tree_to_list(root):
    """层序遍历转列表，None 用 None 占位"""
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # 去掉末尾多余的 None
    while result and result[-1] is None:
        result.pop()
    return result


def build(vals):
    """按层序列表构造二叉树"""
    if not vals:
        return None
    nodes = [TreeNode(v) if v is not None else None for v in vals]
    kid_idx = 1
    for idx, node in enumerate(nodes):
        if node:
            if kid_idx < len(nodes):
                node.left = nodes[kid_idx]
                kid_idx += 1
            if kid_idx < len(nodes):
                node.right = nodes[kid_idx]
                kid_idx += 1
    return nodes[0]


class TestInvertTree(unittest.TestCase):

    def test_example1(self):
        root = build([4, 2, 7, 1, 3, 6, 9])
        inverted = invert_tree_loop(root)
        self.assertEqual(tree_to_list(inverted), [4, 7, 2, 9, 6, 3, 1])

        inverted = invert_tree_recursion(root)
        self.assertEqual(tree_to_list(inverted), [4, 2, 7, 1, 3, 6, 9])

    def test_empty(self):
        self.assertIsNone(invert_tree_loop(None))
        self.assertIsNone(invert_tree_recursion(None))

    def test_single(self):
        root = TreeNode(1)
        inverted = invert_tree_loop(root)
        self.assertEqual(tree_to_list(inverted), [1])

        inverted = invert_tree_recursion(root)
        self.assertEqual(tree_to_list(inverted), [1])

    def test_left_chain(self):
        root = build([1, 2, None, 3, None, 4])
        inverted = invert_tree_loop(root)
        # 变为右链
        self.assertEqual(tree_to_list(inverted), [1, None, 2, None, 3, None, 4])

        inverted = invert_tree_recursion(root)
        self.assertEqual(tree_to_list(inverted), [1, 2, None, 3, None, 4])

    def test_right_chain(self):
        root = build([1, None, 2, None, 3, None, 4])
        inverted = invert_tree_loop(root)
        # 变为左链
        self.assertEqual(tree_to_list(inverted), [1, 2, None, 3, None, 4])

        inverted = invert_tree_recursion(root)
        self.assertEqual(tree_to_list(inverted), [1, None, 2, None, 3, None, 4])

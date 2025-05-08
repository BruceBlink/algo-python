"""
543. 二叉树的直径

给你一棵二叉树的根节点，返回该树的 直径 。
二叉树的 直径 是指树中任意两个节点之间最长路径的 长度 。这条路径可能经过也可能不经过根节点 root 。
两节点之间路径的 长度 由它们之间边数表示。

示例 1：
输入：root = [1,2,3,4,5]
输出：3
解释：3 ，取路径 [4,2,1,3] 或 [5,2,1,3] 的长度。

示例 2：
输入：root = [1,2]
输出：1

提示：

树中节点数目在范围 [1, 104] 内
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


def diameter_of_binary_tree(root: TreeNode | None) -> int:
    """
    递归
    """
    diameter = 0

    def max_depth(node: TreeNode | None) -> int:
        nonlocal diameter  # ← 把外层 diameter 拿进来
        if not node:
            return 0
        left_d = max_depth(node.left)
        right_d = max_depth(node.right)
        # 经过 node 的最长路径是左右深度之和
        diameter = max(diameter, left_d + right_d)
        # 返回从 node 向下的最大深度
        return max(left_d, right_d) + 1

    max_depth(root)
    return diameter


def diameter_of_binary_tree_iter(root: TreeNode | None) -> int:
    if not root:
        return 0

    # 存放节点深度的字典：node -> depth
    depth = {None: 0}
    diameter = 0

    # 栈中元素：(node, visited_flag)
    # visited_flag=False 表示第一次见到，需要先处理子节点
    # visited_flag=True  表示子节点已处理完，可以计算深度并更新直径
    stack = [(root, False)]

    while stack:
        node, visited = stack.pop()
        if node is None:
            continue

        if not visited:
            # 后序：先标记自己，稍后再处理
            stack.append((node, True))
            # 先右再左入栈，这样出栈时先处理左子树，再右，再自己
            stack.append((node.right, False))
            stack.append((node.left, False))
        else:
            # 左右深度都已在 depth 中
            left_d = depth[node.left]
            right_d = depth[node.right]
            # 更新直径：经过当前节点的最长路径 = left_d + right_d
            diameter = max(diameter, left_d + right_d)
            # 记录当前节点深度
            depth[node] = max(left_d, right_d) + 1

    return diameter


def build_tree(vals: list[int]):
    """
    从列表构建二叉树（按层序），其中 None 表示空节点。
    返回根节点。
    """
    if not vals:
        return None
    nodes = [None if v is None else TreeNode(v) for v in vals]
    kid_idx = 1
    for idx, node in enumerate(nodes):
        if node is not None:
            if kid_idx < len(nodes):
                node.left = nodes[kid_idx]
                kid_idx += 1
            if kid_idx < len(nodes):
                node.right = nodes[kid_idx]
                kid_idx += 1
    return nodes[0]


class TestDiameterOfBinaryTree(unittest.TestCase):

    def test_empty_tree(self):
        root = None
        self.assertEqual(diameter_of_binary_tree(root), 0)
        self.assertEqual(diameter_of_binary_tree_iter(root), 0)

    def test_single_node(self):
        root = TreeNode(1)
        self.assertEqual(diameter_of_binary_tree(root), 0)
        self.assertEqual(diameter_of_binary_tree_iter(root), 0)

    def test_two_nodes(self):
        #   1
        #    \
        #     2
        root = TreeNode(1, right=TreeNode(2))
        self.assertEqual(diameter_of_binary_tree(root), 1)
        self.assertEqual(diameter_of_binary_tree_iter(root), 1)

    def test_example1(self):
        #      1
        #     / \
        #    2   3
        #   / \
        #  4   5
        vals = [1, 2, 3, 4, 5]
        root = build_tree(vals)
        # 最长路径是 4-2-1-3 或 5-2-1-3，边数为 3
        self.assertEqual(diameter_of_binary_tree(root), 3)
        self.assertEqual(diameter_of_binary_tree_iter(root), 3)

    def test_unbalanced(self):
        #      1
        #     /
        #    2
        #   /
        #  3
        # /
        #4
        vals = [1, 2, None, 3, None, 4]
        root = build_tree(vals)
        # 最长路径是 4-3-2-1，边数为 3
        self.assertEqual(diameter_of_binary_tree(root), 3)
        self.assertEqual(diameter_of_binary_tree_iter(root), 3)

    def test_full_tree(self):
        # 完全二叉树深度 3
        vals = [1, 2, 3, 4, 5, 6, 7]
        root = build_tree(vals)
        # 最长路径在最左叶到最右叶：4-2-1-3-7，边数为 4
        self.assertEqual(diameter_of_binary_tree(root), 4)
        self.assertEqual(diameter_of_binary_tree_iter(root), 4)

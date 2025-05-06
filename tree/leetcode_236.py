"""
236. 二叉树的最近公共祖先
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，
最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”


示例 1：

输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出：3
解释：节点 5 和节点 1 的最近公共祖先是节点 3 。
示例 2：


输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出：5
解释：节点 5 和节点 4 的最近公共祖先是节点 5 。因为根据定义最近公共祖先节点可以为节点本身。
示例 3：

输入：root = [1,2], p = 1, q = 2
输出：1


提示：

树中节点数目在范围 [2, 10^5] 内。
-10^9 <= Node.val <= 10^9
所有 Node.val 互不相同 。
p != q
p 和 q 均存在于给定的二叉树中。
"""
import unittest
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 辅助函数：从层序列表表示构建二叉树，并返回节点值到节点对象的映射字典
def list_to_tree_with_nodes(values: list):
    """
    从一个表示层序遍历的列表构建二叉树。None 表示该位置没有节点。
    同时返回一个字典，将节点值映射到对应的节点对象。
    注意：如果树中存在重复的节点值，这个字典只会存储最后遇到的该值的节点对象。
    对于 LeetCode 236，p 和 q 的值通常是唯一的，或者通过问题约束保证了可以唯一找到 p 和 q 节点。
    """
    if not values or values[0] is None:
        return None, {}

    root = TreeNode(values[0])
    queue = deque([root])
    node_map = {values[0]: root}  # 存储值到节点的映射

    i = 1
    n = len(values)

    while queue and i < n:
        current_node = queue.popleft()

        # 添加左子节点
        if i < n and values[i] is not None:
            current_node.left = TreeNode(values[i])
            queue.append(current_node.left)
            node_map[values[i]] = current_node.left  # 添加到映射
        i += 1

        # 添加右子节点
        if i < n and values[i] is not None:
            current_node.right = TreeNode(values[i])
            queue.append(current_node.right)
            node_map[values[i]] = current_node.right  # 添加到映射
        i += 1

    return root, node_map


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode | None:
    # 基本情况 1: 如果当前节点为空，或者当前节点就是 p 或 q，则返回当前节点
    # 如果是 p 或 q，那么它自己就是它和它的后代（另一个节点或它自己）的 LCA
    if root is None or root == p or root == q:
        return root

    # 递归查找左子树中的 LCA
    left_lca = lowest_common_ancestor(root.left, p, q)

    # 递归查找右子树中的 LCA
    right_lca = lowest_common_ancestor(root.right, p, q)

    # 情况 1: 如果左子树和右子树都找到了 LCA (即都不为 None)
    # 说明 p 和 q 分别在当前节点的左右子树中，那么当前节点就是它们的 LCA
    if left_lca and right_lca:
        return root

    # 情况 2: 如果只有左子树找到了 LCA (right_lca is None)
    # 说明 p 和 q 都在左子树中，或者左子树包含 p 或 q 且另一个是其后代
    # 此时左子树返回的结果就是 LCA
    # if left_lca is not None:
    #     return left_lca
    #
    # # 情况 3: 如果只有右子树找到了 LCA (left_lca is None)
    # # 说明 p 和 q 都在右子树中，或者右子树包含 p 或 q 且另一个是其后代
    # # 此时右子树返回的结果就是 LCA
    # if right_lca is not None:
    #     return right_lca

    # 情况 4: 如果左右子树都没有找到 (left_lca is None and right_lca is None)
    # 说明 p 和 q 都不在以当前节点为根的子树中，返回 None
    return right_lca or left_lca


class TestLowestCommonAncestor(unittest.TestCase):

    def test_example_1(self):
        # LeetCode 示例 1
        # Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
        values = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
        root, node_map = list_to_tree_with_nodes(values)

        # 根据值获取 p, q 节点对象 和 预期 LCA 节点对象
        p = node_map[5]
        q = node_map[1]
        expected_lca = node_map[3]  # 预期是节点 3

        result = lowest_common_ancestor(root, p, q)

        # 断言返回的节点对象是否是预期的 LCA 节点对象（通过对象引用判断）
        self.assertEqual(result, expected_lca)
        # 可选：检查值以增加清晰度
        if result:
            self.assertEqual(result.val, 3)

    def test_example_2(self):
        # LeetCode 示例 2: p 是 q 的祖先
        # Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
        values = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
        root, node_map = list_to_tree_with_nodes(values)

        p = node_map[5]
        q = node_map[4]
        expected_lca = node_map[5]  # 预期是节点 5 (p 本身)

        result = lowest_common_ancestor(root, p, q)

        self.assertEqual(result, expected_lca)
        if result:
            self.assertEqual(result.val, 5)

    def test_p_is_root(self):
        # p 是根节点
        # Input: root = [3,5,1], p = 3, q = 5
        values = [3, 5, 1]
        root, node_map = list_to_tree_with_nodes(values)

        p = node_map[3]
        q = node_map[5]
        expected_lca = node_map[3]  # 预期是根节点 3

        result = lowest_common_ancestor(root, p, q)

        self.assertEqual(result, expected_lca)
        if result:
            self.assertEqual(result.val, 3)

    def test_p_and_q_in_same_subtree(self):
        # p 和 q 都在左/右子树中，但不是祖先后代关系
        # Input: root = [1, 2, 3, 4, 5, 6, 7], p = 4, q = 5
        values = [1, 2, 3, 4, 5, 6, 7]
        root, node_map = list_to_tree_with_nodes(values)

        p = node_map[4]
        q = node_map[5]
        expected_lca = node_map[2]  # 预期是节点 2

        result = lowest_common_ancestor(root, p, q)

        self.assertEqual(result, expected_lca)
        if result:
            self.assertEqual(result.val, 2)

    def test_p_and_q_in_different_subtrees_deeper(self):
        # p 和 q 在不同子树中，且位置较深
        # Input: root = [1, 2, 3, 4, 5, 6, 7], p = 4, q = 6
        values = [1, 2, 3, 4, 5, 6, 7]
        root, node_map = list_to_tree_with_nodes(values)

        p = node_map[4]
        q = node_map[6]
        expected_lca = node_map[1]  # 预期是节点 1 (根节点)

        result = lowest_common_ancestor(root, p, q)

        self.assertEqual(result, expected_lca)
        if result:
            self.assertEqual(result.val, 1)

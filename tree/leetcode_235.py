"""
235. 二叉搜索树的最近公共祖先

给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，
满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]

示例 1:

输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
输出: 6
解释: 节点 2 和节点 8 的最近公共祖先是 6。
示例 2:

输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
输出: 2
解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。


说明:

所有节点的值都是唯一的。
p、q 为不同节点且均存在于给定的二叉搜索树中。

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


def lowest_common_ancestor_bst(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode | None:
    # 如果 p 和 q 都在左子树
    if max(p.val, q.val) < root.val:
        return lowest_common_ancestor_bst(root.left, p, q)
    # 如果 p 和 q 都在右子树
    elif min(p.val, q.val) > root.val:
        return lowest_common_ancestor_bst(root.right, p, q)
    # 否则，当前节点就是 LCA (p 和 q 跨越当前节点，或其中一个是当前节点)
    else:
        return root


def lowest_common_ancestor_bst_1(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode | None:
    current = root
    while current:
        # 如果 p 和 q 都在左子树
        if max(p.val, q.val) < current.val:
            current = current.left
        # 如果 p 和 q 都在右子树
        elif min(p.val, q.val) > current.val:
            current = current.right
        # 否则，当前节点就是 LCA
        else:
            return current  # 找到 LCA，返回当前节点


class TestLowestCommonAncestorBST(unittest.TestCase):

    def test_example_1(self):
        # LeetCode 示例 1: 标准情况
        # Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
        values = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
        root, node_map = list_to_tree_with_nodes(values)

        # 根据值获取 p, q 节点对象 和 预期 LCA 节点对象
        p = node_map[2]
        q = node_map[8]
        expected_lca = node_map[6]  # 预期是节点 6

        result = lowest_common_ancestor_bst(root, p, q)

        # 断言返回的节点对象是否是预期的 LCA 节点对象（通过对象引用判断）
        self.assertEqual(result, expected_lca)
        # 可选：检查值以增加清晰度
        if result:
            self.assertEqual(result.val, 6)

        result = lowest_common_ancestor_bst_1(root, p, q)
        self.assertEqual(result, expected_lca)
        # 可选：检查值以增加清晰度
        if result:
            self.assertEqual(result.val, 6)

    def test_example_2(self):
        # LeetCode 示例 2: p 是 q 的祖先
        # Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
        values = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
        root, node_map = list_to_tree_with_nodes(values)

        p = node_map[2]
        q = node_map[4]
        expected_lca = node_map[2]  # 预期是节点 2 (p 本身)

        result = lowest_common_ancestor_bst(root, p, q)

        # 断言返回的节点对象是否是预期的 LCA 节点对象（通过对象引用判断）
        self.assertEqual(result, expected_lca)
        # 可选：检查值以增加清晰度
        if result:
            self.assertEqual(result.val, 2)

        result = lowest_common_ancestor_bst_1(root, p, q)
        self.assertEqual(result, expected_lca)
        # 可选：检查值以增加清晰度
        if result:
            self.assertEqual(result.val, 2)

    def test_q_is_p_ancestor(self):
        # q 是 p 的祖先 (类似于 example 2，但 p, q 顺序不同)
        # Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 4, q = 2
        values = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
        root, node_map = list_to_tree_with_nodes(values)

        p = node_map[4]
        q = node_map[2]
        expected_lca = node_map[2]  # 预期是节点 2 (q 本身)

        result = lowest_common_ancestor_bst(root, p, q)

        # 断言返回的节点对象是否是预期的 LCA 节点对象（通过对象引用判断）
        self.assertEqual(result, expected_lca)
        # 可选：检查值以增加清晰度
        if result:
            self.assertEqual(result.val, 2)

        result = lowest_common_ancestor_bst_1(root, p, q)
        self.assertEqual(result, expected_lca)
        # 可选：检查值以增加清晰度
        if result:
            self.assertEqual(result.val, 2)

    def test_both_in_left_subtree_deeper(self):
        # p 和 q 都在左子树中，且位置较深
        # Input: root = [4,2,7,1,3,6,9], p = 1, q = 3
        values = [4, 2, 7, 1, 3, 6, 9]
        root, node_map = list_to_tree_with_nodes(values)

        p = node_map[1]
        q = node_map[3]
        expected_lca = node_map[2]  # 预期是节点 2

        result = lowest_common_ancestor_bst(root, p, q)

        # 断言返回的节点对象是否是预期的 LCA 节点对象（通过对象引用判断）
        self.assertEqual(result, expected_lca)
        # 可选：检查值以增加清晰度
        if result:
            self.assertEqual(result.val, 2)

        result = lowest_common_ancestor_bst_1(root, p, q)
        self.assertEqual(result, expected_lca)
        # 可选：检查值以增加清晰度
        if result:
            self.assertEqual(result.val, 2)

    def test_both_in_right_subtree_deeper(self):
        # p 和 q 都在右子树中，且位置较深
        # Input: root = [4,2,7,1,3,6,9], p = 6, q = 9
        values = [4, 2, 7, 1, 3, 6, 9]
        root, node_map = list_to_tree_with_nodes(values)

        p = node_map[6]
        q = node_map[9]
        expected_lca = node_map[7]  # 预期是节点 7

        result = lowest_common_ancestor_bst(root, p, q)

        # 断言返回的节点对象是否是预期的 LCA 节点对象（通过对象引用判断）
        self.assertEqual(result, expected_lca)
        # 可选：检查值以增加清晰度
        if result:
            self.assertEqual(result.val, 7)

        result = lowest_common_ancestor_bst_1(root, p, q)
        self.assertEqual(result, expected_lca)
        # 可选：检查值以增加清晰度
        if result:
            self.assertEqual(result.val, 7)

    def test_p_q_straddle_root(self):
        # p 和 q 分别在根节点的左右子树中
        # Input: root = [4,2,7,1,3,6,9], p = 1, q = 6
        values = [4, 2, 7, 1, 3, 6, 9]
        root, node_map = list_to_tree_with_nodes(values)

        p = node_map[1]
        q = node_map[6]
        expected_lca = node_map[4]  # 预期是节点 4 (根节点)

        result = lowest_common_ancestor_bst(root, p, q)

        # 断言返回的节点对象是否是预期的 LCA 节点对象（通过对象引用判断）
        self.assertEqual(result, expected_lca)
        # 可选：检查值以增加清晰度
        if result:
            self.assertEqual(result.val, 4)

        result = lowest_common_ancestor_bst_1(root, p, q)
        self.assertEqual(result, expected_lca)
        # 可选：检查值以增加清晰度
        if result:
            self.assertEqual(result.val, 4)

    def test_p_q_straddle_intermediate_node(self):
        # p 和 q 分别在中间节点的左右子树中
        # Input: root = [4,2,7,1,3,6,9], p = 1, q = 3
        values = [4, 2, 7, 1, 3, 6, 9]
        root, node_map = list_to_tree_with_nodes(values)

        p = node_map[1]
        q = node_map[3]
        expected_lca = node_map[2]  # 预期是节点 2

        result = lowest_common_ancestor_bst(root, p, q)

        # 断言返回的节点对象是否是预期的 LCA 节点对象（通过对象引用判断）
        self.assertEqual(result, expected_lca)
        # 可选：检查值以增加清晰度
        if result:
            self.assertEqual(result.val, 2)

        result = lowest_common_ancestor_bst_1(root, p, q)
        self.assertEqual(result, expected_lca)
        # 可选：检查值以增加清晰度
        if result:
            self.assertEqual(result.val, 2)

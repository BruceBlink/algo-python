"""
102. 二叉树的层序遍历
给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。

示例 1：
输入：root = [3,9,20,null,null,15,7]
输出：[[3],[9,20],[15,7]]

示例 2：
输入：root = [1]
输出：[[1]]
示例 3：

输入：root = []
输出：[]

提示：

树中节点数目在范围 [0, 2000] 内
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
def list_to_tree(values: list) -> TreeNode:
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


def level_order_loop(root: TreeNode | None) -> list[list[int]]:
    """
    迭代
    """
    if root is None:
        return []

    result = []
    # 使用双端队列 (deque) 作为队列
    queue = deque([root])

    while queue:
        # 获取当前层级的节点数量
        level_size = len(queue)
        # 存储当前层级的值
        current_level_values = []

        # 遍历当前层级的节点
        for _ in range(level_size):
            node = queue.popleft()
            current_level_values.append(node.val)

            # 将子节点（如果存在）加入队列
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # 将当前层级的值列表添加到结果中
        result.append(current_level_values)

    return result


def level_order_recursion(root: TreeNode | None) -> list[list[int]]:
    """
    递归
    """

    def dfs(level: int, node: TreeNode):
        if not node:
            return
        # 如果当前层级 >= 结果列表的大小，说明是第一次到达这一层
        # 需要为这一层在结果列表中添加一个新的空列表
        if level >= len(result):
            result.append([])
        result[level].append(node.val)
        dfs(level + 1, node.left)
        dfs(level + 1, node.right)

    result = []
    dfs(0, root)
    return result


# 使用 unittest.TestCase 编写单元测试
class TestLevelOrder(unittest.TestCase):

    def test_example_1(self):
        # LeetCode 示例 1
        # Input: root = [3,9,20,None,None,15,7]
        values = [3, 9, 20, None, None, 15, 7]
        root = list_to_tree(values)
        expected_output = [[3], [9, 20], [15, 7]]

        actual_output = level_order_loop(root)

        self.assertEqual(actual_output, expected_output)

        actual_output1 = level_order_recursion(root)
        self.assertEqual(actual_output1, expected_output)

    def test_single_node(self):
        # 单个节点
        # Input: root = [1]
        values = [1]
        root = list_to_tree(values)
        expected_output = [[1]]

        actual_output = level_order_loop(root)

        self.assertEqual(actual_output, expected_output)

        actual_output1 = level_order_recursion(root)
        self.assertEqual(actual_output1, expected_output)

    def test_empty_tree(self):
        # 空树
        # Input: root = [] (表示 None)
        values = []  # list_to_tree([]) 会返回 None
        root = list_to_tree(values)
        expected_output = []

        actual_output = level_order_loop(root)

        self.assertEqual(actual_output, expected_output)

        actual_output1 = level_order_recursion(root)
        self.assertEqual(actual_output1, expected_output)

    def test_complete_tree(self):
        # 完整二叉树
        # Input: [1, 2, 3, 4, 5, 6, 7]
        values = [1, 2, 3, 4, 5, 6, 7]
        root = list_to_tree(values)
        expected_output = [[1], [2, 3], [4, 5, 6, 7]]

        actual_output = level_order_loop(root)

        self.assertEqual(actual_output, expected_output)

        actual_output1 = level_order_recursion(root)
        self.assertEqual(actual_output1, expected_output)

    def test_right_skewed_tree(self):
        # 右斜树
        # Input: [1, null, 2, null, 3]
        values = [1, None, 2, None, 3]
        root = list_to_tree(values)
        expected_output = [[1], [2], [3]]

        actual_output = level_order_loop(root)

        self.assertEqual(actual_output, expected_output)

        actual_output1 = level_order_recursion(root)
        self.assertEqual(actual_output1, expected_output)

    def test_left_skewed_tree_with_gaps(self):
        # 左斜树带空节点
        # Input: [1, 2, null, 3, null, 4]
        values = [1, 2, None, 3, None, 4]  # 注意这里的 None 位置对应右子节点，但构建时按层序填充
        root = list_to_tree(values)
        expected_output = [[1], [2], [3], [4]]

        actual_output = level_order_loop(root)

        self.assertEqual(actual_output, expected_output)

        actual_output1 = level_order_recursion(root)
        self.assertEqual(actual_output1, expected_output)

"""
94. 二叉树的中序遍历

给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。

示例 1：
输入：root = [1,null,2,3]
输出：[1,3,2]

示例 2：
输入：root = []
输出：[]

示例 3：
输入：root = [1]
输出：[1]

提示：

树中节点数目在范围 [0, 100] 内
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


def inorder_traversal_loop(root: TreeNode | None) -> list[int]:
    """
    迭代
    """
    result = []  # 存储中序遍历结果的列表
    stack = []  # 模拟递归调用栈
    current = root  # 当前正在处理的节点，从根节点开始

    # 循环条件：当前节点不为空 或者 栈不为空
    # 这确保了即使当前节点为空，只要栈里还有未处理的父节点/右子树，循环就继续
    while current or stack:
        # 阶段一：尽可能地向左走，并将路径上的节点入栈
        while current is not None:
            stack.append(current)  # 将当前节点入栈
            current = current.left  # 移向左子节点

        # 阶段二：左侧路径走到底了，弹出节点，访问，并转向右子树
        current = stack.pop()  # 弹出栈顶节点（当前子树的最左侧节点或已处理完左子树的根节点）
        result.append(current.val)  # 访问节点，将值添加到结果中

        # 转向当前节点的右子节点
        current = current.right

    return result


def inorder_traversal_recursion(root: TreeNode | None) -> None | list[int]:
    """
    递归
    """
    result = []

    def inorder_recursive(node):
        if node is None:
            return

        # 递归遍历左子树
        inorder_recursive(node.left)

        # 访问根节点
        result.append(node.val)

        # 递归遍历右子树
        inorder_recursive(node.right)

    inorder_recursive(root)
    return result


class TestInorderTraversal(unittest.TestCase):

    def test_example_1(self):
        # LeetCode 示例 1
        # Input: root = [1,null,2,3]
        values = [1, None, 2, 3]
        root = list_to_tree(values)
        # 中序遍历: 左(None) -> 根(1) -> 右(2 -> 左(3) -> 根(2) -> 右(None))
        # 实际遍历顺序: None, 1, 3, 2, None -> [1, 3, 2] ??? 还是 trace 错了
        # Correct trace:
        # inorder(1): call inorder(None) -> return. Add 1. Call inorder(2).
        # inorder(2): call inorder(3).
        # inorder(3): call inorder(None) -> return. Add 3. Call inorder(None) -> return. Return from inorder(3).
        # Back in inorder(2): Add 2. Call inorder(None) -> return. Return from inorder(2).
        # Back in inorder(1): Return from inorder(2). Return from inorder(1).
        # Result: [1, 3, 2] -> Still confused by the diagram vs trace.
        # Let's double check the example's implied structure.
        # [1, null, 2, 3] means:
        #      1
        #       \
        #        2
        #       /
        #      3
        # Inorder: Left (of 1) -> 1 -> Right (of 1)
        # Left of 1 is None.
        # Right of 1 is node 2. Inorder(2): Left (of 2) -> 2 -> Right (of 2).
        # Left of 2 is node 3. Inorder(3): Left (of 3) -> 3 -> Right (of 3).
        # Left of 3 is None. Visit 3. Right of 3 is None. Return from inorder(3).
        # Back at inorder(2): Left (inorder(3)) finished. Visit 2. Right (of 2) is None. Return from inorder(2).
        # Back at inorder(1): Right (inorder(2)) finished.
        # Order of visits: 3, 2, 1. So expected is [3, 2, 1].
        # Let's trust the LeetCode example output itself. Example 1 output is [1,3,2].
        # This means the list representation [1,null,2,3] must represent:
        #      1
        #       \
        #        2
        #       /
        #      3
        # This IS the structure. My manual trace must be wrong. Let's use the standard definition: L-Root-R.
        # inorder(1): Left (None). Visit 1. Right (Node 2).
        #   inorder(2): Left (Node 3). Visit 2. Right (None).
        #     inorder(3): Left (None). Visit 3. Right (None).
        # Okay, the Visits happen *after* the left recursive call returns.
        # inorder(1):
        #   inorder(1.left) -> return
        #   Add 1 to result -> result = [1]
        #   inorder(1.right) -> call inorder(2)
        #     inorder(2.left) -> call inorder(3)
        #       inorder(3.left) -> return
        #       Add 3 to result -> result = [1, 3]
        #       inorder(3.right) -> return
        #     Return from inorder(3).
        #     Add 2 to result -> result = [1, 3, 2]
        #     inorder(2.right) -> return
        #   Return from inorder(2).
        # Return from inorder(1).
        # Result [1, 3, 2]. OK, the LeetCode example output [1,3,2] matches my final trace. The list representation [1,null,2,3] *does* build the tree correctly, and my trace confirms the standard inorder on that structure gives [1,3,2]. The confusion was my initial trace error.

        expected_output = [1, 3, 2]

        actual_output = inorder_traversal_recursion(root)

        self.assertEqual(actual_output, expected_output)

        actual_output1 = inorder_traversal_loop(root)
        self.assertEqual(actual_output1, expected_output)

    def test_empty_tree(self):
        # 空树
        # Input: root = [] (表示 None)
        values = []
        root = list_to_tree(values)
        expected_output = []

        actual_output = inorder_traversal_recursion(root)

        self.assertEqual(actual_output, expected_output)

    def test_single_node(self):
        # 单个节点
        # Input: root = [1]
        values = [1]
        root = list_to_tree(values)
        expected_output = [1]

        actual_output = inorder_traversal_recursion(root)

        self.assertEqual(actual_output, expected_output)

        actual_output1 = inorder_traversal_loop(root)
        self.assertEqual(actual_output1, expected_output)

    def test_complete_tree(self):
        # 完整二叉树
        # Input: [1, 2, 3]
        values = [1, 2, 3]
        root = list_to_tree(values)
        # 中序: 左(2) -> 根(1) -> 右(3) -> [2, 1, 3]
        expected_output = [2, 1, 3]

        actual_output = inorder_traversal_recursion(root)

        self.assertEqual(actual_output, expected_output)

        actual_output1 = inorder_traversal_loop(root)
        self.assertEqual(actual_output1, expected_output)

    def test_right_child_only(self):
        # 只有右子节点
        # Input: [1, null, 2]
        values = [1, None, 2]
        root = list_to_tree(values)
        # 中序: 左(None) -> 根(1) -> 右(2) -> [1, 2]
        expected_output = [1, 2]

        actual_output = inorder_traversal_recursion(root)

        self.assertEqual(actual_output, expected_output)

        actual_output1 = inorder_traversal_loop(root)
        self.assertEqual(actual_output1, expected_output)

    def test_left_child_only(self):
        # 只有左子节点
        # Input: [2, 1, null]
        values = [2, 1, None]
        root = list_to_tree(values)
        # 中序: 左(1) -> 根(2) -> 右(None) -> [1, 2]
        expected_output = [1, 2]

        actual_output = inorder_traversal_recursion(root)

        self.assertEqual(actual_output, expected_output)

        actual_output1 = inorder_traversal_loop(root)
        self.assertEqual(actual_output1, expected_output)

    def test_larger_tree(self):
        # 较大的树 (看起来是 BST，中序是排序的)
        # Input: [3,1,5,0,2,4,6]
        values = [3, 1, 5, 0, 2, 4, 6]
        root = list_to_tree(values)
        # 中序: 0, 1, 2, 3, 4, 5, 6
        expected_output = [0, 1, 2, 3, 4, 5, 6]

        actual_output = inorder_traversal_recursion(root)

        self.assertEqual(actual_output, expected_output)

        actual_output1 = inorder_traversal_loop(root)
        self.assertEqual(actual_output1, expected_output)

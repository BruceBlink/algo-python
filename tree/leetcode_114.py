"""
114. 二叉树展开为链表

给你二叉树的根结点 root ，请你将它展开为一个单链表：
展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
展开后的单链表应该与二叉树 先序遍历 顺序相同。

示例 1：
输入：root = [1,2,5,3,4,null,6]
输出：[1,null,2,null,3,null,4,null,5,null,6]

示例 2：
输入：root = []
输出：[]

示例 3：
输入：root = [0]
输出：[0]

提示：

树中结点数在范围 [0, 2000]内
-100 <= Node.val <= 100

进阶：你可以使用原地算法（O(1) 额外空间）展开这棵树吗？
"""

import unittest
from collections import deque  # list_to_tree 函数需要用到 deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"[{self.val}]"  # 正确写法

    def __repr__(self):
        return f"[{self.val}]"


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


# Helper function to convert a linked list (or a flattened tree) to a list of values
# 辅助函数：将链表（或展平的树）转换为值的列表
def linked_list_to_list(head: TreeNode) -> list:
    values = []
    current = head
    # 展平后的树，左指针应为 None，右指针连接下一个节点
    while current is not None:
        values.append(current.val)
        # 展平后只沿着 right 指针前进
        current = current.right
    return values


# The Solution class with the flatten method (using iterative O(1) space approach)
# Solution 类，包含 flatten 方法 (使用基于 O(1) 空间的迭代方法)
class Solution:
    def __init__(self):
        # 初始化一个类成员变量，用于存储前一个被展平并处理好的节点
        # (在反向前序遍历的顺序下)
        self.prev = None

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        current = root

        # 当 current 不为空时循环
        while current:
            # 如果 current 有左孩子
            if current.left is not None:
                # 找到左子树中最右边的节点 (predecessor)
                predecessor = current.left
                # 寻找最右边的节点，直到其 right 指针为 None
                while predecessor.right is not None:
                    predecessor = predecessor.right

                # 将左子树的最右边节点的 right 指针指向 current 原来的 right 子树的根
                predecessor.right = current.right

                # 将 current 的 right 指针指向 current 原来的 left 子树的根
                current.right = current.left

                # 将 current 的 left 指针设为 None
                current.left = None

            # 移动 current 到下一个节点 (已经处理好的节点的右指针指向下一个)
            current = current.right

        # 方法原地修改，无需返回

    def flatten1(self, root: TreeNode) -> None:
        if not root:
            return
        self.flatten1(root.left)
        self.flatten1(root.right)
        # 至此左右子树都被拉成链表
        left, right = root.left, root.right
        # 将左子书变为右子树，置空左子树
        root.left, root.right = None, left
        # 将原来的右子树，拼接到现在的右子树的后面
        p = root
        while p.right:
            p = p.right
        p.right = right

    # 处理顺序是 右子树 -> 左子树 -> 根节点 (反向前序遍历)
    def flatten1_optimized(self, node: TreeNode):
        # 基本情况：如果当前节点是空的，说明到达叶子节点的下方，停止递归
        if node is None:
            return

        # --- 递归步骤 (反向前序遍历的顺序) ---

        # 1. 【最重要】递归展平右子树
        # 先处理右子树。当这个递归调用返回时，整个右子树已经被展平了，
        # 并且 self.prev 会指向这个展平后的右子树链表的【头部】（因为右子树也是反向构建的）
        # 如果右子树是 None，调用会立即返回，self.prev 保持不变
        self.flatten1_optimized(node.right)

        # 2. 递归展平左子树
        # 再处理左子树。当这个递归调用返回时，整个左子树已经被展平了，
        # 并且 self.prev 会指向这个展平后的左子树链表的【头部】
        # （注意：这里的 self.prev 是在处理完右子树后传进来的那个 self.prev，现在更新了）
        # 如果左子树是 None，调用会立即返回，self.prev 保持不变 (它此时指向右子树的头部或更早的节点)
        self.flatten1_optimized(node.left)

        # 3. 【最核心的连接步骤】处理当前节点 (在左右子树都展平后)
        # 当代码执行到这里时，当前节点 node 的左右子树都已经按反向前序遍历的顺序展平了。
        # 此时的 self.prev 指向的是：
        # - 如果左子树非空，self.prev 指向展平后的左子树链表的头部。
        # - 如果左子树为空，self.prev 指向展平后的右子树链表的头部（或者更早的节点，如果右子树也为空/小）。
        # 无论哪种情况，这个 self.prev 正好是最终展平链表中，紧跟在当前 node 后面的那个节点！

        # 当前节点的右指针应该指向 self.prev (即最终链表中跟在它后面的节点)
        node.right = self.prev

        # 当前节点的左指针设为 None (符合链表的定义)
        node.left = None

        # 更新 self.prev 为当前节点 node
        # 当前节点 node 现在是刚刚被处理好的节点，它成为了下一个（即调用当前函数的那个父节点）处理时，需要指向的“前一个节点”。
        self.prev = node


# Unit tests using unittest.TestCase
# 使用 unittest.TestCase 编写单元测试
class TestFlatten(unittest.TestCase):

    def test_example_1(self):
        # LeetCode 示例 1
        # Input: root = [1,2,5,3,4,null,6]
        # 原始结构:   1
        #           / \
        #          2   5
        #         / \   \
        #        3   4   6
        # 前序遍历顺序: 1, 2, 3, 4, 5, 6
        # 展平后链表: 1 -> 2 -> 3 -> 4 -> 5 -> 6
        values = [1, 2, 5, 3, 4, None, 6]
        root = list_to_tree(values)
        expected_output = [1, 2, 3, 4, 5, 6]

        solution = Solution()
        # solution.flatten(root)  # 方法原地修改
        solution.flatten1_optimized(root)
        # 将展平后的树结构（从原始 root 开始）转换为列表进行比较
        actual_output = linked_list_to_list(root)

        self.assertEqual(actual_output, expected_output)

    def test_empty_tree(self):
        # 空树
        # Input: root = [] (表示 None)
        values = []
        root = list_to_tree(values)
        expected_output = []

        solution = Solution()
        solution.flatten(root)

        actual_output = linked_list_to_list(root)

        self.assertEqual(actual_output, expected_output)

    def test_single_node(self):
        # 单个节点
        # Input: root = [0]
        values = [0]
        root = list_to_tree(values)
        expected_output = [0]

        solution = Solution()
        solution.flatten(root)

        actual_output = linked_list_to_list(root)

        self.assertEqual(actual_output, expected_output)

    def test_left_child_only(self):
        # 只有左子节点
        # Input: [1, 2, null]
        # 结构:   1
        #        /
        #       2
        # 前序: 1, 2
        # 展平: 1 -> 2
        values = [1, 2, None]
        root = list_to_tree(values)
        expected_output = [1, 2]

        solution = Solution()
        solution.flatten(root)

        actual_output = linked_list_to_list(root)

        self.assertEqual(actual_output, expected_output)

    def test_right_child_only(self):
        # 只有右子节点
        # Input: [1, null, 2]
        # 结构:   1
        #         \
        #          2
        # 前序: 1, 2
        # 展平: 1 -> 2
        values = [1, None, 2]
        root = list_to_tree(values)
        expected_output = [1, 2]

        solution = Solution()
        solution.flatten(root)

        actual_output = linked_list_to_list(root)

        self.assertEqual(actual_output, expected_output)

    def test_simple_tree(self):
        # 简单树 (根左右)
        # Input: [1, 2, 3]
        # 结构:   1
        #        / \
        #       2   3
        # 前序: 1, 2, 3
        # 展平: 1 -> 2 -> 3
        values = [1, 2, 3]
        root = list_to_tree(values)
        expected_output = [1, 2, 3]

        solution = Solution()
        solution.flatten(root)

        actual_output = linked_list_to_list(root)

        self.assertEqual(actual_output, expected_output)

    def test_complete_tree(self):
        # 完整二叉树
        # Input: [1, 2, 3, 4, 5, 6, 7]
        # 结构:   1
        #        / \
        #       2   3
        #      / \ / \
        #     4  5 6  7
        # 前序: 1, 2, 4, 5, 3, 6, 7
        # 展平: 1 -> 2 -> 4 -> 5 -> 3 -> 6 -> 7
        values = [1, 2, 3, 4, 5, 6, 7]
        root = list_to_tree(values)
        expected_output = [1, 2, 4, 5, 3, 6, 7]

        solution = Solution()
        solution.flatten(root)

        actual_output = linked_list_to_list(root)

        self.assertEqual(actual_output, expected_output)


# This allows running the tests from the command line
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

"""
106. 从中序与后序遍历序列构造二叉树

给定两个整数数组 inorder 和 postorder ，其中 inorder 是二叉树的中序遍历， postorder 是同一棵树的后序遍历，请你构造并返回这颗 二叉树 。

示例 1:
输入：inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
输出：[3,9,20,null,null,15,7]

示例 2:
输入：inorder = [-1], postorder = [-1]
输出：[-1]


提示:

1 <= inorder.length <= 3000
postorder.length == inorder.length
-3000 <= inorder[i], postorder[i] <= 3000
inorder 和 postorder 都由 不同 的值组成
postorder 中每一个值都在 inorder 中
inorder 保证是树的中序遍历
postorder 保证是树的后序遍历
"""

import unittest
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"[{self.val}]"  # 正确写法


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


# Helper function to compare two tree structures recursively
# 辅助函数：递归比较两个树结构是否完全相同 (复制自之前的问题)
def are_trees_equal(root1: TreeNode, root2: TreeNode) -> bool:
    # 如果两个节点都为空，认为相等
    if root1 is None and root2 is None:
        return True

    # 如果一个为空，另一个不为空，认为不相等
    if root1 is None or root2 is None:
        return False

    # 如果两个节点值不相等，认为不相等
    if root1.val != root2.val:
        return False

    # 递归比较左子树和右子树
    return are_trees_equal(root1.left, root2.left) and are_trees_equal(root1.right, root2.right)


class Solution:
    def __init__(self):
        self.inorder_map = None
        self.postorder_index = None

    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:

        def build(inorder_start: int, inorder_end: int) -> TreeNode | None:
            # 4. 基本情况：如果中序范围无效，返回 None
            if inorder_start > inorder_end:
                return None

            # 5. 创建根节点：当前子树的根是后序数组中 self.postorder_index 指向的元素
            root_val = postorder[self.postorder_index]  # 使用成员变量 postorder
            root = TreeNode(root_val)

            # 6. 更新后序索引：指向下一个需要处理的根节点 (向前移动)
            self.postorder_index -= 1

            # 7. 找到根节点在中序数组中的位置
            root_inorder_index = self.inorder_map[root_val]

            # 8. 递归构建右子树 (在中序数组中，根节点右边的部分 [root_inorder_index + 1, inorder_end])
            # 【关键】先构建右子树，因为它在后序遍历中紧跟在左子树后面，在根节点前面
            # 而我们是从后序数组的末尾向前处理的
            root.right = build(root_inorder_index + 1, inorder_end)

            # 9. 递归构建左子树 (在中序数组中，根节点左边的部分 [inorder_start, root_inorder_index - 1])
            root.left = build(inorder_start, root_inorder_index - 1)

            # 10. 返回当前根节点
            return root

        # 处理空输入数组
        if not inorder or not postorder:
            return None

        # 1. 预处理：创建中序数组 值 -> 索引 的映射
        self.inorder_map = {val: i for i, val in enumerate(inorder)}

        # 2. 初始化后序数组的索引指针，从最后一个元素开始
        self.postorder_index = len(postorder) - 1

        # 3. 调用递归辅助函数，构建整棵树 (初始范围对应整个中序数组)
        return build(0, len(inorder) - 1)


# 使用 unittest.TestCase 编写单元测试
class TestBuildTree(unittest.TestCase):

    def test_example_1(self):
        # LeetCode 示例 1
        # Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
        # 预期树的层序表示: [3, 9, 20, None, None, 15, 7]
        inorder = [9, 3, 15, 20, 7]
        postorder = [9, 15, 7, 20, 3]
        expected_values = [3, 9, 20, None, None, 15, 7]
        expected_root = list_to_tree(expected_values)

        solution = Solution()
        actual_root = solution.buildTree(inorder, postorder)

        # 比较实际和预期的树结构
        self.assertTrue(are_trees_equal(actual_root, expected_root))

    def test_empty_arrays(self):
        # 输入为空数组
        inorder = []
        postorder = []
        expected_root = None

        solution = Solution()
        actual_root = solution.buildTree(inorder, postorder)

        self.assertTrue(are_trees_equal(actual_root, expected_root))

    def test_single_node(self):
        # 单个节点
        inorder = [1]
        postorder = [1]
        expected_root = list_to_tree([1])

        solution = Solution()
        actual_root = solution.buildTree(inorder, postorder)

        self.assertTrue(are_trees_equal(actual_root, expected_root))

    def test_two_nodes_left_child(self):
        # 两个节点，左孩子
        # inorder = [2, 1], postorder = [2, 1] -> 1 是根 (后序末尾), 2 在 1 左边 (中序), 2 在 1 前面 (后序) -> 2 是 1 的左孩子
        inorder = [2, 1]
        postorder = [2, 1]
        expected_values = [1, 2] # Tree: 1 -> left 2
        expected_root = list_to_tree(expected_values)

        solution = Solution()
        actual_root = solution.buildTree(inorder, postorder)

        self.assertTrue(are_trees_equal(actual_root, expected_root))

    def test_two_nodes_right_child(self):
        # 两个节点，右孩子
        # inorder = [1, 2], postorder = [2, 1] -> 1 是根 (后序末尾), 2 在 1 右边 (中序), 2 在 1 前面 (后序) -> 2 是 1 的右孩子
        inorder = [1, 2]
        postorder = [2, 1]
        expected_values = [1, None, 2] # Tree: 1 -> right 2
        expected_root = list_to_tree(expected_values)

        solution = Solution()
        actual_root = solution.buildTree(inorder, postorder)

        self.assertTrue(are_trees_equal(actual_root, expected_root))

    def test_simple_tree(self):
        # 简单树
        # inorder = [1, 2, 3, 4], postorder = [2, 1, 4, 3]
        # Root 3 (后序末尾). Inorder [1,2] | 3 | [4]. Left in [1,2], Right in [4]. Post root used, Right post [4], Left post [2,1].
        # Build right from in=[4], post=[4]: Root 4. Returns node(4). Right of 3 is 4.
        # Build left from in=[1,2], post=[2,1]: Root 1 (后序末尾). Inorder [1] | 2. Left in [], Right in [2]. Post root used, Right post [2], Left post []. Build right from in=[2], post=[2]: Root 2. Returns node(2). Right of 1 is 2. Build left from in=[], post=[]: Returns None. Left of 1 None. Tree 1 -> right 2. Left of 3 is (1 -> right 2).
        # 结构:   3
        #        / \
        #       1   4
        #        \
        #         2
        # 层序: [3, 1, 4, None, 2]
        inorder = [1, 2, 3, 4]
        postorder = [2, 1, 4, 3]
        expected_values = [3, 1, 4, None, 2]
        expected_root = list_to_tree(expected_values)

        solution = Solution()
        actual_root = solution.buildTree(inorder, postorder)

        self.assertTrue(are_trees_equal(actual_root, expected_root))

    def test_complex_tree(self):
        # 复杂一些的树
        # inorder = [1, 2, 3, 4, 5], postorder = [1, 3, 2, 5, 4]
        # Root 4 (后序末尾). Inorder [1,2,3] | 4 | [5]. Left in [1,2,3], Right in [5]. Post root used, Right post [5], Left post [1,3,2].
        # Build right from in=[5], post=[5]: Root 5. Returns node(5). Right of 4 is 5.
        # Build left from in=[1,2,3], post=[1,3,2]: Root 2 (后序末尾). Inorder [1] | 2 | [3]. Left in [1], Right in [3]. Post root used, Right post [3], Left post [1].
        #   Build right from in=[3], post=[3]: Root 3. Returns node(3). Right of 2 is 3.
        #   Build left from in=[1], post=[1]: Root 1. Returns node(1). Left of 2 is 1.
        #   Tree from [1,2,3], [1,3,2]: 2 -> left 1, right 3. Left of 4 is (2 -> left 1, right 3).
        # 结构:   4
        #        / \
        #       2   5
        #      / \
        #     1   3
        # 层序: [4, 2, 5, 1, 3]
        inorder = [1, 2, 3, 4, 5]
        postorder = [1, 3, 2, 5, 4]
        expected_values = [4, 2, 5, 1, 3]
        expected_root = list_to_tree(expected_values)

        solution = Solution()
        actual_root = solution.buildTree(inorder, postorder)

        self.assertTrue(are_trees_equal(actual_root, expected_root))


# This allows running the tests from the command line
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
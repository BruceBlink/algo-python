"""
116. 填充每个节点的下一个右侧节点指针
给定一个 完美二叉树 ，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
初始状态下，所有 next 指针都被设置为 NULL。

示例 1：
输入：root = [1,2,3,4,5,6,7]
输出：[1,#,2,3,#,4,5,6,7,#]
解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。序列化的输出按层序遍历排列，同一层节点由 next 指针连接，'#' 标志着每一层的结束。

示例 2:
输入：root = []
输出：[]

提示：

树中节点的数量在 [0, 212 - 1] 范围内
-1000 <= node.val <= 1000


进阶：

你只能使用常量级额外空间。
使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。

"""

import unittest
from collections import deque


# Definition for a Node. (题目自带)
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def __str__(self):
        return f"[{self.val}]"  # 正确写法


# Helper function to build a PERFECT binary tree (using Node class) from a level-order list representation
# 辅助函数：从层序列表表示构建完美的 Node 二叉树
def list_to_perfect_node_tree(values: list) -> Node:
    """
    从一个表示层序遍历的列表构建完美二叉树 (使用 Node 类)。
    注意：此函数假定输入列表表示一个有效的完美二叉树。
    """
    if not values or values[0] is None:
        return None

    root = Node(values[0])
    queue = deque([root])
    i = 1
    n = len(values)

    while queue and i < n:
        current_node = queue.popleft()

        # 在完美二叉树中，如果一个节点有左孩子，它一定有右孩子，且下一层都会被填满直到叶子层
        # 因此，我们通常可以简化构建逻辑，直接按顺序取值赋给 left 和 right
        # 但为了通用性（即使输入列表包含 None），沿用之前的逻辑更稳妥

        # 添加左子节点
        if i < n and values[i] is not None:
            current_node.left = Node(values[i])
            queue.append(current_node.left)
        i += 1

        # 添加右子节点
        if i < n and values[i] is not None:
            current_node.right = Node(values[i])
            queue.append(current_node.right)
        i += 1

    return root


# Helper function to convert a perfect binary tree with populated 'next' pointers to a list of lists (level by level)
# 辅助函数：将填充了 next 指针的完美二叉树转换为按层级的列表列表
def perfect_node_tree_to_level_list(root: Node) -> list[list[int]]:
    levels = []
    if not root:
        return levels

    # 从根节点开始，它是第一层的最左边节点
    leftmost = root

    # 当当前层的最左边节点不为空时，处理这一层
    # 同时，由于是完美二叉树，如果最左边节点存在，且它不是叶子层，它的 left 孩子一定存在
    while leftmost:
        current_level_values = []
        # current 指针用于遍历当前层的节点
        current = leftmost

        # 沿着当前层的 next 指针遍历所有节点
        while current:
            current_level_values.append(current.val)
            # 移动到当前层的下一个节点 (通过 next 指针)
            current = current.next

        # 将当前层的值列表添加到结果中
        levels.append(current_level_values)

        # 移动到下一层的最左边节点
        # 如果当前 leftmost 有 left 孩子 (即它不是叶子层)，那么它的 left 孩子就是下一层的最左边节点
        # 如果是叶子层，leftmost.left 将是 None，外层 while 循环将终止
        leftmost = leftmost.left

    return levels


# The Solution class with the connect method (using iterative BFS approach)
# Solution 类，包含 connect 方法 (使用基于 BFS 的迭代方法，之前验证为正确)
class Solution:
    def connect(self, root: Node | None) -> Node | None:
        """
        递归实现
        """

        # 辅助递归函数，用于连接 node1.next = node2，并递归处理下一层的相关节点对
        # node1 和 node2 是一对在当前层中【应该连接】起来的相邻节点 (或者都是 None)
        def traverse(node1: Node | None, node2: Node | Node):
            # 基本情况：如果任一节点为空，则它们无法连接，停止递归
            if not node1 or not node2:
                return

            # 【核心连接】将 node1 的 next 指向 node2
            # 因为传入的 node1 和 node2 就是当前需要连接的一对节点
            node1.next = node2

            # 【递归调用】处理下一层的相关节点对
            # 现在 node1 和 node2 已经连接好了 (node1.next = node2)
            # 我们需要递归地去处理下一层需要连接的节点对
            # 下一层需要连接的节点对有哪些呢？
            # 1. node1 的子节点：node1.left 和 node1.right 是相邻的，需要连接
            traverse(node1.left, node1.right)

            # 2. node2 的子节点：node2.left 和 node2.right 是相邻的，需要连接
            traverse(node2.left, node2.right)

            # 3. 跨越父节点的连接：node1 的右孩子 和 node2 的左孩子 是相邻的，需要连接
            # node1 和 node2 本身通过 next 连接，它们的右孩子和左孩子是下一层相邻的节点
            traverse(node1.right, node2.left)

        # 主函数入口
        if not root:
            return None

        # 从根节点的左右孩子开始调用
        # 第一次调用 traverse(root.left, root.right)
        # 这会将 root.left.next 设置为 root.right
        # 并开始递归处理下一层 (root.left 和 root.right 的孩子层) 的连接
        traverse(root.left, root.right)

        # 根节点的 next 保持 None (题目要求)
        return root

    def connect1(self, root: Node | None) -> Node | None:
        """
        BFS 层序遍历
        """
        from collections import deque
        # 1. 基本情况：处理空树
        if not root:
            return None

        # 2. 初始化队列，将根节点加入队列
        # 队列用于 BFS (层序遍历)
        queue = deque([root])

        # 3. 主循环：当队列不为空时，继续处理
        # 每一轮外层 while 循环处理一层
        while queue:
            # 4. 获取当前层级的节点数量
            size = len(queue)
            # size 在进入内层 for 循环之前固定，代表当前层有多少节点需要处理

            # 5. 内层循环：遍历当前层级的每一个节点
            for i in range(size):
                # 6. 从队列头部取出一个节点
                node = queue.popleft()  # 取出当前层的第 i+1 个节点

                # 7. 设置当前节点的 next 指针
                # 如果当前节点不是当前层的最后一个节点 (i < size - 1)
                if i < size - 1:
                    # 将当前节点的 next 指向队列的头部
                    # 【核心逻辑】此时 queue 的头部 (queue[0]) 恰好是当前层级的下一个节点
                    # 这是因为在 for 循环中，当前层级剩余的节点（从 i+1 到 size-1）还在队列的前面，
                    # 后面才是下一层添加的子节点
                    node.next = queue[0]  # 连接到当前层的下一个节点
                # 如果是当前层的最后一个节点 (i == size - 1)，其 next 保持为 None (初始值)

                # 8. 将当前节点的子节点加入队列 (为下一层做准备)
                # 先加左孩子，再加右孩子，保证下一层在队列中是按层序排列的
                if node.left:
                    queue.append(node.left)  # 左孩子入队

                if node.right:
                    queue.append(node.right)  # 右孩子入队

        # 9. 所有层级处理完毕，返回根节点 (树已被原地修改)
        return root

    def connect2(self, root: Node | None) -> Node | None:
        # 处理根节点为空的情况
        if root is None:
            return None

        # leftmost 指针用于标记当前处理层的最左边节点
        leftmost = root

        # 外层循环，处理除了叶子层以外的所有层
        # 如果最左边的节点有左孩子，说明下一整层都存在
        while leftmost.left:
            # current 指针用于遍历当前层的所有节点
            current = leftmost

            # 内层循环，沿着当前层的 next 指针从左到右遍历节点
            while current:
                # 1. 连接当前节点的左孩子和右孩子
                current.left.next = current.right

                # 2. 连接当前节点的右孩子到其下一个兄弟节点的左孩子
                # 如果当前节点在当前层有下一个节点 (current.next is not None)
                if current.next:
                    current.right.next = current.next.left

                # 移动到当前层的下一个节点
                current = current.next

            # 移动到下一层的最左边节点
            leftmost = leftmost.left

        # 返回原始的根节点
        return root


# Unit tests using unittest.TestCase
# 使用 unittest.TestCase 编写单元测试
class TestConnect(unittest.TestCase):

    def test_example_1(self):
        # LeetCode 示例 1: 3 层完美二叉树
        # Input: root = [1,2,3,4,5,6,7]
        # 预期连接:
        # Level 1: 1 -> NULL
        # Level 2: 2 -> 3 -> NULL
        # Level 3: 4 -> 5 -> 6 -> 7 -> NULL
        values = [1, 2, 3, 4, 5, 6, 7]
        root = list_to_perfect_node_tree(values)

        # 预期输出 (按层级的节点值列表)
        expected_output = [[1], [2, 3], [4, 5, 6, 7]]

        solution = Solution()
        connected_root = solution.connect(root)  # 原地修改

        # 将修改后的树结构转换为按层级的列表进行比较
        actual_output = perfect_node_tree_to_level_list(connected_root)

        self.assertEqual(actual_output, expected_output)
        connected_root = solution.connect1(root)  # 原地修改

        # 将修改后的树结构转换为按层级的列表进行比较
        actual_output = perfect_node_tree_to_level_list(connected_root)

        self.assertEqual(actual_output, expected_output)

        connected_root = solution.connect2(root)  # 原地修改

        # 将修改后的树结构转换为按层级的列表进行比较
        actual_output = perfect_node_tree_to_level_list(connected_root)

        self.assertEqual(actual_output, expected_output)

    def test_empty_tree(self):
        # 空树
        # Input: root = []
        values = []
        root = list_to_perfect_node_tree(values)
        expected_output = []

        solution = Solution()
        connected_root = solution.connect(root)  # 原地修改

        # 将修改后的树结构转换为按层级的列表进行比较
        actual_output = perfect_node_tree_to_level_list(connected_root)

        self.assertEqual(actual_output, expected_output)
        connected_root = solution.connect1(root)  # 原地修改

        # 将修改后的树结构转换为按层级的列表进行比较
        actual_output = perfect_node_tree_to_level_list(connected_root)

        self.assertEqual(actual_output, expected_output)

        connected_root = solution.connect2(root)  # 原地修改

        # 将修改后的树结构转换为按层级的列表进行比较
        actual_output = perfect_node_tree_to_level_list(connected_root)

        self.assertEqual(actual_output, expected_output)

    def test_two_level_tree(self):
        # 只有两层 (根 + 两个孩子) 的完美二叉树
        # Input: [1, 2, 3]
        # 预期连接:
        # Level 1: 1 -> NULL
        # Level 2: 2 -> 3 -> NULL
        values = [1, 2, 3]
        root = list_to_perfect_node_tree(values)

        expected_output = [[1], [2, 3]]

        solution = Solution()
        connected_root = solution.connect(root)  # 原地修改

        # 将修改后的树结构转换为按层级的列表进行比较
        actual_output = perfect_node_tree_to_level_list(connected_root)

        self.assertEqual(actual_output, expected_output)
        connected_root = solution.connect1(root)  # 原地修改

        # 将修改后的树结构转换为按层级的列表进行比较
        actual_output = perfect_node_tree_to_level_list(connected_root)

        self.assertEqual(actual_output, expected_output)

        connected_root = solution.connect2(root)  # 原地修改

        # 将修改后的树结构转换为按层级的列表进行比较
        actual_output = perfect_node_tree_to_level_list(connected_root)

        self.assertEqual(actual_output, expected_output)

    def test_four_level_tree(self):
        # 4 层完美二叉树
        # Input: [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        # 预期连接:
        # Level 1: 1 -> NULL
        # Level 2: 2 -> 3 -> NULL
        # Level 3: 4 -> 5 -> 6 -> 7 -> NULL
        # Level 4: 8 -> ... -> 15 -> NULL
        values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        root = list_to_perfect_node_tree(values)

        expected_output = [[1], [2, 3], [4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14, 15]]

        solution = Solution()
        connected_root = solution.connect(root)  # 原地修改

        # 将修改后的树结构转换为按层级的列表进行比较
        actual_output = perfect_node_tree_to_level_list(connected_root)

        self.assertEqual(actual_output, expected_output)
        connected_root = solution.connect1(root)  # 原地修改

        # 将修改后的树结构转换为按层级的列表进行比较
        actual_output = perfect_node_tree_to_level_list(connected_root)

        self.assertEqual(actual_output, expected_output)

        connected_root = solution.connect2(root)  # 原地修改

        # 将修改后的树结构转换为按层级的列表进行比较
        actual_output = perfect_node_tree_to_level_list(connected_root)

        self.assertEqual(actual_output, expected_output)

    # Note: According to the strict definition of a perfect binary tree with parents having two children
    # and leaves on the same level, a single node tree [1] might not fit the definition.
    # However, if problem constraints allow num_nodes >= 0, [1] could be an edge case.
    # For a single node [1], the connect function should return the root with next=None.
    # The perfect_node_tree_to_level_list would produce [[1]].
    # Let's add a test case for it for robustness, assuming it's a possible valid input.

    def test_single_node_tree(self):
        # 单个节点树 (边缘情况，可能不严格符合完美二叉树定义，但测试覆盖)
        # Input: [1]
        # 预期连接: Level 1: 1 -> NULL
        values = [1]
        root = list_to_perfect_node_tree(values)

        expected_output = [[1]]

        solution = Solution()
        connected_root = solution.connect(root)  # 原地修改

        # 将修改后的树结构转换为按层级的列表进行比较
        actual_output = perfect_node_tree_to_level_list(connected_root)

        self.assertEqual(actual_output, expected_output)
        connected_root = solution.connect1(root)  # 原地修改

        # 将修改后的树结构转换为按层级的列表进行比较
        actual_output = perfect_node_tree_to_level_list(connected_root)

        self.assertEqual(actual_output, expected_output)

        connected_root = solution.connect2(root)  # 原地修改

        # 将修改后的树结构转换为按层级的列表进行比较
        actual_output = perfect_node_tree_to_level_list(connected_root)

        self.assertEqual(actual_output, expected_output)


# This allows running the tests from the command line
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

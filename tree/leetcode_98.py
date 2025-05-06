"""
98. 验证二叉搜索树
给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。

有效 二叉搜索树定义如下：

节点的左子树只包含 小于 当前节点的数。
节点的右子树只包含 大于 当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。


示例 1：
输入：root = [2,1,3]
输出：true

示例 2：
输入：root = [5,1,4,null,null,3,6]
输出：false
解释：根节点的值是 5 ，但是右子节点的值是 4 。

提示：

树中节点数目范围在[1, 10^4] 内
-2^31 <= Node.val <= 2^31 - 1
"""
import unittest
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def list_to_tree(values: list) -> TreeNode | None:
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


def is_valid_bst(root: TreeNode) -> bool:
    """
    递归-中序遍历：利用二叉查找树性质：中序遍历为升序数组
    """
    result = []

    def inorder(node: TreeNode):
        if not node:
            return
        inorder(node.left)
        result.append(node.val)
        inorder(node.right)

    inorder(root)
    return result == sorted(result)


def is_valid_bst1(root: TreeNode) -> bool:
    """
    迭代-中序遍历：
    """
    stack = []  # 用于迭代中序遍历的栈
    current = root  # 当前节点
    prev_val = float('-inf')  # 记录上一个访问的节点的值，初始化为负无穷

    # 迭代中序遍历的标准模板
    while current is not None or stack:
        # 尽可能向左走并入栈
        while current is not None:
            stack.append(current)
            current = current.left

        # 弹出节点，访问，并检查是否大于前一个值
        current = stack.pop()

        # 检查当前节点值是否严格大于前一个值
        if current.val <= prev_val:
            return False  # 不是严格升序，无效 BST

        # 更新前一个值
        prev_val = current.val

        # 转向右子树
        current = current.right

    # 遍历完成，所有检查都通过
    return True


def is_valid_bst2(root: TreeNode) -> bool:
    # 辅助函数，带有上下边界
    def is_valid(node, min_bound, max_bound):
        # 基本情况：空节点是有效的 BST
        if node is None:
            return True

        # 检查当前节点的值是否在允许的范围内
        # 注意是严格小于/大于
        if node.val <= min_bound or node.val >= max_bound:
            return False

        # 递归检查左子树和右子树
        # 左子树的上限是当前节点的值 (node.val)
        is_left_valid = is_valid(node.left, min_bound, node.val)
        # 右子树的下限是当前节点的值 (node.val)
        is_right_valid = is_valid(node.right, node.val, max_bound)

        # 只有当左右子树都有效时，当前子树才有效
        return is_left_valid and is_right_valid

    # 从根节点开始调用辅助函数，初始边界为负无穷和正无穷
    return is_valid(root, float('-inf'), float('inf'))


def is_valid_bst3(root: TreeNode) -> bool:
    # 初始化一个类成员变量来存储上一个访问的节点的值
    # 初始化为负无穷，以确保第一个节点的值能通过检查
    prev_val = float('-inf')

    # 递归辅助函数，执行中序遍历并进行验证
    def inorder_check(node: TreeNode, _prev_val=None):
        # 基本情况：空节点是有效的
        if node is None:
            return True

        # 1. 递归检查左子树
        # 如果左子树无效，则整个树无效，直接返回 False
        if not inorder_check(node.left, _prev_val):
            return False

        # 2. 访问根节点 (在左子树检查完成后)
        # 检查当前节点的值是否严格大于上一个访问的节点的值
        if node.val <= _prev_val:
            return False  # 违反了 BST 的性质，不是有效的 BST

        # 更新上一个访问的节点的值为当前节点的值
        _prev_val = node.val

        # 3. 递归检查右子树
        # 如果右子树无效，则整个树无效，返回 False
        return inorder_check(node.right, _prev_val)

    # 从根节点开始调用验证函数
    return inorder_check(root, prev_val)


class TestIsValidBST(unittest.TestCase):

    def test_example_1(self):
        # LeetCode 示例 1: 标准有效 BST
        # Input: root = [2,1,3]
        values = [2, 1, 3]
        root = list_to_tree(values)

        self.assertTrue(is_valid_bst(root))
        self.assertTrue(is_valid_bst1(root))
        self.assertTrue(is_valid_bst2(root))
        self.assertTrue(is_valid_bst3(root))

    def test_example_2(self):
        # LeetCode 示例 2: 无效 BST (违反右子树所有节点 > 根节点)
        # Input: root = [5,1,4,null,null,3,6]
        values = [5, 1, 4, None, None, 3, 6]  # 节点 3 在 5 的右子树中，但 3 < 5
        root = list_to_tree(values)

        self.assertFalse(is_valid_bst(root))
        self.assertFalse(is_valid_bst1(root))
        self.assertFalse(is_valid_bst2(root))
        self.assertFalse(is_valid_bst3(root))

    def test_empty_tree(self):
        # 空树是有效的 BST
        # Input: root = [] (表示 None)
        values = []
        root = list_to_tree(values)

        self.assertTrue(is_valid_bst(root))
        self.assertTrue(is_valid_bst1(root))
        self.assertTrue(is_valid_bst2(root))
        self.assertTrue(is_valid_bst3(root))

    def test_single_node(self):
        # 单个节点是有效的 BST
        # Input: root = [1]
        values = [1]
        root = list_to_tree(values)

        self.assertTrue(is_valid_bst(root))
        self.assertTrue(is_valid_bst1(root))
        self.assertTrue(is_valid_bst2(root))
        self.assertTrue(is_valid_bst3(root))

    def test_tricky_out_of_range(self):
        # 复杂情况：子节点值在其直接父节点的范围内，但不在更上层祖先的范围内
        # Input: root = [5, 4, 6, null, null, 3, 7]
        values = [5, 4, 6, None, None, 3, 7]  # 节点 3 在 6 的左子树中 (3 < 6), 但 3 在 4 的右子树中 (应 > 4)
        root = list_to_tree(values)

        self.assertFalse(is_valid_bst(root))
        self.assertFalse(is_valid_bst1(root))
        self.assertFalse(is_valid_bst2(root))
        self.assertFalse(is_valid_bst3(root))

    def test_tricky_duplicate_boundary(self):
        # 包含重复值在边界上
        # Input: root = [10, 5, 15, null, null, 6, 20]
        values = [10, 5, 15, None, None, 6, 20]  # 节点 6 在 10 的右子树中 (应 > 10), 但 6 < 10
        root = list_to_tree(values)

        self.assertFalse(is_valid_bst(root))
        self.assertFalse(is_valid_bst1(root))
        self.assertFalse(is_valid_bst2(root))
        self.assertFalse(is_valid_bst3(root))

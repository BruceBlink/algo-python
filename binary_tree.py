class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_symmetric1(root) -> bool:
    """
    对称二叉树（LeetCode 101）
    给你一个二叉树的根节点 root ， 检查它是否轴对称。
    递归实现
    :param root:
    :return:
    """

    if not root:
        return False

    def is_mirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (left.val == right.val) and is_mirror(left.left, right.right) and is_mirror(left.right, right.left)

    return is_mirror(root.left, root.right)


def is_symmetric2(root) -> bool:
    """
    对称二叉树（LeetCode 101）
    给你一个二叉树的根节点 root ， 检查它是否轴对称。
    迭代实现
    :param root:
    :return:
    """

    if not root:
        return False

    queue = [root.left, root.right]
    while queue:
        left = queue.pop(0)
        right = queue.pop(0)
        if not left and not right:
            continue
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        queue.append(left.left)
        queue.append(right.right)
        queue.append(left.right)
        queue.append(right.left)

    return True


# 测试用例1：对称树
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4 3
root1 = TreeNode(1,
                 TreeNode(2, TreeNode(3), TreeNode(4)),
                 TreeNode(2, TreeNode(4), TreeNode(3)))
print(is_symmetric1(root1))  # 输出 True
print(is_symmetric2(root1))  # 输出 True

# 测试用例2：非对称树
#     1
#    / \
#   2   2
#    \   \
#     3   3
root2 = TreeNode(1,
                 TreeNode(2, None, TreeNode(3)),
                 TreeNode(2, None, TreeNode(3)))
print(is_symmetric1(root2))  # 输出 False
print(is_symmetric2(root2))  # 输出 False


def max_depth(root) -> int:
    """
    二叉树的最大深度（LeetCode 104）
    给定一个二叉树，找出其最大深度。
    最大深度是指从根节点到最远叶子节点的最长路径上的节点数。
    递归实现
    :param root:
    :return:
    """
    if not root:
        return 0
    return max(max_depth(root.left), max_depth(root.right)) + 1


def max_depth_iterative(root) -> int:
    """
    二叉树的最大深度（LeetCode 104）
    给定一个二叉树，找出其最大深度。
    最大深度是指从根节点到最远叶子节点的最长路径上的节点数。
    迭代实现
    :param root:
    :return:
    """
    if not root:
        return 0

    queue = [root]
    depth = 0

    while queue:
        depth += 1
        for _ in range(len(queue)):
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return depth


# 测试用例3：最大深度
#     1
#    / \
#   2   3
#  / \
#  4   5
# /
# 6
root3 = TreeNode(1,
                 TreeNode(2, TreeNode(4, TreeNode(6)), TreeNode(5)),
                 TreeNode(3))
print(max_depth(root3))  # 输出 4
print(max_depth_iterative(root3))  # 输出 4


def min_depth(root) -> int:
    """
    二叉树的最小深度（LeetCode 111）
    给定一个二叉树，找出其最小深度。
    最小深度是指从根节点到最近叶子节点的最短路径上的节点数。
    递归实现
    :param root:
    :return:
    """
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    if not root.left:
        return min_depth(root.right) + 1
    if not root.right:
        return min_depth(root.left) + 1
    return min(min_depth(root.left), min_depth(root.right)) + 1


def validate_BST(root: TreeNode) -> bool:
    """
    检查树是不是二叉搜索树 (leetcode.98)
    中序遍历二叉树查看结果是不是升序的
    (由二叉搜索树的性质可以推导出,二叉搜索树中序遍历的结果一定是升序数组)
    :param root:
    :return:
    """
    stack = []
    inorder = float('-inf')

    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        if root.val <= inorder:
            return False
        inorder = root.val
        root = root.right
    return True


def is_valid_bst_inorder(root):
    def inorder_traversal(node, inorder):
        if not node:
            return True, inorder
        # 递归访问左子树
        is_left_valid, inorder = inorder_traversal(node.left, inorder)
        if not is_left_valid or node.val <= inorder:
            return False, inorder
        # 更新中序遍历的上一个值
        inorder = node.val
        # 递归访问右子树
        return inorder_traversal(node.right, inorder)

    # 从根节点开始
    valid, _ = inorder_traversal(root, float('-inf'))
    return valid


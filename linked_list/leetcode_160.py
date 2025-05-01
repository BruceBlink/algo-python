"""
160. 相交链表

给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。
图示两个链表在节点 c1 开始相交：
题目数据 保证 整个链式结构中不存在环。
注意，函数返回结果后，链表必须 保持其原始结构 。

自定义评测：

评测系统 的输入如下（你设计的程序 不适用 此输入）：

intersectVal - 相交的起始节点的值。如果不存在相交节点，这一值为 0
listA - 第一个链表
listB - 第二个链表
skipA - 在 listA 中（从头节点开始）跳到交叉节点的节点数
skipB - 在 listB 中（从头节点开始）跳到交叉节点的节点数
评测系统将根据这些输入创建链式数据结构，并将两个头节点 headA 和 headB 传递给你的程序。如果程序能够正确返回相交节点，那么你的解决方案将被 视作正确答案 。

示例 1：

输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
输出：Intersected at '8'
解释：相交节点的值为 8 （注意，如果两个链表相交则不能为 0）。
从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,6,1,8,4,5]。
在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
— 请注意相交节点的值不为 1，因为在链表 A 和链表 B 之中值为 1 的节点 (A 中第二个节点和 B 中第三个节点) 是不同的节点。换句话说，它们在内存中指向两个不同的位置，而链表 A 和链表 B 中值为 8 的节点 (A 中第三个节点，B 中第四个节点) 在内存中指向相同的位置。

示例 2：



输入：intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
输出：Intersected at '2'
解释：相交节点的值为 2 （注意，如果两个链表相交则不能为 0）。
从各自的表头开始算起，链表 A 为 [1,9,1,2,4]，链表 B 为 [3,2,4]。
在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。
示例 3：


输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
输出：No intersection
解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。
由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。
这两个链表不相交，因此返回 null 。

提示：

listA 中节点数目为 m
listB 中节点数目为 n
1 <= m, n <= 3 * 104
1 <= Node.val <= 105
0 <= skipA <= m
0 <= skipB <= n
如果 listA 和 listB 没有交点，intersectVal 为 0
如果 listA 和 listB 有交点，intersectVal == listA[skipA] == listB[skipB]
"""
import unittest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # Helper method to allow comparison of ListNode objects in the heap based on value
    # This is needed for Python 3's heapq which tries to compare the second element (ListNode)
    # if the first elements (val) are equal.
    # Alternatively, one could store (val, id, node) tuple to break ties by id.
    # For this problem's constraints, comparing values within ListNode is sufficient
    # for the heap's internal sorting logic to work correctly based on the first element (val).
    # However, defining __lt__ explicitly makes it robust against Python version differences
    # or if node object comparison was the default fallback.
    # We only need to compare based on value for the heap.
    def __lt__(self, other):
        return self.val < other.val


def get_intersection_node(headA: ListNode, headB: ListNode) -> ListNode:
    # 如果任一链表为空，则不可能相交
    if not headA or not headB:
        return None

    # 初始化两个指针，分别从两个链表的头部开始
    pA = headA
    pB = headB

    # 同时遍历两个链表
    # 当一个指针到达链表末尾 (None) 时，将其重定向到另一个链表的头部
    # 如果存在相交，它们最终会在相交节点相遇
    # 如果没有相交，它们最终会在 None 处相遇 (因为它们都走了 lengthA + lengthB 步)
    while pA != pB:
        # pA = pA.next if pA else headB 的意思是：
        # 如果 pA 不是 None，pA 移动到下一个节点
        # 如果 pA 是 None (到达链表 A 末尾)，将 pA 重定向到 headB
        pA = pA.next if pA else headB

        # pB = pB.next if pB else headA 的意思是：
        # 如果 pB 不是 None，pB 移动到下一个节点
        # 如果 pB 是 None (到达链表 B 末尾)，将 pB 重定向到 headA
        pB = pB.next if pB else headA

    # 循环结束后，如果 pA 和 pB 相遇，那么它们就是相交节点 (或者都是 None，表示不相交)
    return pA


# 辅助函数，用于构建相交的链表结构，方便测试
def create_intersecting_lists(listA_vals_before_intersect: list, listB_vals_before_intersect: list,
                              intersect_vals: list):
    """
    创建一个相交的链表结构，相交点是 intersect_vals 构成的链表头部。

    参数:
        listA_vals_before_intersect: listA 在相交点之前节点的值列表。
        listB_vals_before_intersect: listB 在相交点之前节点的值列表。
        intersect_vals: 相交部分共同节点的值列表。

    返回:
        一个元组: (headA, headB, intersection_node)。
        headA: 链表 A 的头节点。
        headB: 链表 B 的头节点。
        intersection_node: 相交的起始节点 (如果 intersect_vals 为空则为 None)。
    """
    # 1. 构建相交部分的链表段
    intersection_head = None  # 相交部分的头节点
    intersection_tail = None  # 相交部分的尾节点
    if intersect_vals:
        intersection_head = ListNode(intersect_vals[0])
        intersection_tail = intersection_head
        for val in intersect_vals[1:]:
            intersection_tail.next = ListNode(val)
            intersection_tail = intersection_tail.next

    # 2. 构建 listA 的非相交部分并连接到相交点
    headA = None  # 链表 A 的头节点
    tailA = None  # 链表 A 的非相交部分的尾节点
    if listA_vals_before_intersect:
        headA = ListNode(listA_vals_before_intersect[0])
        tailA = headA
        for val in listA_vals_before_intersect[1:]:
            tailA.next = ListNode(val)
            tailA = tailA.next
        # 将 listA 非相交部分的尾部连接到相交链表段的头部
        tailA.next = intersection_head
    else:
        # 如果 listA 没有非相交部分，则 listA 的头节点就是相交链表段的头节点
        headA = intersection_head

    # 3. 构建 listB 的非相交部分并连接到相交点
    headB = None  # 链表 B 的头节点
    tailB = None  # 链表 B 的非相交部分的尾节点
    if listB_vals_before_intersect:
        headB = ListNode(listB_vals_before_intersect[0])
        tailB = headB
        for val in listB_vals_before_intersect[1:]:
            tailB.next = ListNode(val)
            tailB = tailB.next  # 修正: tailB = tailB_tail.next -> tailB = tailB.next
        # 将 listB 非相交部分的尾部连接到相交链表段的头部
        tailB.next = intersection_head
    else:
        # 如果 listB 没有非相交部分，则 listB 的头节点就是相交链表段的头节点
        headB = intersection_head

    return headA, headB, intersection_head


class TestGetIntersectionNode(unittest.TestCase):

    def test_example_1(self):
        # LeetCode 示例 1
        # Input: listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], intersectVal = 8, skipA = 2, skipB = 3
        # (即 A 的非相交部分是 [4, 1]，B 的非相交部分是 [5, 6, 1]，相交部分是 [8, 4, 5])
        headA, headB, intersection_node = create_intersecting_lists([4, 1], [5, 6, 1], [8, 4, 5])

        result = get_intersection_node(headA, headB)

        # 断言返回的节点对象是否是预期的相交节点对象（通过对象引用判断）
        self.assertEqual(result, intersection_node)
        # （可选）如果断言失败，可以检查值以增加清晰度
        if result:
            self.assertEqual(result.val, 8)

    def test_example_2(self):
        # LeetCode 示例 2
        # Input: listA = [1,9,1,2,4], listB = [3,2,4], intersectVal = 2, skipA = 3, skipB = 1
        # (即 A 的非相交部分是 [1, 9, 1]，B 的非相交部分是 [3]，相交部分是 [2, 4])
        headA, headB, intersection_node = create_intersecting_lists([1, 9, 1], [3], [2, 4])

        result = get_intersection_node(headA, headB)

        self.assertEqual(result, intersection_node)
        if result:
            self.assertEqual(result.val, 2)

    def test_no_intersection(self):
        # 没有相交的情况
        # Input: listA = [2,6,4], listB = [1,5], intersectVal = 0, skipA = 3, skipB = 2
        # (即 A 是 [2, 6, 4]，B 是 [1, 5]，相交部分为空)
        headA, headB, intersection_node = create_intersecting_lists([2, 6, 4], [1, 5], [])  # 空的 intersect_vals 表示不相交

        result = get_intersection_node(headA, headB)

        # 断言返回结果是 None （没有找到相交点）
        self.assertIsNone(result)

    def test_empty_lists(self):
        # 两个链表都为空的情况
        headA, headB, intersection_node = create_intersecting_lists([], [], [])

        result = get_intersection_node(headA, headB)

        self.assertIsNone(result)

    def test_one_empty_list_no_intersection(self):
        # 其中一个链表为空，且没有相交
        headA, headB, intersection_node = create_intersecting_lists([1], [], [])

        result = get_intersection_node(headA, headB)

        self.assertIsNone(result)

    def test_intersection_at_head(self):
        # 相交点是两个链表的头节点（实际上是同一个链表）
        headA, headB, intersection_node = create_intersecting_lists([], [], [1, 2, 3])  # 非相交部分为空
        # 此时 headA 和 headB 都会指向同一个节点对象（即值为 1 的那个节点）

        result = get_intersection_node(headA, headB)

        self.assertEqual(result, intersection_node)  # 结果应该就是值为 1 的那个节点对象
        if result:
            self.assertEqual(result.val, 1)

    def test_single_node_intersection(self):
        # 相交部分只有一个节点
        headA, headB, intersection_node = create_intersecting_lists([1], [2], [3])

        result = get_intersection_node(headA, headB)

        self.assertEqual(result, intersection_node)  # 结果应该就是值为 3 的那个节点对象
        if result:
            self.assertEqual(result.val, 3)

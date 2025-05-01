"""
23. 合并K个有序链表
给你一个链表数组，每个链表都已经按升序排列。
请你将所有链表合并到一个升序链表中，返回合并后的链表。
示例 1：
输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6

示例 2：
输入：lists = []
输出：[]

示例 3：
输入：lists = [[]]
输出：[]


提示：
k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] 按 升序 排列
lists[i].length 的总和不超过 10^4
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


def merge_k_lists(lists: list[ListNode]) -> ListNode:
    import heapq
    # Handle edge cases
    if not lists:
        return None

    min_heap = []

    # 将每个非空链表的头节点放入最小堆
    # heapq 可以直接存储 ListNode 对象，只要 ListNode 定义了 __lt__ 方法
    for head in lists:
        if head is not None:
            # heapq.heappush(min_heap, (head.val, head)) # Alternative if ListNode doesn't have __lt__ or for clarity
            heapq.heappush(min_heap, head)  # Push the node directly if ListNode has __lt__

    # 创建一个哑节点，用于构建合并后的链表
    dummy = ListNode(0)
    curr = dummy  # 当前指针，指向已合并链表的末尾

    # 当堆不为空时，不断取出最小节点并添加到合并链表
    while min_heap:
        # 从堆中取出值最小的节点
        # smallest_node = heapq.heappop(min_heap)[1] # If storing (val, node)
        smallest_node = heapq.heappop(min_heap)  # If storing node directly

        # 将取出的最小节点连接到已合并链表的末尾
        curr.next = smallest_node
        # 移动当前指针
        curr = curr.next

        # 如果取出的节点还有下一个节点，将它的下一个节点放入堆中
        if smallest_node.next is not None:
            # heapq.heappush(min_heap, (smallest_node.next.val, smallest_node.next)) # If storing (val, node)
            heapq.heappush(min_heap, smallest_node.next)  # If storing node directly

    # 合并后的链表头部是哑节点的下一个节点
    return dummy.next


# Helper function to convert a list of values to a linked list
def list_to_linked_list(values: list) -> ListNode:
    if not values:
        return None
    dummy = ListNode(0)
    curr = dummy
    for val in values:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next


# Helper function to convert a linked list to a list of values
def linked_list_to_list(head: ListNode) -> list:
    values = []
    curr = head
    while curr is not None:
        values.append(curr.val)
        curr = curr.next
    return values


# Unit tests using unittest.TestCase
class TestMergeKLists(unittest.TestCase):

    def test_example_1(self):
        # Input: lists = [[1,4,5],[1,3,4],[2,6]]
        list1 = list_to_linked_list([1, 4, 5])
        list2 = list_to_linked_list([1, 3, 4])
        list3 = list_to_linked_list([2, 6])
        input_lists = [list1, list2, list3]
        expected_output = [1, 1, 2, 3, 4, 4, 5, 6]

        merged_head = merge_k_lists(input_lists)
        actual_output = linked_list_to_list(merged_head)

        self.assertEqual(actual_output, expected_output)

    def test_empty_input(self):
        # Input: lists = []
        input_lists = []
        expected_output = []

        merged_head = merge_k_lists(input_lists)
        actual_output = linked_list_to_list(merged_head)

        self.assertEqual(actual_output, expected_output)

    def test_list_of_empty_lists(self):
        # Input: lists = [[]]
        input_lists = [list_to_linked_list([])]
        expected_output = []

        merged_head = merge_k_lists(input_lists)
        actual_output = linked_list_to_list(merged_head)

        self.assertEqual(actual_output, expected_output)

    def test_empty_and_non_empty_list(self):
        # Input: lists = [[], [1]]
        input_lists = [list_to_linked_list([]), list_to_linked_list([1])]
        expected_output = [1]

        merged_head = merge_k_lists(input_lists)
        actual_output = linked_list_to_list(merged_head)

        self.assertEqual(actual_output, expected_output)

    def test_multiple_empty_and_non_empty_lists(self):
        # Input: lists = [[2], [], [1]]
        input_lists = [list_to_linked_list([2]), list_to_linked_list([]), list_to_linked_list([1])]
        expected_output = [1, 2]

        merged_head = merge_k_lists(input_lists)
        actual_output = linked_list_to_list(merged_head)

        self.assertEqual(actual_output, expected_output)

    def test_various_values(self):
        # Input: lists = [[-1, 5, 11], [6, 10]]
        list1 = list_to_linked_list([-1, 5, 11])
        list2 = list_to_linked_list([6, 10])
        input_lists = [list1, list2]
        expected_output = [-1, 5, 6, 10, 11]

        merged_head = merge_k_lists(input_lists)
        actual_output = linked_list_to_list(merged_head)

        self.assertEqual(actual_output, expected_output)

    def test_single_list(self):
        # Input: lists = [[1, 2, 3]]
        input_lists = [list_to_linked_list([1, 2, 3])]
        expected_output = [1, 2, 3]

        merged_head = merge_k_lists(input_lists)
        actual_output = linked_list_to_list(merged_head)

        self.assertEqual(actual_output, expected_output)

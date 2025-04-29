"""
21. 合并两个有序链表
简单
相关标签
相关企业
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例 1：

输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]
示例 2：

输入：l1 = [], l2 = []
输出：[]
示例 3：

输入：l1 = [], l2 = [0]
输出：[0]

提示：
两个链表的节点数目范围是 [0, 50]
-100 <= Node.val <= 100
l1 和 l2 均按 非递减顺序 排列
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(list1: ListNode, list2: ListNode) -> ListNode:
    # 创建一个哑节点，用于简化链表头部的处理
    dummy = ListNode(0)
    # 创建一个当前指针，指向已合并链表的末尾，初始指向哑节点
    curr = dummy

    # 当两个链表都还有节点时，进行比较并合并
    while list1 is not None and list2 is not None:
        # 比较当前节点的值
        if list1.val <= list2.val:
            # 将 list1 的当前节点接到已合并链表末尾
            curr.next = list1
            # 移动 list1 指针
            list1 = list1.next
        else:
            # 将 list2 的当前节点接到已合并链表末尾
            curr.next = list2
            # 移动 list2 指针
            list2 = list2.next

        # 移动当前指针到新添加的节点
        curr = curr.next

    # 循环结束后，如果其中一个链表还有剩余节点，直接接到末尾
    if list1 is not None:
        curr.next = list1
    elif list2 is not None:
        curr.next = list2

    # 合并后的链表头部是哑节点的下一个节点
    return dummy.next





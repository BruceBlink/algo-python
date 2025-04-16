from __future__ import annotations


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next: None | ListNode = None


def reverse_list(head: ListNode) -> ListNode:
    """
    反转链表
    :param head:
    :return:
    """
    cur, prev = head, None
    while cur:
        cur.next, prev, cur = prev, cur, cur.next
    return prev


def reverse_list1(head: ListNode) -> ListNode:
    """
    反转链表
    :param head:
    :return:
    """
    cur, prev = head, None
    while cur:
        next_node = cur.next  # 保存下一个节点
        cur.next = prev       # 反转当前节点的指针
        prev = cur            # prev移动到当前节点
        cur = next_node       # cur移动到下一个节点
    return prev


if __name__ == '__main__':
    linked_list = ListNode(1)
    linked_list.next = ListNode(2)
    linked_list.next.next = ListNode(3)
    linked_list.next.next.next = ListNode(4)
    linked_list.next.next.next.next = ListNode(5)

    reverse = reverse_list(linked_list)
    print(reverse.val)

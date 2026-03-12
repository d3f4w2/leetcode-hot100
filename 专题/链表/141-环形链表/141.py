# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head) -> bool:
        if not head or not head.next:
            return False
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
    
def build_cycle_list(nums, pos):
    if not nums:
        return None

    dummy = ListNode(0)
    curr = dummy
    cycle_node = None

    for i, num in enumerate(nums):
        curr.next = ListNode(num)
        curr = curr.next
        if i == pos:
            cycle_node = curr

    if pos != -1:
        curr.next = cycle_node

    return dummy.next


def test(nums, pos, expected):
    head = build_cycle_list(nums, pos)
    result = Solution().hasCycle(head)
    print(f"nums={nums}, pos={pos}, result={result}, expected={expected}")


# 简单测试样例
test([3, 2, 0, -4], 1, True)   # 尾节点连到下标 1 -> 有环
test([1, 2], 0, True)          # 尾节点连到下标 0 -> 有环
test([1], -1, False)           # 单节点，无环
test([], -1, False)            # 空链表，无环
test([1], 0, True)             # 单节点自环
test([1, 2, 3, 4], -1, False)  # 普通无环链表
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head):
        if not head or not head.next:
            return None
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    fast = fast.next
                    slow = slow.next
                return fast
        return None

if __name__ == "__main__":
    # 创建链表：3 -> 2 -> 0 -> -4
    n1 = ListNode(3)
    n2 = ListNode(2)
    n3 = ListNode(0)
    n4 = ListNode(-4)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n2   # 这里形成环，入口是值为 2 的节点

    s = Solution()
    entry = s.detectCycle(n1)

    if entry:
        print(entry.val)   # 期望输出 2
    else:
        print(None)

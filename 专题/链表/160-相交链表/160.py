from typing import Optional


# LeetCode 平台会提供 ListNode 定义。
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(
        self,
        headA: Optional[ListNode],
        headB: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        pa = headA
        pb = headB
        while pa != pb:
            pa = pa.next if pa else headB
            pb = pb.next if pb else headA
        return pa
    
if __name__ == "__main__":
    # 公共部分：8 -> 4 -> 5
    c1 = ListNode(8)
    c2 = ListNode(4)
    c3 = ListNode(5)
    c1.next = c2
    c2.next = c3

    # A: 4 -> 1 -> 8 -> 4 -> 5
    a1 = ListNode(4)
    a2 = ListNode(1)
    a1.next = a2
    a2.next = c1

    # B: 5 -> 6 -> 1 -> 8 -> 4 -> 5
    b1 = ListNode(5)
    b2 = ListNode(6)
    b3 = ListNode(1)
    b1.next = b2
    b2.next = b3
    b3.next = c1

    s = Solution()
    ans = s.getIntersectionNode(a1, b1)

    if ans:
        print(ans.val)   # 期望输出 8
    else:
        print(None)
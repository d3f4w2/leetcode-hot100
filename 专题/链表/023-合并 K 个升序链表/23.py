# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None
        return self.merge_list(lists, 0, len(lists)-1)
    def merge_list(self, lists, left, right):
        if left > right:
            return None
        if left == right:
            return lists[left]
        mid = (left + right) // 2
        left_list = self.merge_list(lists, left, mid)
        right_list = self.merge_list(lists, mid+1, right)
        return self.merge_two(left_list, right_list)
    def merge_two(self, l1, l2):
        dummy = ListNode(0)
        cur = dummy
        while l1 and l2:
            if l1.val > l2.val:
                cur.next = l2
                l2 = l2.next
            else:
                cur.next = l1
                l1 = l1.next

            cur = cur.next

        cur.next = l1 if l1 else l2

        return dummy.next
    


def build_list(nums):
    dummy = ListNode(0)
    curr = dummy
    for num in nums:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next


def to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


if __name__ == "__main__":
    s = Solution()

    lists = [
        build_list([1, 4, 5]),
        build_list([1, 3, 4]),
        build_list([2, 6])
    ]

    ans = s.mergeKLists(lists)
    print(to_list(ans))   # 期望输出 [1, 1, 2, 3, 4, 4, 5, 6]
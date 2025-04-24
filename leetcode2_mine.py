#LeetCode 2. Add Two Numbers

#最開始解題自己的想法

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def to_list(node):
            result = []
            while node:
                result.append(node.val)
                node = node.next
            return result

        l1=to_list(l1)
        l2=to_list(l2)
        a=int("".join(map(str,l1[::-1])))
        b=int("".join(map(str,l2[::-1])))

        c=list(map(int,str(a+b)[::-1]))

        head = ListNode()
        current = head
        for i in c:
            current.next = ListNode(i)
            current = current.next
        return head.next

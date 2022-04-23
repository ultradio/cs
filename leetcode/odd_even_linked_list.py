

# https://leetcode.com/explore/interview/card/top-interview-questions-medium/107/linked-list/784/

from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self) -> None:
        self.head: ListNode = None
        self.tail: ListNode = None
    
    def push(self, value):
        new_node = ListNode(val=value)
        if self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def printList(self, head: ListNode):
        while head:
            print(head.val)
            head = head.next
        
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head_left: ListNode = None
        tail_left: ListNode = None
        head_right: ListNode = None
        tail_right: ListNode = None
        temp: ListNode = None

        count = 0
        while head:
            count += 1
            temp = ListNode(head.val)
            if count % 2 == 1:
                if tail_left:
                    tail_left.next = temp
                    tail_left = temp
                else:
                    head_left  = temp
                    tail_left  = temp
            else:
                if tail_right:
                    tail_right.next = temp
                    tail_right = temp
                else:
                    head_right  = temp
                    tail_right  = temp

            head = head.next
        
        if tail_left:
            tail_left.next = head_right        
        return head_left

head = [1,2,3,4,5]
head = [2,1,3,5,6,4,7]

ll = Solution()
for value in head:
    ll.push(value=value)

sol = Solution()
res = sol.oddEvenList(ll.head)
sol.printList(res)

        
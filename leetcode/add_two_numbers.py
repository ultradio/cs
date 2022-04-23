

from typing import List, Optional

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# https://leetcode.com/explore/interview/card/top-interview-questions-medium/107/linked-list/783/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self) -> None:
        self.head: ListNode = None
        self.tail: ListNode = None
    
    def push(self, val):
        new_node = ListNode(val=val)
        if self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.tail = new_node
            self.head = new_node

    def printList(self):
        temp = self.head
        values = []
        while temp:
            values.append(temp.val)
            temp = temp.next
        return values

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prev: ListNode = None
        temp: ListNode = None
        carry = 0

        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            sum_val = carry + v1 + v2
            carry = 1 if sum_val >= 10 else 0
            sum_val = sum_val if sum_val < 10 else sum_val % 10

            temp = ListNode(sum_val)
            if self.tail:
                prev.next = temp
            else:
                self.tail = temp
                self.head = temp
            prev = temp

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next
        
        if carry > 0:
            temp.next = ListNode(carry)
        
        return self.head

v1 = [2,4,3]
v2 = [5,6,4]
#v1 = [9,9,9,9,9,9,9]
#v2 = [9,9,9,9]

l1 = Solution()
for val in v1:
    l1.push(val=val)

l2 = Solution()
for val in v2:
    l2.push(val=val)

sol = Solution()
sol.addTwoNumbers(l1.head, l2.head)
print(sol.printList())
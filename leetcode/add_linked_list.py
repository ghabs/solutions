class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        ln = ListNode(0)
        head = ln
        while l1 is not None or l2 is not None or carry:
            if l1:
                x = l1.val
                l1 = l1.next
            else:
                x = 0
            if l2:
                y = l2.val
                l2 = l2.next
            else:
                y = 0
            summed = x + y + carry
            carry = summed // 10
            ln.next = ListNode(summed % 10)
            ln = ln.next
        
        return head.next
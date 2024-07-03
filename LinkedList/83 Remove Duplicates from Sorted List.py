# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        currentNode = head
        while currentNode != None and currentNode.next != None:
            if currentNode.val == currentNode.next.val:
                tempNode = currentNode.next
                while tempNode.next != None and tempNode.val == tempNode.next.val:
                    tempNode = tempNode.next
                currentNode.next = tempNode.next
            currentNode = currentNode.next

        return head
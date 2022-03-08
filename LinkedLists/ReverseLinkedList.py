from typing import List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def iterativeReverseLinkedList (self,head: ListNode,prev=None) -> ListNode:
        '''
        - This will run with time complexity of O(n).
        - Space complexity is constant O(1) because we only need a fixed amount of variables.
        ''' 
        current = head
        prev = None

        while current!= None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev

    def recursiveReverseLinkedList (self,head: ListNode,prev=None) -> ListNode:
        '''
        - This will run with time complexity of O(n).
        - Space complexity is O(n) as it will call the function n times.
        ''' 
        if head == None:
            return prev
        next = head.next
        head.next = prev
        return self.recursiveReverseLinkedList(next,head)

s = LinkedList()

def createList():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)
    return head

def printResult(type:str,head: ListNode):
    if head:
        result = []
        while head != None:
            result.append(head.val)
            head = head.next
        print("Reversed List ("+type+") :",result)

reversed_list = s.iterativeReverseLinkedList(createList())
printResult("Iterative",reversed_list)

reversed_list = s.recursiveReverseLinkedList(createList())
printResult("Recursive",reversed_list)
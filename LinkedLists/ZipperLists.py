from typing import List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class LinkedList:
    '''
    - Zipper list is formed by 2 linked lists given as input.
    - The idea is that the zipper list will have alternating itens from both lists.
    - Example: List1: 1 -> 2 -> 3 -> None
               List2: 32 -> 33 -> None
               Zipper List: 1 -> 32 -> 2 -> 33 -> 3 -> None
    '''
    def iterativeZipperList(self,head1:ListNode,head2:ListNode) -> ListNode:
        '''
        - Time complexity is O(min(n,m)) where m and n represent the length of the two input lists.
        - Space complexity is constant O(1). Fixed amount of variables
        '''
        tail = head1
        current1 = head1.next
        current2 = head2
        count = 0

        while current1 != None and current2 != None:
            if count == 0 or count%2 == 0:
                tail.next = current2
                tail = tail.next
                current2 = current2.next
            if count%2 != 0:
                tail.next = current1
                tail = tail.next
                current1 = current1.next
            count = count + 1

        if not current2:
            tail.next = current1
        if not current1:
            tail.next = current2
        return head1

    def recursiveZipperList(self,head1:ListNode,head2:ListNode) -> ListNode:
        '''
        - Time complexity is O(min(n,m)) where m and n represent the length of the two input lists.
        - Space complexity is O(min(n,m)) for the amount of recursive calls.
        '''
        if (head1 == None) and (head2 == None):
            return None
        if head1 == None:
            return head2
        if head2 == None:
            return head1

        next1 = head1.next
        next2 = head2.next
        head1.next = head2
        head2.next = self.recursiveZipperList(next1,next2)

        return head1

s = LinkedList()

def createLists(): 
    head1 = ListNode(1)
    head1.next = ListNode(3)
    head1.next.next = ListNode(5)
    head1.next.next.next = ListNode(7)

    head2 = ListNode(32)
    head2.next = ListNode(34)
    head2.next.next = ListNode(36)

    return head1,head2

def printResult(type:str,head: ListNode):
    if head:
        result = []
        while head != None:
            result.append(head.val)
            head = head.next
        print("Zipper List ("+type+") :",result)

head1,head2 = createLists()
zipper_list = s.iterativeZipperList(head1,head2)
printResult("Iterative",zipper_list)

head1,head2 = createLists()
zipper_list = s.recursiveZipperList(head1,head2)
printResult("Recursive",zipper_list)
from typing import List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def mergeTwoSortedLists(self,head1: ListNode,head2: ListNode) -> ListNode:
        '''
        Example: merge 1->2->4->5->None with 1->3->4->None. This gives 1->1->2->3->4->4->5->None
        - Time complexity will be O(n) where n represents the number of elements in the shortest list.
        - Since this approach creates a new list, the space complexity will be O(n+m) where n and m represent the sizes of the two input lists.
        '''
        current = ListNode(0)
        new_list = current
        while head1 != None and head2 != None:
            if head1.val <= head2.val:
                current.next = head1
                head1 = head1.next
            elif head1.val > head2.val:
                current.next = head2
                head2 = head2.next
            current = current.next
        if head1:
            current.next = head1
        if head2:
            current.next = head2
        return new_list.next

s = LinkedList()

head1 = ListNode(1)
head1.next = ListNode(3)
head1.next.next = ListNode(5)
head1.next.next.next = ListNode(7)

head2 = ListNode(2)
head2.next = ListNode(4)
head2.next.next = ListNode(6)

merged_list = s.mergeTwoSortedLists(head1,head2)
if merged_list:
    all_values = []
    while merged_list:
        all_values.append(merged_list.val)
        merged_list = merged_list.next
    print("New sorted list is:",all_values)
class LinkedListNode:
    # __init__ will be used to make a LinkedListNode type object.
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def detect_cycle(head):
    slow_pointer = head
    fast_pointer = head

    while fast_pointer and fast_pointer.next:
        # Move the slow pointer one step at a time
        slow_pointer = slow_pointer.next
        # Move the fast pointer two steps at a time
        fast_pointer = fast_pointer.next.next
        
        # If there is a cycle, the slow and fast pointers will meet
        if slow_pointer == fast_pointer:
            return True
    # If we reach the end of the linked list and haven't found a cycle, return False          
    return False

l = LinkedListNode(2)
l.next = LinkedListNode(4)
l.next.next = LinkedListNode(6)
l.next.next.next = LinkedListNode(8)
l.next.next.next.next = LinkedListNode(10)

print(detect_cycle(l))
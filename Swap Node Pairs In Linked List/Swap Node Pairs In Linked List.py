class Node:
    def __init__(self, next=None):
        self.next = next

def swap_pairs(head):
    dummy = Node()
    dummy.next = head
    current = dummy
    while current.next is not None and current.next.next is not None:
        first = current.next
        second = current.next.next
        first.next = second.next
        current.next = second
        current.next.next = first
        current = current.next.next
    return dummy.next

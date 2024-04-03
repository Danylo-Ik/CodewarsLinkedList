class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    def __repr__(self):
        return " -> ".join([str(self.data), str(self.next)])

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    if not head or not head.next:
        raise ValueError("List is too short")
    first = head
    second = head.next
    first_head = first
    second_head = second
    while first and second:
        first.next = second.next
        first = first.next
        if first:
            second.next = first.next
            second = second.next
    return Context(first_head, second_head)

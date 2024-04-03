class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    def __repr__(self):
        return " -> ".join([str(self.data), str(self.next)])

def remove_duplicates(head):
    if head is None:
        return head
    current = head
    while current.next is not None:
        if current.next.data == current.data:
            current.next = current.next.next
        else:
            current = current.next
    return head

class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def get_nth(node, index):
    counter = 0
    current = node
    while current:
        if counter == index:
            return current
        counter += 1
        current = current.next
    raise ValueError("Index is out of range")

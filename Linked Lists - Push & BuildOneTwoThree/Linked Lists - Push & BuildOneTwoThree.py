class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def push(head, data):
    temp = Node(data)
    temp.next = head
    return temp

def build_one_two_three():
    return push(push(push(None, 3), 2), 1)

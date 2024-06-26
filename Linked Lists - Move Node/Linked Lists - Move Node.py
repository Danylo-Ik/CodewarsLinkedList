class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
    
def move_node(source, dest):
    if source is None:
        raise ValueError("Source is None")
    node_moved = source
    source = source.next
    dest = push(dest, node_moved.data)
    return Context(source, dest)

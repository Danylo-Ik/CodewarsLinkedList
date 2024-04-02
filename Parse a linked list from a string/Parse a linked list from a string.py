class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    def __repr__(self):
        return f"Node({self.data}, {self.next})"

def linked_list_from_string(s):
    if s == "None":
        return None
    s = s.split(" -> ")
    ll = Node(int(s[0]), linked_list_from_string(" -> ".join(s[1:])))
    return ll

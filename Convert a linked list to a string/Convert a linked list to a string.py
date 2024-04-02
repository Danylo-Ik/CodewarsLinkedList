class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def stringify(node):
    current_el = node
    res = ""

    if current_el is None:
        return "None"

    while current_el.next is not None:
        res += str(current_el.data)
        res += " -> "
        current_el = current_el.next
    res += str(current_el.data)
    res += " -> None"
    return res

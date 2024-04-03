def loop_size(node):
    fst_ptr = node
    slw_ptr = node
    while fst_ptr and fst_ptr.next:
        fst_ptr = fst_ptr.next.next
        slw_ptr = slw_ptr.next
        if fst_ptr == slw_ptr:
            break
    ref = slw_ptr
    counter = 1
    while slw_ptr.next != ref:
        slw_ptr = slw_ptr.next
        counter += 1
    return counter

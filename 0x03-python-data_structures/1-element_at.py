#!/usr/bin/python3
def element_at(my_list, idx):
    ln = len(my_list)
    if ln < 0 or idx >= ln:
        return None
    else:
        return my_list[idx]

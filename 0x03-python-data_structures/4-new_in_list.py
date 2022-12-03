#!/usr/bin/python3


new_list = []
def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    else:
        for i in my_list:
            new_list.append(i)
        new_list[idx] = element
        return new_list

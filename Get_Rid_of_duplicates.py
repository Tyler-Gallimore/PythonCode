def unique(input_list=[]):
    new_list = []
    for i in input_list:
        if i in new_list:
            continue
        else:
            new_list.append(i)
    return new_list

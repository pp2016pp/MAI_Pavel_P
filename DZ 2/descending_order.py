def descending_order(num):
    return int("".join(sorted(str(num), reverse=True)))
    """str_num = str(num)
    list_num = []
    for i in str_num:
        list_num.append(i)
    list_num.sort(reverse=True)
    str_res = ''
    for i in list_num:
        str_res += i
    return int(str_res)"""

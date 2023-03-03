def sum_arrays(array1, array2):
    if len(array1) == 0 and len(array2) == 0:
        return []
    elif len(array1) == 0:
        first_element = 0
    else:
        first_element = int(''.join(str(element) for element in array1))
    if len(array2) == 0:
        second_element = 0
    else:
        second_element = int(''.join(str(element) for element in array2))
    result = str(first_element + second_element)
    result_list = []
    index = 0
    sign = False
    if result[0] == '-':
        sign = True
        index = 1
    for i in result[index:]:
        result_list.append(int(i))
    if sign:
        result_list[0] = result_list[0] * (-1)
    return result_list

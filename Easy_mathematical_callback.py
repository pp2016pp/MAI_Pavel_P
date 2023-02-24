def process_array(arr, callback):
    new_arr = list(map(callback, arr))
    return new_arr
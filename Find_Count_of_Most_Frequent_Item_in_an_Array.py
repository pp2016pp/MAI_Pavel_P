def most_frequent_item_count(collection):
    numbers = set(collection)
    list_counts = [collection.count(element) for element in numbers]
    if len(list_counts) !=0:
        return max(list_counts)
    return 0

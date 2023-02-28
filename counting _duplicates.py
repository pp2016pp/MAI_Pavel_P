def duplicate_count(text):
    count_repeat = 0
    text = text.lower()
    for letter in text:
        if text.count(letter) > 1:
            count_repeat += 1
            text = text.replace(letter, '')
    return count_repeat

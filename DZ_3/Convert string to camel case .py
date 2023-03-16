def to_camel_case(text):
    for i in range(len(text)):
        if text[i] == '-' or text[i] == '_':
            #text[i + 1] = text[i + 1].capitalize()
            text = text[:i+1] + text[i + 1].capitalize() + text[i + 2:]
    text = text.replace('-', '')
    text = text.replace('_', '')
    return text

# https://www.codewars.com/kata/517abf86da9663f1d2000003
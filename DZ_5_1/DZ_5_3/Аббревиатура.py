string = "world wide web"
abbr = "".join(word[0].upper() for word in string.split())
print(abbr)  # выведет "WWW"

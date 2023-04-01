text = "The quick brown fox jumps over the lazy dog"
letter_freq = {char.lower(): text.lower().count(char.lower()) for char in set(text.lower()) if char.isalpha()}
print(letter_freq)

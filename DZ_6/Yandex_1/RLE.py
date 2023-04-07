s = input()
current_digit = ''
count = 0
for digit in s:
  if digit == current_digit:
    count += 1
  else:
    if current_digit != '':
      print(current_digit, count)
    current_digit = digit
    count = 1
print(current_digit, count)

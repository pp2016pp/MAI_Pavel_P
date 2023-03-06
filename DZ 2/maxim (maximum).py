def maxim(a, *b, low=0, hi=10):
  """i am Maxim"""

  max = 0

  for number in (a, ) + b:
    if max < a:
        max = a


  if low < max < hi:
    return max
  elif max < low:
    return low

  return hi


print(maxim())
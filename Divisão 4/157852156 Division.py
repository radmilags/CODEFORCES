n = int(input())
i = 1
while i <= n:
  x = int(input())
  if x <= 1399:
    print("Division 4")
  elif x >= 1400 and x <= 1599:
    print("Division 3")
  elif x >= 1600 and x <= 1899:
    print("Division 2")
  elif x >= 1900:
    print("Division 1")
  i += 1
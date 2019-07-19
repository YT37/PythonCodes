#nums = (55, 44, 33, 22)
#print(max(min(nums[:2]), abs(-42)))
for i in range(10):
  try: 
    if 10 / i == 2.0:
      break
  except ZeroDivisionError:
    print(1)
  else:
    print(2)
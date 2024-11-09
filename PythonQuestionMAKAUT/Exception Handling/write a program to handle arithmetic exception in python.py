try:
  arithmetic = 5/0
  print(arithmetic)
except ArithmeticError:
  print('You have just made an Arithmetic error')
def AddTwo():
  x = float(input("Enter first number: "))
  y = float(input("Enter second number: "))
  total = x + y
  print(f"{x} + {y} = {total}")
  return total

AddTwo()
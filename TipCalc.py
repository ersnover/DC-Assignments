def GetNums():
  total = float(input("Enter total: "))
  percent = float(input("Enter tip percentage: "))
  percent /= 100
  return total, percent

def TipCalc(total,percent):
  tip = round(total * percent,2)
  print(f"You should tip ${tip}")
  return tip


total, percent = GetNums()
TipCalc(total,percent)
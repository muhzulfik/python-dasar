try:
  print(x)
except:
  print("Something else went wrong")

x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")
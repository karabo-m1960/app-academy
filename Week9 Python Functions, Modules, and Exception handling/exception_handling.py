
try:
  print(x)
except NameError: 
  print("Variable x is not defined")  
except:
  print("An exception occurred") 
  
  
try:
  print(x)
except:
  print("something went wrong") 
finally:
  print("The 'try except' is finished")  
  
# Else block

try:
  print("x")  
except NameError:
  print("Variable x is not defined")
else:
  print("Everything went wrong") 
  
# Raising exceptions manually

x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")   
  
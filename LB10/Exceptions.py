# Sources:
# https://www.w3schools.com/python/python_try_except.asp
# https://docs.python.org/3/tutorial/errors.html

x = 10

try:
  print(x % 0)
except NameError:
  print("Variable x is not defined")
except TypeError:
  print("Only integers are allowed")
except ZeroDivisionError:
  print("Divide en un numero diferente a cero, por algo llevaste cálculo p")
except:
  print("Something else went wrong")
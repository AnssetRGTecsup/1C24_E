# Sources:
# https://www.w3schools.com/python/python_try_except.asp
# https://docs.python.org/3/tutorial/errors.html

try:
  print(10 % 0)
except NameError:
  print("Variable x is not defined")
except TypeError:
  print("Only integers are allowed")
except ZeroDivisionError:
  print("Cannot divide by cero")
except:
  print("Something else went wrong")
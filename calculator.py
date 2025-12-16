print("Simple Calculator")

def addition(a, b):
  return a + b
def subtraction(a, b):
  return a - b
def multiplication(a,b):
  return a*b
def division(a,b):
  if b == 0:
    return "Enter a non zero Divisor"
  return a/b

def caculator():
  input1 = input("Enter First Number:")
  input2 = input("Enter Second Number:")

  num1 = float(input1)
  num2 = float(input2)
  
  selection = input("Select An Operation (+, -, *, /, ):")
  if selection == '+':
    result = addition(num1,num2)
  elif selection == '-':
    result = subtraction(num1,num2)
  elif selection == '*':
    result = multiplication(num1,num2)
  elif selection == '/':
    result = division(num1,num2)
  else:
    print("Invalid Operator")
    exit()
  print(f"Result is : {result}")
caculator()
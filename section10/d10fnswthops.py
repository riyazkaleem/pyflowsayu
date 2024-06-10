# functions
def is_leap(year):
  """ this function takes year as argument and checks
  if the year is a leap year and return True or False"""
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False
  
def days_in_month(year,  month):
  """Based on year and the month number this function
  return the number of days in month after checking
  if it is a leap year or not"""
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
  leapFlag=is_leap(year)
  if leapFlag == True:
    if month == 2:
      noOfDays = 29
      return noOfDays
    else:
      return month_days[month-1]
  else:
    return month_days[month-1]
  
#leap year and calculating no of days in a month
year = int(input()) # Enter a year
month = int(input()) # Enter a month
days = days_in_month(year, month)
print(days)

#implementing function definition inside another function
def outer_function(a, b):
    def inner_function(c, d):
        return c + d
    return inner_function(a, b)
 
result = outer_function(5, 10)
print(result)

#calculator
#functions
def addition(a, b):
  """performs addition of two numbers"""
  return a+b

def subtraction(a, b):
  """performs addition of two numbers"""
  return a-b

def multiplication(a, b):
  """performs addition of two numbers"""
  return a*b

def division(a, b):
  """performs addition of two numbers"""
  return a/b

#implementation
calci = {
  '+': addition,
  '-': subtraction,
  '*': multiplication,
  '/': division
}

n1 = int(input('enter first number: '))
for operator in calci:
  print (operator)

continueFlag = True
while continueFlag:
    symbol = input('enter the operation u wanna do: ')
    n2 = int(input('enter next number: '))
    operation = calci[symbol]
    result = operation(n1, n2)
    print(f'calculating {n1} {symbol} {n2}: {result}')

    if input('do you wanna continue') == 'y':
      n1=result
    else:
      continueFlag = False







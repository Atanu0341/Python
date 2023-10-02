def calculateGmean(a, b):
  mean = (a * b) / (a + b)
  print(mean)


def isGreater(a, b):
  if (a > b):
    print("First number is greeater")
  else:
    print("Second number is greater or equal")


a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

isGreater(a, b)
calculateGmean(a, b)

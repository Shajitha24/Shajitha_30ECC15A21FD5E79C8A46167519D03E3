# 1.1 Implement a recursive function to calculate the factorial of a given number.

def factp(n):
  if n==0 or n==1:
    return 1
  else:
    return n*factp(n-1)

num=int(input("Enter the value:"))
result=factp(num)
print("The {}! value is {}".format(num, result))
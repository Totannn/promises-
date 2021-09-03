#this is for a calculator

print("lets get started")
print ("please select a mathematical operation")
print("1 for addition")
print("2 for subtraction")
print("3 for multiplication")
print("4 for Division")
print ("5 for exponent ")
print ("6 for logarithm")

operation= input()
if operation == "1":
       num1 = input("enter the first number")
       num2 = input("enter the second number")
       print("your answer is")
       print (str(int(num1)+int(num2)))

elif operation == "2":
       num1 = input("enter the first number")
       num2 = input("enter the second number")
       print("your answer is")
       print (str(int(num1)-int(num2)))
elif operation == "3":
       num1 = input("enter the first number")
       num2 = input("enter the second number")
       print("your answer is")
       print (str(int(num1)*int(num2)))
elif operation == "4":
       num1 = input("enter the first number")
       num2 = input("enter the second number")
       print("your answer is")
       print (str(int(num1)/int(num2)))
elif operation == "5":
       num1 = input("enter the first number")
       num2 = input("enter the second number")
       print("your answer is")
       print (str(int(num1)**int(num2)))
elif operation == "6":
       import math
       num1 = input("enter the first number")

       print("your answer is")
       print (math.log((int(num1))))
       

else:
    print("soltion does not exist")
    

  
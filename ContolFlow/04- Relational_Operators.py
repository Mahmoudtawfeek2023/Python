x = 20
y = 20
if x == y:
  print("These numbers are the same")


credits = int(input("My total credits degree is: "))
if credits >= 120:
  print("You have enough credits to graduate!")
else:
  print("You don\'t have enough credit")

Age = int(input("My age is: "))
if Age < 18:
    print("You aren't permitted to get an ID")
elif Age == 18:
    print("You need birth of certification to get an ID")
elif Age > 18 and Age < 21:
    print("Here is your ID, you still under your parents control")
else:
    print("You are an adult, Here is your ID")

Number = int(input("The number is: "))
if not Number % 2 == 0:
    print("It is an odd number")
else:
    print("The number is Zero or Even")    
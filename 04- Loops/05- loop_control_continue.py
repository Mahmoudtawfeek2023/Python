big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]

#o print out all of the numbers in a list, but only if they are positive integers.
for i in big_number_list:
  if i <= 0:
    continue
  print(i)
  
ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]
for age in ages:
  if age <= 20:
    continue
  else:
    print("You are allowed to enter the bar because you have",age,"years old.")
message1 = "I am Mahmoud Tawfeek"
message2 = 'I am a software developer for networking automation'
message = message1 + ' ' + message2
print(message)

#Accessing the Characters of a String
var_1 = message[0]
var_2 = message[21:]
var_3 = message[1:4]
var_4 = message[:15]
# var_5 = message[200] ==> Error as value isn't exist
print("var_1: " + var_1)
print("var_2: " + var_2)
print("var_3: " + var_3)
print("var_4: " + var_4)

# Multi-line Strings
my_string = """If it were done when 'tis done, then 'twere well
It were done quickly: if the assassination
Could trammel up the consequence, and catch
With his surcease success; that but this blow
Might be the be-all and the end-all here,
But here, upon this bank and shoal of time,
We'ld jump the life to come."""
print(my_string)

# Escape Characters
my_string_1 = 'It\'s a lovely day!'
print(my_string_1)

# Arranging lines
note = "I am on top!\nI am on bottom. \n\tI am indented!"
print(note)

# Modifying Strings
string_one = "Hello, "
string_two = "World! "
combo = string_one + string_two
print(combo)
new_combo = combo * 2
print(new_combo)
if "World" in new_combo:
  print("It's here!")
  
# Built-in String Methods:
    # .capitalize(): Make first letter capital only.
print("WELCOME TO CODECADEMY DOCS!".capitalize())
text = "welcome to codecademy's docs!"
print(text.capitalize())
text2 = "welcome To Codecademy's Docs!"
x = text2.capitalize()
print(x)

    # .casefold(): returns a copy of a string with all characters in lowercase. 
        # It is similar to .lower(), but whereas that method deals purely with ASCII text, .casefold() can also convert Unicode characters.
my_string_1 = "THIS SHOULD ALL BE IN LOWERCASE!"
print(my_string_1.casefold()) 
my_string_2 = "this Should ALSO Be Entirely In Lowercase!"
print(my_string_2.casefold())
my_string_3 = "Straße"
print(my_string_3.casefold())  

    # .count(): Takes in a list of values of any data type, and returns the number of times(count) a particular value is present within the list.
pets = ['fish', 'dog', 'dog', 'turtle', 'cat', 'cat', 'cat']
print(pets.count('cat'))
treats_per_pet = [1, 3, 3, 1.5, 2, 2, 2]
x1 = treats_per_pet.count(3)
print(x1)

    # .endswith(): The .endswith() method checks a value against a given string and returns True if the string ends with that value. Otherwise, it returns False.
example_str = "This is a string 123"
check_A = example_str.endswith("g")
check_B = example_str.endswith("s")
check_C = example_str.endswith("st", 4, 12)
print("A: ", check_A)
print("B: ", check_B)
print("C: ", check_C)

    # .find() : The .find() string method takes in a substring (and optionally start/end index), returns the index number of the first occurrence of the substring inside a string. 
    # It is case sensitive. If the substring is not found, returns -1.
new_string = "I like to eat potato"
like_result = new_string.find("like")
drink_result = new_string.find("drink")
to_result = new_string.find("to")
print(like_result)  
print(drink_result) 
print(to_result)    

new_string2 = "I like to eat potato"
like_2_length_result = new_string2.find("like", 2, len(new_string))
like_4_length_result = new_string2.find("like", 4, len(new_string))
like_0_3_result = new_string2.find("like", 0, 3)
like_0_15_result = new_string2.find("like", 0, 15)
like_0_last3_result = new_string2.find("like", 0, -3)
print(like_2_length_result)
print(like_4_length_result)
print(like_0_3_result)
print(like_0_15_result)
print(like_0_last3_result)
print("")
to_0_length_result = new_string2.find("to", 0, len(new_string))
to_15_length_result = new_string2.find("to", 15, len(new_string))
print(to_0_length_result)
print(to_15_length_result)

    # .format(): The .format() string function returns a string with values inserted via placeholders.
    # Python’s built-in string function .format() converts strings by inserting values passed through placeholders.                    
    # {} is a placeholder. All the arguments specified in the format method will be replacing the placeholders in the string.
phrase = "I like to eat {}s and {}s."
formatted_phrase = phrase.format("apple", "orange")
print(formatted_phrase)

string_1 = "I like to eat {food1} and {0}"
new_string_1 = string_1.format("orange", food1="apple")
string_2 = "I like to eat {0} and {food1}"
new_string_2 = string_2.format("orange", food1="apple")
print(new_string_1)
print(new_string_2)

    # .index(): The .index() string method searches through a string variable for the occurrence of a pattern or a substring. If the substring is not found, a ValueError will be raised.
my_new_string = 'Learning to code is fun!'
my_new_index = my_new_string.index('code', 8, 16)
print(my_new_index)    

    # .islower(): The .islower() string method takes in a string and returns True if all the letters in the string are in lowercase, else returns False. 
    # This method ignores spaces, newlines, numeric, and special characters in the string.
my_slower_string = "Learn--to--code--from--Codecademy!\n"
print(my_slower_string.islower())

    # .isupper(): The .isupper() string method takes in a string and returns True if all the letters in the string are in uppercase, else returns False. 
    # This method ignores spaces, newlines, numeric, and special characters in the string.
my_upper_string = "--PYTHON3--"
print(my_upper_string.isupper())

    # .join(): The .join() method concatenates all items from an iterable into a single string.
fruits = ["Apples", "Bananas", "Blueberries"]
combined = " ".join(fruits)
print(combined)
vehicles = ("bicycle", "car", "moped", "truck")
joined = "-".join(vehicles)
print(joined)

    # .lower(): Takes a string, and returns a copy of that string in which all letters are lowercase. Numbers and symbols are not changed
string_lower_1 = "Red Pandas"
string_lower_2 = "rEd pAnDaS"
if string_lower_1 == string_lower_2:
  print("These strings are already the same")
elif string_lower_1.lower() == string_lower_2.lower():
  print("They are the same when you use the .lower() method")
else:
  print("They are NOT the same")
  
    # .partition(): Searches a string for a given keyword and splits that string into a three part tuple.
my_tuple_string = "Do not go gentle into that good night"
my_tuple = my_tuple_string.partition("gentle")
print(my_tuple)

    # .replace(): Replace a specific substring with another substring.
welcome = "Hello, world!"
welcome = welcome.replace("world", "Codecademy")
print(welcome)

    # .split(): The .split() method returns a new list of substrings based on a given string.
my_list_string = "I like waffles from Belgium"
my_list = my_list_string.split()
print(my_list)

multiline_string = """
Beets
Bears
Battlestar Galactica
"""
menu = "Breakfast|Eggs|Tomatoes|Beans|Waffles"
list_a = multiline_string.split("\n")
list_b = menu.split("|", 3)
print(f"Using escape characters: {list_a}")
print(f"Limited number of list items: {list_b}")

example_string = "Bears, beans, and breakfast."
regex_string = r"ea"
print(example_string.split(regex_string))

    # .startswith(): The .startswith() method checks a value against a given string and returns True if the string starts with that value. Otherwise, it returns False.
example_A = "This is a string 1232312"
check_A = example_A.startswith("This")
print(check_A)

example_B = "This is a string"
check_B = example_B.startswith("t")
print(check_B)

example_C = "This is a string"
check_C = example_C.startswith("st", 10, 14)
print(check_C)

    # .swapcase(): Takes a string and returns a copy of that string in which all lowercase letters are uppercase, and all upercase letters are lowercase. 
    # Numbers and symbols are not changed
my_swapcase_string = "camelCasingIsFun"
my_swapcase_string.swapcase()
print(my_swapcase_string)
print(my_swapcase_string.swapcase())

    # .title(): The .title() string method takes in a string and returns a copy of the string formatted in the title case: each word in the string is capitalized.
my_title_string = "Soon everyone will have a 5g connection!"
print(my_title_string.title())

    # .upper(): The .upper() method takes a string and returns a copy of that string in which all letters are uppercase. Numbers and symbols are not changed.
string_upper_1 = "Green Tigers"
string_upper_2 = "gReEn tIgErs"
if string_upper_1 == string_upper_2:
  print("These strings are already the same")
elif string_upper_1.upper() == string_upper_2.upper():
  print("They are the same when you use the .upper() method")
else:
  print("They are NOT the same")
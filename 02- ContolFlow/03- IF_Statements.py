# Enter a user name here, make sure to make it a string
while True:
    user_name = input("My Username is: ")
    denied_user_name = "dave"
    fake_user_name = "angela_catlady_87"
    if user_name == denied_user_name.capitalize():
        print("Get off my computer Dave!")
    elif user_name == fake_user_name.lower():
        print("I know it is you, Dave! Go away!")
    else:
         print("Welcome new colleague")
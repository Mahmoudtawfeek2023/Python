# type(): to return the type of value
message = "Hello, world!"
case = 1
movie = 409.123
print(type(message),type(case),type(movie))

# isinstance(): ask about the type of data
word = "purple"
languages = ("Python", "JavaScript", "Go")
print(isinstance(word, str))
print(isinstance(languages, list))
print(isinstance(languages, tuple))
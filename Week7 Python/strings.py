#Strings concatenations

greeting = 'Hello, '+ 'World!'

print(greeting)

repeated_string = 'Hello ' * 3

print(repeated_string)

message = 'Bob\'s world'
print(message)

message = """Bob's world
is a great place to be."""
print(message)

#advanced string formatting

message = ' Hello world!'

print(message.strip()) # Remove leading and trailing whitespace

message = 'Hello'

print(message[0])
print(message[1])
print(message[-1])
print(len(message))

message = 'Hello, world!'

print(message.split('.')) # Split the string into a list based on the comma

fruit_list = ['apple', 'banana', 'cherry']
joined_string = ','.join(fruit_list)
print(joined_string)  

original_string = 'Hello, world!'
substring = original_string[0:5] #Extract Hello
print(substring)  
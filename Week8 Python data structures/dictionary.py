# Dictionaries 

my_dict = {"name": "John", "age": 30}

print(my_dict["name"])  # Accessing the value associated with the key "name"

my_dict["age"] = 35# Changing the value associated with the key "age"
print(my_dict)

my_dict["Gender"] = "Male"  # Adding a new key-value pair
print(my_dict)

my_dict.pop("age")  # Removing the key "age" and its associated value
print(my_dict)

print("name" in my_dict)  # Checking if the key "name" exists in the dictionary
print("age" in my_dict)  # Checking if the key "age" exists in the dictionary 

Fruits = ["apple", "banana", "cherry"]

print(Fruits[0])  # Accessing the first element

print(Fruits[1])  # Accessing the second element

#Changing the second element

Fruits[1] = "blueberry"
print(Fruits)

#Adding an element to the list

Fruits = ["apple", "banana", "cherry"]

Fruits.append("kiwi") #Adding kiwi to the end of the list
print(Fruits)

Fruits.extend(["kiwi", "mango", "papaya"]) #Adding multiple elements to the end of the list
print(Fruits)

Fruits = ["apple", "banana", "cherry"]

Fruits.insert(1, "orange") # Inserting orange at index 1
print(Fruits)


#Removing elements from the list

Fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

Fruits.remove("banana")  # Removing banana from the list
print(Fruits)

popped_fruit = Fruits.pop()  # Removing the last element (mango) and storing it in popped_fruit
print(popped_fruit) 
print(Fruits) 

Fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
Fruits.pop(1)  # Removing the element at index 1 (banana)
print(Fruits)

Fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

del Fruits[1]  # Deleting the element at index 1 (banana)
print(Fruits)

Fruits.clear()  # Clearing the entire list
print(Fruits)  # Should print an empty list

#Sorting the list

Fruits = ["banana", "apple", "cherry", "kiwi", "mango"]

Fruits.sort()  # Sorting the list in ascending order
print(Fruits)

Fruits.sort(reverse=True)  # Sorting the list in descending order
print(Fruits)

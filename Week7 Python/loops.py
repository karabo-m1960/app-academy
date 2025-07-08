#For Loops

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
  print(fruit)
  

numbers = [1, 2, 3, 4, 5]
for number in numbers:
  print(number)
  

#While Loops to count from 1 to 5

count = 1
while count <= 5:
    print(count)
    count += 1 #increment the count by 1
    

# For Loop control statements

fruits = ["apple", "banana", "cherry", "date"]

for fruit in fruits:
    if fruit == "cherry":
        break  # Exit the loop when "Cherry" is found
    print(fruit)
    
for fruit in fruits:
    if fruit == "cherry":
        continue  # Skip the iteration when "Cherry" is found
    print(fruit)
    
for fruit in fruits:
    if fruit == "cherry":
        pass  # Do nothing when "Cherry" is found
    print(fruit)
    

#While Loop control statements

count = 0

while count < 5:
    print(count)
    count += 1
    if count == 3:
        break  # Exit the loop when count is 3
      
while count < 5:
    print(count)
    count += 1
    if count == 3:
        continue # Skip the iteration when count is 3
      
while count < 5:
    print(count)
    count += 1
    if count == 3:
        pass  # Do nothing when count is 3
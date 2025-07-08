# Tuples

my_tuple = (1, 2, 3, 4, 5)

print(my_tuple)
print(my_tuple[0])  # Accessing the first element
print(my_tuple[2])  # Accessing the second element
print(my_tuple[-1])  # Accessing the fifth element

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

conc_tuple = tuple1 + tuple2 # Concatenating tuple1 and tuple2
rep_tuple = tuple1 * 3  # Repeating tuple1 three times

print(conc_tuple)  
print(rep_tuple)  
print(my_tuple[1:3])  # Slicing the tuple from index 1 to 2 (exclusive of 3)

my_tuple = (1, 2, 3)
a, b, c = my_tuple  # Unpacking the tuple into variables a, b, c
print(a, b, c)  
print(a)
print(b)
print(c)
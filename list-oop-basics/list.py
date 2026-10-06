students = ["Kai Samba", "Foday", "Sharon"]
print(students)

print(f"My best friend is {students[0]}")
print(f"My best friend is {students[1]}")
print(f"My best friend is {students[2]}")

# Get the index of an item in a list
print (students.index ("Kai Samba"))
print (students.index ("Sharon"))

# know the number of items in a list
print(f" The total items in the list is: {len(students)}")

# Add items to a list
students.append("Isatu")
print(students)
students += ["Kadiatu", "John", "Bintu"]

print(students)
students.insert(4, "Donald")
print (students)

# Extending a list
fruits = ["Apple", "Banana", "Mango"]
students.extend(fruits)
print(students)

# Removing an item in a list
fruits.remove("Mango")

students.pop()
students.pop()
thirdItem = students.pop()
print(students)
print(thirdItem)
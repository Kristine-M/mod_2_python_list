# task 1.1
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort()
print(grades , "\n")
grades.reverse() #descending order
print(grades)

# task 1.2
sum = 0
for num in grades:
    sum += num
avg = sum / len(grades)
print(avg)

# task 1.3

for i in range(len(grades)):
    if grades[i] < 80:
        grades[i] = "Failed"
        
print(grades)

# task 2.1
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

for i in range(len(submitted)):
    if submitted[i] in attended:
        print(submitted[i], "\n") #prints the names who submitted and attended
        
# task 2.2

for i in range(len(submitted)):
    if submitted[i] not in attended:
        print("not identical")

# task 2.3

attended.remove("Eve")
attended.remove("Frank")
        
print(attended)

# task 3.1

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 
89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

second_week = temperatures[7:14]

print(second_week)


# task 3.2

above_100 = []

for num in temperatures:
    if num > 100:
        above_100.append(num)
        
print(above_100)


#task 3.3
temperatures.reverse()
print(temperatures)
fifth_to_tenth = temperatures[4:10]
print(fifth_to_tenth)

# task 4.1
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even = [num for num in numbers if num % 2 == 0] #single in line

for num in numbers: # or by looping
    if num % 2 == 0:
        even.append(num)
        
print(even)

# task 4.2

greater_5  = [num for num in numbers if num > 5]
print(greater_5)

# task 4.3

print(7 in numbers)


# task 5.1
students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

add_element = [] #we have not yet covered dictionaries or pairs so I put it into 
new_list = [] #individual list

for i in range(len(students)):
    add_element.append(students[i])
    add_element.append(grades[i])
    add_element.append(activities[i])
    new_list.append(add_element)
    add_element = []
    
print(new_list)

# task 5.2

new_list.remove(['Jane', 78, 'Art'])

print(new_list)

# task 5.3- Did not know what or how to add key-value pair so I appended to the lists

for i in range(len(new_list)):
    curr_list = new_list[i]
    curr_list.append("status: Passed")
    
print(new_list)
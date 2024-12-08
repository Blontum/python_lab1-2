# List of student numbers
students = [1, 2, 3, 4, 5]

# Open the file in write mode ('w' )
with open('studentsnum.txt', 'w') as file:
    for number in students:
        file.write(f"{number}\n")

# Open the file in read mode and print the contents
with open('studentsnum.txt', 'r') as file:
    content = file.read()
    print(content)
''''''''''
bo = open ('bo.txt', 'w')# open file . Write manupulate every information (creation)

bo.write('tomat') # write to the file
bo.write('bama')

bo.close() # close the file

bo = open ('bo.txt', 'r') # read the file. Read is without changing any information
bo = open ('bo.tex', 'a') # append the file. append add information to the existing data   

# example

cars = open (' bo-cars.txt', 'w') 
cars.write("porch 911\n")  
cars.write("class honda\n")
cars.write("honda crv \n")
cars.write("tesla model y \n")
cars.write("ford f-150\n")         


with open ('bo.txt', 'w') as cars:
    cars.write('fordcars\n')
    cars.write('toyot\n')      

cars = open (' bo-cars.txt', 'r') 

line_1 = cars.readline() 
line_2 = cars.readline()

print(f" 1st line: {line_1}")
print(f" 2nd line: {line_2}")
cars.close()       '''''''''


def read_file() :
    grocery_list = open ('grocery.txt', 'r')
    
    dollar_menu = [ "bread,", "beans"]
    for line in grocery_list:
        dollar_menu.append(line)

        print(dollar_menu)
        grocery_list.close
     

 # Ask to operator
def print_name(name):
 print("Hello" + " " + name)
 print_name(input("Please input your name : "))

 # Number of entries
 number_of_entries = input("How many entries do you want to make : ")
 # Ask to operator
 fname = input("Please enter your file name with adding(.txt) : ")

 # Creating a file
 file = open(fname , "w")

 for i in range(0, int(number_of_entries)) :
     Task = input("Task : ")
     entry = "(Task) \n"
     if i == int(number_of_entries) -1 :
         print("Done!")
     else :
         print("Okay, next one: ")
         file.close()
         x = open(fname , "r")
         count = 0
         for line in x:
             count += 1
             print(count)




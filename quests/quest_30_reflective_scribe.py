#!/usr/bin/python3      
#this a shebang that tackles comments
#this file tackles different tasks with comments 


# --- this is the quest_20_even_number_forager.py ---

#!/usr/bin/python3        #this is a shebang to be able to run the script
for i in range(1, 21):    #this a "for" loop to be able that displays integers from 1 to 20 using the variable "1"
    if i % 2 == 0:        # this set a condition for all even numbers 
	    print(i)          #this prints all even numbers


## --- this is the quest_16_marching_ants

#!/usr/bin/python3                          #this a shebang to be able to run the script

length = float(input("Enter length: "))     #this asks the user to input a length and it stores it in the variable "length"
width = float(input("Enter width: "))       #this asks the user to input width nbumer and it stores it in the variable "width"

area = length * width                       # this calculate the area using the "*" operator between the variables "length" and "width"

print("Area of rectangle is:", area)        #this prints the result of the variable "area" with a message 


## --- this is the quest_29_code_breaker

#!/usr/bin/python3                           #this is a shebang to be able to run the script
attempt = 0                                  #this is an initialization of a variable "attempt" that will help in the repetition of our program
print("you have three attempts for this code")      #this is a message that warns the user that he only has three attempts for the code

while attempt < 3:                            # this a loop "while" that helps us in the repetition of our program with a condition of only execute for the values of the variable "attempt" that is less than 3
    attempt += 1                              # this is a counter that will count how many time the programs has executed
    secret_code = (input("enter the secret_code:"))     # this asks a user to input a code and it stores it in a variable "secret_code'
    if secret_code == "`42`":                 #this is a condition for all values of "secret_code" that are not `42`
        print("unlocked")                     # this prints a message if the condition is true
        break                                 #this breaks or stops the program if the condition up is met 
    else:                                     # this is will repeat itself whenever the condition is not met because of the loop
#this will repeat itself for three time whenever the conditionset is not met

        print("wrong code. abeg repeat:")
else:
    print("you have exceeded the number of attempts")      #this will be displayed in case the attempsts are finished. 

#This is the title and blank space
print("Hours to Days Converter ")

print(" ")

#This is the where the user inputs the numbers of hours
hours = int(input("Insert the number of hours here: "))

#This is where the code does the math and convers the hours
d_to_h = (hours//24)
remainder = (hours % 24)

print (" ")

#Here is the out come of the calculation
print ("There is " +str(d_to_h)+ " day(s) and a remainder of "+str(remainder) + " hour(s) in " +str(hours) + " hours.")
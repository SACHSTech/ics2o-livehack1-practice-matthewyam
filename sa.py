#This is the title and blank space
print("Days to Minutes Converter ")

print(" ")

#This is the where the user inputs the numbers of minutes
minutes = int(input("Insert the number of minutes here: "))

#This is where the code does the math and convers the minutes
m_to_d = (minutes//60//24)
remainder_m = (minutes % 60 % 24)

print (" ")

#Here is the out come of the calculation
print ("There is " +str(m_to_d)+ " day(s) and a remainder of "+str(remainder_m) + " minutes(s) in " +str(m_to_d) + " minutes.")
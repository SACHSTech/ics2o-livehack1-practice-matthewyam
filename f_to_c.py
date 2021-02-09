#This is the title and the blank space to make it easier to read
print("Fahrenheit to Celsius Converter")
print(" ")

#This line indicates the user to enter the temperature in fahrenheit
ftemp=int(input("Enter the temperature in fahrenheit here: "))

#This is the math equasion to convert fahrenheit to celsius
f_to_c = (9/5*(ftemp-32))

#This is the line that will print hte calculation
print ("This is the temperature in celsius: "+str(f_to_c) +str("°C"))
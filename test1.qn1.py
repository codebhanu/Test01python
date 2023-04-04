
# Taking input for date
Day=int(input("Enter the day in numeric form: "))
Month=int(input("Enter the month in the numeric form: "))
Year=int(input("Enter the year as two numerical digits (for example: 98, 20, 21): "))

#Checking if date entered is valid or not
if Day<1 or Day>31:
    print("Error: Invalid Day Input")
elif Month<1 or Month>12:
    print("Error: Invalid Month Input")  

elif Year<10 or Year>99:
    print("Error: Invalid Year Input") 
else:
    print("Success: Congratulations! you entered the correct date.") 
    print(" The date is:  {}/{}/{}".format(Month, Day, Year))
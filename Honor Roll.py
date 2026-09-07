# Johnathon Ramer
# Honor Roll.py
# My application will continuously ask for a students last name, first name, and GPA.
# If the student's GPA was over the specified amount it will print out the message stating
# That that student achieved being on the specified honors list. This will continiously ask
# and report until the user puts "ZZZ" as the student's last name signaling the program to quit.


while True:

    last_Name = input("Please Enter Student's Last Name: ")

    if(last_Name == "ZZZ"):
        break

    first_Name = input("Please Enter Student's First Name: ")

    gpa = float(input("Please Enter the Student's GPA: "))

    if(gpa >= 3.5):
        print(f"{first_Name} {last_Name} has made the Dean's List with a GPA of {gpa}")
    if(gpa >= 3.25):
        print(f"{first_Name} {last_Name} has made the Honor Roll with a GPA of {gpa}")
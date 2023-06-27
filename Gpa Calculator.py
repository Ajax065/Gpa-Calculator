print ("Hello Please Fill in the right values")
Student_Name = input("What is your name: ")
Matric_No = input("What is you matric number: ").upper()
Total_Load_Unit = int(input("What is your total load unit: "))
Courses_Offered = int(input("How many courses did you do: "))
Obtainable_Grade = []
for x in range(Courses_Offered):
    Course_name = input("Course title: ")
    Unit = int(input("Course unit: "))
    score = int(input("What was score: "))
    if (score >= 70):
        grade = 5
    elif (score >= 60):
        grade = 4
    elif (score >= 50):
        grade = 3
    elif (score >= 45):
        grade = 2
    else:
        grade = 0
        
    Grade = Unit*grade
    Obtainable_Grade.append(Grade)

Total_Credit_Point = sum(Obtainable_Grade)
GPA = Total_Credit_Point/Total_Load_Unit
print("Your GPA is" + GPA)
      
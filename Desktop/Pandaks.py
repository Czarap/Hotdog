
import pandas as pd
Username =  input("Enter username: ")
Password =  input( "Enter password: ")
if Username == "ComputerScience" and Password == "PSU88@" :
 student_record  = []
 def add_student_record():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    course = input("Enter student course: ")
    year_level = (input("Enter student year level: "))
    student_records = {
        "Name": name,
        "Age": age,
        "Course": course,
        "Year Level": year_level
    }
    student_record.append(student_records)
    print("Student record added successfully")
 def search_student_record():
    student_name = input("Enter a student name: ")
    for record in student_record:
        if record["Name"] == student_name :
            print("Name", record["Name"])
            print("Age", record["Age"])
            print("Course", record["Course"])
            print("Year Level", record["Year Level"])
        else:
          print("Student not found")
 def update_course():
     name = input("Enter a student name: ")
     for record in student_record:
         if record["Name"] == name:
          new_course = input("Enter a course: ")
          record["Course"] = new_course
          print("Student Course updated succesfully")
 def filter_students() :
     n_course = lambda x : [student for student in student_record if student["Course"] == x]
     course = input("Enter a course")
     students = n_course(course)
     for student in students:
        print("Name", student["Name"])
        print("Age", student["Age"])
        print("Course", student["Course"])
        print("Year Level", student["Year Level"])
 def number_of_students(records):
      if len(records) == 0:
        return 0
      return 1 + number_of_students(records[1:])
 def student_display_records():
    data = pd.DataFrame(student_record)
    data.index = range(1,len(data)+1)
    print(data)
 
 while True:
    print("\nStudent System Record")
    print("1. Add Student Record")
    print("2. Search Student Record")
    print("3. Update Course Information")
    print("4. Filter Students by Course")
    print("5. Calculate Total Number of Students")
    print("6. Display Student Records")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")
    
    if choice == "1" :
       add_student_record()  
    elif choice == "2" :
      search_student_record()
    elif choice == "3":
      update_course()
    elif choice == "4":
     filter_students()
    elif choice == "5" :
     total_students = number_of_students(student_record)
     print("Total number of student: ",total_students)
    elif choice == "6":
        student_display_records()
    elif choice == "7" :
     break
    else:
        print("Invalid choice. Please enter a number from 1-7")
else:
 print("Invalid username or password")    
from counselor import *


stu={}

def student_derails():
    student=int(input("Enter Serial Number : "))
    if student in all_record.keys():
        print("First Name--------------")
        print(all_record[student]["First_Name"])
        print("Last Name--------------")
        print(all_record[student]["Last_Name"])
        print("Contact Number--------------")
        print(all_record[student]["Countect_Number"])
        print("Subject--------------")
        print(all_record[student]["Subject"])
        print("Marks--------------")
        print(all_record[student]["Marks"])
        print("Fees--------------")
        print(all_record[student]["Fees"])
    else:
        print("Not A Student Serial Number")


def student_parents():
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name : ")
    Contect_number = int(input("Enter Contect Number : "))
    salary = int(input("Enter salary : "))
    global stu
    stu.update( {'fname': first_name, 'lname': last_name,'Contact': Contect_number, "salary": salary,})
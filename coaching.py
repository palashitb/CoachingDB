import subprocess as sp
import pymysql
import pymysql.cursors
from datetime import date

# def calculate_age(born):
#     today = date.today()
#     return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
def option1():
    
    print("Select something to add")
    print("1. Student")
    print("2. New Branch")
    print("3. Staff(employee)")
    print("4. Online Lecture details")
    print("5. New Course")
    print("6. Student family details")
    print("7. Study material given to a particular student")
    print("8. New study material")

    ad = int(input("\nEnter Choice>  "))
    tmp = sp.call('clear', shell = True)
    if( ad == 1 ):
        studentAdmission();
    if( ad == 2 ):
        addBranch();
    if( ad == 3 ):
        addStaff();
    if( ad == 4 ):
        addOnlineLecture();
    if( ad == 5 ):
        addCourse();
    if( ad == 6 ):
        addFamilyMembers();
    if( ad == 7 ):
        addReads();
    if( ad == 8 ):
        addStudyMaterial();


def option2():
    """
    Function to implement option 1
    """
    print("Not implemented")


def option3():
    """
    Function to implement option 2
    """
    print("Not implemented")


def option4():
    """
    Function to implement option 3
    """
    print("Not implemented")


def studentAdmission():
    """
    This is a sample function implemented for the refrence.
    This example is related to the Employee Database.
    In addition to taking input, you are required to handle domain errors as well
    For example: the SSN should be only 9 characters long
    Sex should be only M or F
    If you choose to take Super_SSN, you need to make sure the foreign key constraint is satisfied
    HINT: Instead of handling all these errors yourself, you can make use of except clause to print the error returned to you by MySQL
    """
    try:
        # Takes emplyee details as input
        row = {}
        print("Enter new student's details: ")
        name = input("Full Name: ")
        row["full_name"] = name;
        row["rollno"] = input("Roll No.: ")
        row["dob"] = input("Birth Date (YYYY-MM-DD): ")
        row["gender"] = input("Gender: (Male/Female/Others): ")
        print("Course id(format: (Exam_to_appear)_subjectID)\nFor example JEE_MATH01, MED_BIO02")
        row["course_id"] = input("Please enter the course id for the course student is enrolled in")
        query = "INSERT INTO students(rollno, course_id, full_name, dob, gender) VALUES('%s', '%s', '%s', '%s', '%s')" % (
            row["rollno"], row["course_id"], row["full_name"], row["dob"], row["gender"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def addBranch():

    try:
        row = {}
        print("Enter new branch details")
        row["name"] = input("Name: ")
        row["address"] = input("Address: ")
        row["pincode"] = input("Pincode(6 digit): ")
        row["branchcode"] = input("Branch code(First 3-4 letters of the city followed by 2digit no. like KOTA02): ")

        query = "INSERT INTO branch(pincode, branchcode, name, address) VALUES('%s', '%s', '%s', '%s')" % (
            row["pincode"], row["branchcode"], row["name"], row["address"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted into database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def addStaff():

    try:
        row = {}
        print("Enter new Staff details")
        row["staff_id"] = input("Staff_id(First letter should be S followed by a non 0 int without preceding 0s): ")
        row["salary"] = input("Enter salary(correct upto 2 decimals XD): ")
        row["branchcode"] = input("Branch code for the branch where employed(First 3-4 letters of the city followed by 2digit no. like KOTA02): ")
        row["name"] = input("Full name of the employee: ")
        row["working_hours"] = input("Expected working hours(no. of hours followed by 'hour' without spaces): ")

        query = "INSERT INTO staff(staff_id, salary, branchcode, name, working_hours) VALUES('%s', '%s', '%s', '%s', '%s')" % (
            row["staff_id"], row["salary"], row["branchcode"], row["name"], row["working_hours"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted into database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def addOnlineLecture():
    try:

        print("Enter Online Lecture Details")
        row = {}
        row["topic_name"] = input("Topic Name: ")
        row["staff_id"] = input("Staff Id of the teacher who is tutoring the video(First letter should be S followed by a non 0 int without preceding 0s): ")
        row["duration"] = input("Duration of the online lecture(no. of mins followed by space followed by 'min': ")

        query = "INSERT INTO online_lecture(topic_name, staff_id, duration) VALUES('%s', '%s', '%s')" % (row["topic_name"], row["staff_id"], row["duration"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted into database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def addCourse():

    try:

        row = {}
        print("Enter New Course Details")
        row["coursename"] = input("Course name(name of the exam to appear): ")
        row["session"] = input("Session(YYYY): ")
        print("Course id(format: (Exam_to_appear)_subjectID)\nFor example JEE_MATH01, MED_BIO02")
        row["course_id"] = input("Course Id: ")
        row["staff_id"] = input("Staff Id of the teacher taking the course(First letter should be S followed by a non 0 int without preceding 0s): ")
        row["fee"] = input("Fee(in Rs, upto 2 decimals: ")
        # have to make a function so that we can count the no. of students in a course

        query = "INSERT INTO course(course_id, staff_id, C_name, session, fee, num_of_students_enrolled) VALUES('%s', '%s', '%s', '%s', '%s', '%s')" % (
            row["course_id"], row["staff_id"], row["coursename"], row["session"], row["fee"], '0')

        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted into database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def addFamilyMembers():

    try:

        row = {}
        print("Enter Family member details")
        row["name"] = input("Name of the Family member: ")
        row["rollno"] = input("Roll number of the student related to the family memeber(format: positive integer): ")
        row["phone_no"] = input("Phone no. of the family member: ")
        row["address"] = input("Address of the member(expected to be same as student): ")

        query = "INSERT INTO student_family_member_name(rollno, name, phone_no) VALUES('%s', '%s', '%s')" % (row["rollno"], row["name"], row["phone_no"])

        print(query)
        cur.execute(query)
        con.commit()

        query = "INSERT INTO student_family_address(student_rollno, address) VALUES('%s', '%s')" % (row["rollno"], row["address"])
        cur.execute(query)
        con.commit()
        print(query)
        print("Inserted into database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def addReads():

    try:
        print("Enter the details about the study_material given to a student")
        row = {}
        row["rollno"] = input("Roll no of the student(format: +ve int): ")
        row["study_material_id"] = input("ID of the study material given to the specified student(format: X_SUBJ00): ")

        query = "INSERT INTO `reads`(rollno, study_material_id) VALUES('%s', '%s')" % (row["rollno"], row["study_material_id"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted into database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def addStudyMaterial():

    try:

        print("Enter the details of the new study material")
        row = {}
        row["id"] = input("ID of the study material(format: X_SUBJ00): ")
        row["difficulty_level"] = input("Approximate difficulty level of the study material(Easy/Medium/Hard): ")

        query = "INSERT INTO study_material(id, difficulty_level) VALUES('%s', '%s')" % (row["id"], row["difficulty_level"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted into database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return


def dispatch(ch):
    """
    Function that maps helper functions to option entered
    """

    if(ch == 1):
        option1();
    elif(ch == 2):
        option2()
    elif(ch == 3):
        option3()
    elif(ch == 4):
        option4()
    else:
        print("Error: Invalid Option")


# Global
while(1):
    tmp = sp.call('clear', shell=True)
    
    username = input("Username: ")
    password = input("Password: ")

    try:
        # Set db name accordingly which have been create by you
        # Set host to the server's address if you don't want to use local SQL server 
        con = pymysql.connect(host='localhost',
                              user=username,
                              password=password,
                              db='COACHING',
                              cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('clear', shell=True)

        if(con.open):
            print("Connected")
        else:
            print("Failed to connect")

        tmp = input("Enter any key to CONTINUE>")

        with con.cursor() as cur:
            while(1):
                tmp = sp.call('clear', shell=True)
                print("1. Make a change to the database")  # Hire an Employee
                print("2. Option 2")  # Fire an Employee
                print("3. Option 3")  # Promote Employee
                print("4. Option 4")  # Employee Statistics
                print("5. Logout")
                ch = int(input("Enter choice> "))
                tmp = sp.call('clear', shell=True)
                if ch >= 5:
                    break
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE>")

    except:
        tmp = sp.call('clear', shell=True)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")

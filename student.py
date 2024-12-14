# ----------------------------------------------------------------
# Author: John Kappler, Zayd Siwan
# Date: October 23rd - November 21st, 2023
#
# This module supports changes in the registered courses
# for students in the class registration system.  It allows
# students to add courses, drop courses and list courses they are
# registered for.
# -----------------------------------------------------------------

def list_courses(s_id, c_roster):
    # ------------------------------------------------------------
    # Author: Zayd Siwan
    # This function displays all the courses, indicates which ones
    # in which the student is enrolled, and counts the courses a
    # student has registered for. It has two parameters: s_id is the
    # ID of the student; c_roster is the list of class rosters.
    # This function has no return value.
    # -------------------------------------------------------------
    enrolled_courses = []
    for course, roster in c_roster.items():
        if s_id in roster:
            enrolled_courses.append(course)

    print("\nCourses:", end="\n")
    for course in c_roster.keys():
        if course in enrolled_courses:
            print(course, "(Enrolled)", end="\n")
        else:
            print(course, end="\n")

    print("Total courses enrolled:", len(enrolled_courses))
    print("")


def add_course(s_id, c_roster, c_max_size):
    # -----------------------------------------
    # John Kappler
    # 11/11/2023
    # add_course function in the student module
    # allows the user to enroll in a course
    # Program checks that course exists and has
    # available spaces
    # -----------------------------------------
    # Collects user input
    course_choice = input(f"\nEnter course you want to add: ")

    # Check if the course exists in the course roster
    if course_choice not in c_roster:
        print(f"Course not found\n")
        return

    '''
    Check if the student is already enrolled in the course
    The get function allows us to handle situations
    where the course_choice supplied doesn't exist. 
    The brackets indicate that we will default
    to an empty list in such a case
    '''
    # Create an enrolled_students list by taking elements
    # from the c_roster dictionary
    enrolled_students = c_roster.get(course_choice, [])
    if s_id in enrolled_students:
        print(f"You are already enrolled in that course.\n")
        return

    '''
    Check if the course is full
    Once again, we use get to handle a possible scenario.
    Here, if the course does not exist, the max size defaults
    to zero
    '''
    if len(enrolled_students) >= c_max_size.get(course_choice, 0):
        print(f"Course already full.\n")
        return

    # Add a student to the enrolled_students list
    enrolled_students.append(s_id)
    # We make sure to update the course roster for the
    # specific course with the new addition
    c_roster[course_choice] = enrolled_students
    print(f"Course added\n")


def drop_course(s_id, c_roster):
    # ------------------------------------------------------------
    # Author: Zayd Siwan
    # This function drops a student from a course.  It has two
    # parameters: s_id is the ID of the student to be dropped;
    # c_roster is the list of class rosters. This function asks
    # the user to enter the course he/she wants to drop.  If the course
    # is not offered, display error message and stop.  If the student
    # is not enrolled in that course, display error message and stop.
    # Remove student ID from the course’s roster and display a message
    # if there is no problem.  This function has no return value.
    # -------------------------------------------------------------
    dropping_course = input("\nEnter the course you want to drop: ")

    if dropping_course not in c_roster:
        print("Course not found.\n")
        return

    if s_id not in c_roster[dropping_course]:
        print("You are not enrolled in that course.\n")
        return

    c_roster[dropping_course].remove(s_id)
    print(f"Course dropped \n")

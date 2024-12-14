# ----------------------------------------------------------------
# Author: Nkaujhnub Vue, John Kappler
# Date: October 23rd, 2023 - November 21st, 2023
#
# This program creates a class registration system.  It allows
# students to add courses, drop courses and list courses they are
# registered for. It also allows students to review the tuition
# # costs for their course roster.
# -----------------------------------------------------------------
import student
import billing


def main():
    # ------------------------------------------------------------
    # Author: Nkaujhnub Vue, Jim Matlock
    # This function manages the whole registration system.  It has
    # no parameter.  It creates student list, in_state_list, course
    # list, max class size list and roster list.  It uses a loop to
    # serve multiple students. Inside the loop, ask student to enter
    # ID, and call the login function to verify student's identity.
    # Then let student choose to add course, drop course or list
    # courses. This function has no return value.
    # -------------------------------------------------------------

    student_list = [('1001', '111'), ('1002', '222'),
                    ('1003', '333'), ('1004', '444'),
                    ('1005', '555'), ('1006', '666')]
    student_in_state = {'1001': True,
                        '1002': False,
                        '1003': True,
                        '1004': False,
                        '1005': False,
                        '1006': True}

    course_hours = {'CSC101': 3, 'CSC102': 4, 'CSC103': 5,
                    'CSC104': 3, 'CSC105': 2}
    course_roster = {'CSC101': ['1004', '1003'],
                     'CSC102': ['1001'],
                     'CSC103': ['1002'],
                     'CSC104': [],
                     'CSC105': ['1005', '1002']}
    course_max_size = {'CSC101': 3, 'CSC102': 2, 'CSC103': 1,
                       'CSC104': 3, 'CSC105': 4}

    session_tracker = 'y'
    while session_tracker == 'y':  # track user's session
        s_id = input("Enter ID to log in, or 0 to quit: ")  # ask user for input

        if s_id == '0':  # if a user puts in 0, end session
            session_tracker = 'n'  # change session tracker
            print(f'\nSession ended.')
        else:  # otherwise,
            if login(s_id, student_list):  # try to log in
                show_menu()  # show menu for user
                user_action = ' '
                while user_action != '0':  # while option is not to quit,
                    user_action = input("What do you want to do? ")  # ask user what they want to do

                    # then, perform actions accordingly
                    if user_action == '0':
                        session_tracker = 'y'
                        print(f"\nSession ended.")
                    elif user_action == '1':  # do action 1
                        student.add_course(s_id, course_roster, course_max_size)
                        show_menu()
                    elif user_action == '2':  # do action 2
                        student.drop_course(s_id, course_roster)
                        show_menu()
                    elif user_action == '3':  # do action 3
                        student.list_courses(s_id, course_roster)
                        show_menu()
                    elif user_action == '4':  # do action 4
                        billing.display_bill(s_id, student_in_state, course_roster, course_hours)
                        show_menu()
                    else:
                        # if user doesn't select an option 0-4,
                        # print error message
                        print(f"Error: Please select an option from 0-4.")


def login(s_id, s_list):
    # ------------------------------------------------------------
    # Author: Nkaujhnub Vue
    # This function allows a student to log in.
    # It has two parameters: s_id and s_list, which is the student
    # list. This function asks user to enter PIN. If the ID and PIN
    # combination is in s_list, display message of verification and
    # return True. Otherwise, display error message and return False.
    # -------------------------------------------------------------
    user_pin = input("Enter PIN: ")

    # create dict to get the solo student info
    s_dict = {k: v for (k, v) in s_list if k == s_id}
    # check if the dictionary is empty
    if not s_dict:
        # if empty, error msg + return false
        print(f"IP or PIN incorrect\n")
        return False
    else:
        # otherwise, see if user pin matches info
        # if user pin doesn't match, error msg + return false
        if user_pin != s_dict[s_id]:
            print(f"IP or Pin incorrect\n")
            return False
        else:
            # otherwise, confirm w/ user + return true
            print(f"IP and PIN verified\n")
            return True


def show_menu():
    # ------------------------------------------------------------
    # Author: John Kappler
    # This function displays the action menu to the logged in student.
    # It takes no parameters and returns no values.
    # -------------------------------------------------------------
    print(f"Action Menu")
    print(f"----------")
    print(f"1: Add course")
    print(f"2: Drop course")
    print(f"3: List course")
    print(f"4: Show bill")
    print(f"0: Logout")


main()

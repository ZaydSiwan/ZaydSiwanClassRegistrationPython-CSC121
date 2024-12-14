# ----------------------------------------------------------------
# Author: Nkaujhnub Vue, Jack Kappler, Zayd Siwan
# Date: October 28th, 2023
#
# This module calculates and displays billing information
# for students in the class registration system.  Student and
# class records are reviewed and tuition fees are calculated.
# -----------------------------------------------------------------
import datetime
from datetime import datetime

# The rate of which In-State Students are charged per credit hour
IN_STATE_RATE = 225
# The rate of which Out-Of-State Students are charged per credit hour
OUT_OF_STATE_RATE = 850


def display_bill(s_id, s_in_state, c_rosters, c_hours):
    # ------------------------------------------------------------
    # This function displays the student's bill. It takes four
    # parameters: s_id, the student id; s_in_state, the list of
    # in-state students; c_rosters, the rosters of students in
    # each course; c_hours, the number of hours in each course.
    # The function has no return value.
    # ------------------------------------------------------------

    # ------------------------------------------------------------
    # HEADER SECTION OF SUMMARY
    print(f"\nTuition Summary")
    print(f"Student: {s_id},", end=" ")

    total_cost = 0
    hrs_total = 0
    course_list = []
    course_cost_dict = {}
    # ------------------------------------------------------------

    if s_in_state[s_id]:  # ]]if the student is in-state
        print(f"In-State Student")
        # check if student is in course roster
        for course, students in c_rosters.items():
            # if student is in the roster, add to course_list
            course_list = [course for course, students in c_rosters.items() if s_id in students]
        # now with course_list, determine cost of each course
        for i in range(len(course_list)):
            course_cost_dict = {course: c_hours[course] * IN_STATE_RATE for course in course_list}
    else:
        print(f"Out-Of-State Student")
        # check if student is in course roster
        for course, students in c_rosters.items():
            # if student is in the roster, add to course_list
            course_list = [course for course, students in c_rosters.items() if s_id in students]
        # now with course_list, determine cost of each course
        for i in range(len(course_list)):
            course_cost_dict = {course: c_hours[course] * OUT_OF_STATE_RATE for course in course_list}

    # ------------------------------------------------------------
    # SECOND HALF PRINTING PORTION
    # get the current time
    now = datetime.now()
    curr_date = now.strftime("%B %d, %Y")
    curr_time = now.strftime("%I:%M%p")
    print(f"{curr_date} at {curr_time}")

    # print dividers + titles
    print(f"Course    Hours    Cost   ")
    print(f"------    -----  ---------")

    # now print courses accordingly
    for key in course_cost_dict.keys():
        # increment total_cost & total hrs
        total_cost += course_cost_dict[key]
        hrs_total += c_hours[key]
        print(f"{key: <14}", end="")
        print(f"{c_hours[key]: <2}", end="$")
        print(f"{float(course_cost_dict[key]):>9.2f}")

    # now, print the total
    print(f"\t\t-------  ---------")
    print(f"Total", end="")
    print(f"{hrs_total: >10}", end="")
    print(f" $ {total_cost:>8.2f}\n")
    # ------------------------------------------------------------

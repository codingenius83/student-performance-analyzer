"""
name: caleb
period: pm
student performance analyzer
"""
#program introduction
print('='*30)
print('STUDENT PERFORMANCE ANALYZER')
print('='*30)
name = input('\nwhat is the students name?')
grade_lvl = int(input('\nwhat grade lvl is the student in?(1-12)'))
assignment_avg = input('\nwhat is the students assignment average?')
quiz_avg = input('\nwhat is the students quiz average?')
test_avg = input('\nwhat is the students test average?')
attendance_percentage = float(input('\nwhat is the students attendance percentage?'))
missing_assignments = int(input('\nhow many missing assignments does the student have?'))
def calculate_grade(assignment_average, quiz_average, test_average):
    assignments_w = 3/10
    quizzes_w = 3/10
    tests_w = 2/5
    overall_grade = assignment_average * assignments_w + quiz_average * quizzes_w + test_average * tests_w
    return overall_grade
number_grade = calculate_grade(assignment_avg, quiz_avg, test_avg)
print(number_grade)
def letter_grader(num_grade):
    letter_grad = ''
    if num_grade <= 0:
        num_grade == 0
    if num_grade < 60:
        letter_grad = 'F'
    elif num_grade >= 60 and num_grade < 70:
        letter_grad = 'D'
    elif num_grade >= 70 and num_grade < 80:
        letter_grad = 'C'
    elif num_grade >= 80 and num_grade < 90:
        letter_grad = 'B'
    else:
        letter_grad = 'A'
    return letter_grad
letter_grade = letter_grader(number_grade)
print(letter_grade)
def attendance_status_checker(attendance):
    status = ''
    if attendance <= 0:
        attendance == 0
    if attendance < 80:
        status = 'poor attendance'
    elif attendance >= 80 and attendance < 90:
        status = 'attendance warning'
    elif attendance >= 90 and attendance < 95:
        status = 'good attendance'
    else:
        status = 'excellent attendance'
    return status
attendance_status = attendance_status_checker(attendance_percentage)
print(attendance_status)
def assignment_status_checker(missing_assigns):
    status = ''
    if missing_assigns <= 0:
        missing_assigns = 0
    if missing_assigns == 0:
        status = 'Excellent'
    elif missing_assigns == 1 or missing_assigns == 2:
        status = 'good'
    elif missing_assigns == 3 or missing_assigns == 4:
        status = 'warning'
    else:
        status = 'critical'
    return status
assignment_status = assignment_status_checker(missing_assignments)
print(assignment_status)
def check_eligibility(overall_grade, attendance, assignments_missing):
    academic_eligibility = ''
    reason = ''
    if overall_grade >= 70:
        if attendance >= 90:
            if assignments_missing <= 2:
                academic_eligibility = 'ELIGIBLE'
                reason = 'student passed all the requirements'
            else:
                academic_eligibility = 'NOT ELIGIBLE'
                reason = 'too many missing assignments'
        else:
            academic_eligibility = 'NOT ELIGIBLE'
            reason = 'attendance is too low'
    else:
        academic_eligibility = 'NOT ELIGIBLE'
        reason = 'overall grade is too low'
    return academic_eligibility, reason
acadmic_eligibility, reason = check_eligibility(number_grade, attendance_percentage, missing_assignments)




        
        


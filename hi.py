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
grade_lvl = int(input('\nwhat grade lvl is the student in?(9-12)'))
assignment_avg = int(input('\nwhat is the students assignment average?'))
quiz_avg = int(input('\nwhat is the students quiz average?'))
test_avg = int(input('\nwhat is the students test average?'))
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
academic_eligibility, reason = check_eligibility(number_grade, attendance_percentage, missing_assignments)
print(f'academic eligibility: {academic_eligibility}\nreason: {reason}')
def check_high_honors(overall_grade, attendance, missing_assignments):
    high_honors = ''
    reason = ''
    if overall_grade >= 90:
        if attendance >= 95:
            if missing_assignments == 0:
                high_honors = 'YES'
                reason = 'meet all requirements'
            else:
                high_honors = 'NO'
                reason = 'student has missing assignments'
        else:
            high_honors = 'NO'
            reason = 'attendance requirement not met'
    else:
        high_honors = 'NO'
        reason = 'grade requirement not met'
    return high_honors, reason
def check_good_standing(overall_grade, attendance):
    good_standing = ''
    if overall_grade >= 70 and  attendance >= 90:
        good_standing = 'YES'
    else:
        good_standing = 'NO'
    return good_standing
def check_support(overall_grade, attendance):
    additional_support = ''
    if overall_grade < 70 or attendance < 80:
        additional_support = 'recommended'
    else:
        additional_support = 'not needed'
    return additional_support
print('\n\n\n')
username = input('enter username: ')
pin = input('enter pin: ')
if username == 'students':
    if pin == '1234':
        print('login successful')
    else:
        print('login failed: inncorrect pin')
else:
    print('login failed: inncorrect username') 
def grade_level_message(grade_level):
    if grade_level == 9:
        return 'welcome to your freshmen year'
    elif grade_level == 10:
        return 'keep building your skills'
    elif grade_level == 11:
        return 'keep pushing'
    elif grade_level == 12:
        return 'finish strong'
    else:
        return 'invalid grade level'
def strongest_category(assignment_average, quiz_average, test_average):
    strongest_category = ''
    if assignment_average > quiz_average > test_average or assignment_average > test_average > quiz_average:
        strongest_category = 'assignments'
    elif quiz_average > assignment_average > test_average or quiz_average > test_average > assignment_average:
        strongest_category = 'quizzes'
    elif test_average > assignment_average > quiz_average or test_average > quiz_average > assignment_average:
        strongest_category = 'tests'
    else:
        if assignment_average == quiz_average == test_average:
            strongest_category = 'all the same'
        elif assignment_average > quiz_average and assignment_average == test_average:
            strongest_category = 'assignments and tests'
        elif assignment_average > test_average and assignment_average == quiz_average:
            strongest_category = 'assignments and quizzes'
        elif quiz_average > assignment_average and quiz_average == test_average:
            strongest_category = 'quizzes and tests'
    return strongest_category
print('\n\n\n', '='*25, '\nstudent summary\n', '='*25)
print(f'\n\nstudent: {name}\ngrade level: {grade_lvl}')
print(f'\n\nassignment average: {assignment_avg}\nquiz average: {quiz_avg}\ntest average: {test_avg}')
print(f'\n\noverall grade: {number_grade}\nattendance: {attendance_percentage}\nmissing assignments: {missing_assignments}')
print('\n\n', '='*25)

        
        


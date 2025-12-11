# Own Project 01
# Revision Lesson on How to Solve Quadratic Equations
# Using the quadratic formula
import math
import cmath
import time

# Function: Display instructions on how to solve quadratic equations
def show_how_to():
    print("\\==============================================================//")
    print("                         THEORY NOTES")
    print("             Finding the roots of a quadratic equation")
    print("\\==============================================================//")
    print("For the equation,")
    print("    ax**2 + bx + c = 0")
    print("You can determine one or two possible values of x (roots).")
    print("NOTE: a must not equal 0")
    print(".................................................................")
    time.sleep(2)
    print("")
    print("The quadratic formula below can be used to find the roots")
    print("          x = [-b + sqrt(b**2 - 4ac)] / (2a)")
    print("or        x = [-b - sqrt(b**2 - 4ac)] / (2a)")
    print(".................................................................")
    time.sleep(2)
    print("")
    print("In the above formula, (b**2 - 4ac) is known as the discriminant")
    print("")
    print("There are 3 types of roots based on the discriminant value:")
    print("1. When discriminant > 0, the roots are real and different")
    print("2. When discriminant = 0, the roots are real and equal (the same)")
    print("1. When discriminant < 0, the roots are complex and different")
    print("-----------------------------------------------------------------")

# Create student profile and store in a dictionary
print("\\==============================================================//")
print("                          LESSON")
print("             Finding the roots of a quadratic equation")
print("\\==============================================================//")
print("")
print("Create student profile for this lesson:")
name = input("What is your name? ")
year_group = input("What year group are you in school? ")
school = input("What is the name of your school? ")
student_profile = {
    "student_name": name,
    "student_year_group": year_group,
    "student_school": school
}
print("")
time.sleep(2)

# Call function to show notes on how to solve quadratic equations
show_how_to()
print("")

# Function: Check quiz answers
def check_quiz_answers(quiz_answer, student_quiz_answer, q_number, correct_answer):
    quiz_answer.append(correct_answer)
    answer_entered = input("Enter you answer here (a/b/c): ")
    student_quiz_answer.append(answer_entered)
    l_number = q_number - 1 # list number
    # print(q_number)
    # print(quiz_answer)
    # print(student_quiz_answer)

    if student_quiz_answer[l_number] == quiz_answer[l_number]:
        print("Correct!")
    else:
        print(f"Incorrect. Take note that the correct answer is: {quiz_answer[l_number]}")
    print("")

# Function: Theory Quiz
def quiz():
    print("===============================")
    print("         Theory Quiz")
    print("===============================")
    print("")
    # quiz_answer = ["a", "c", "b", "c", "a", "b", "a", "a"]
    quiz_answer = []
    student_quiz_answer = []

    # Question 1
    q_number = 1 # Question number
    print("Q1: What do you call a, b or c?")
    print("(a) coefficient     (b) variable     (c) letter")
    correct_answer = "a"
    check_quiz_answers(quiz_answer, student_quiz_answer, q_number, correct_answer)

    # Question 2
    q_number = 2 # Question number
    print("Q2: What type of number should a, b and c (in the quadratic equation) be?")
    print("(a) complex number     (b) boolean     (c) real number")
    correct_answer = "c"
    check_quiz_answers(quiz_answer, student_quiz_answer, q_number, correct_answer)

    # Question 3
    q_number = 3 # Question number
    print("Q3: What should a not equal to?")
    print("(a) negative number     (b) zero     (c) complex number")
    correct_answer = "b"
    check_quiz_answers(quiz_answer, student_quiz_answer, q_number, correct_answer)

    # Question 4
    q_number = 4 # Question number
    print("Q4: What do you call the term, (b**2 - 4ac)?")
    print("(a) unknown     (b) square root term     (c) discriminant")
    correct_answer = "c"
    check_quiz_answers(quiz_answer, student_quiz_answer, q_number, correct_answer)

    # Question 5
    q_number = 5 # Question number
    print("Q5: How many cases should we consider for the discriminant?")
    print("(a) 3     (b) 0     (c) 2")
    correct_answer = "a"
    check_quiz_answers(quiz_answer, student_quiz_answer, q_number, correct_answer)

    # Question 6
    q_number = 6 # Question number
    print("Q6: When discriminant > 0, the roots should be:")
    print("(a) real and equal     (b) real and different     (c) complex and different")
    correct_answer = "b"
    check_quiz_answers(quiz_answer, student_quiz_answer, q_number, correct_answer)

    # Question 7
    q_number = 7 # Question number
    print("Q7: When discriminant = 0, the roots should be: ")
    print("(a) real and equal     (b) real and different     (c) complex and equal")
    correct_answer = "a"
    check_quiz_answers(quiz_answer, student_quiz_answer, q_number, correct_answer)

    # Question 8
    q_number = 8 # Question number
    print("Q8: When discriminant < 0, the root should bes: ")
    print("(a) complex     (b) real and different     (c) real and equal")
    correct_answer = "a"
    check_quiz_answers(quiz_answer, student_quiz_answer, q_number, correct_answer)

    time.sleep(2)
    print("Report card for the following student:")
    print(student_profile)
    print("")

    # Count number of correct answers
    n_correct_answers = 0
    for i in range(len(quiz_answer)):
        if student_quiz_answer[i] == quiz_answer[i]:
            n_correct_answers = n_correct_answers + 1

    print(f"{student_profile["student_name"]}'s score: {n_correct_answers} out of {len(quiz_answer)}.")

    # Grade quiz results
    if n_correct_answers > 7:
        print("Perfect score! Give yourself a pat on the back")
    elif n_correct_answers > 6:
        print("Almost perfect!")
    elif n_correct_answers > 4:
        print("Not bad but there is room for improvement.")
    elif n_correct_answers > 3:
        print("Half correct. Where are your gaps in knowledge?")
    else:
        print("Best to revise this topic again. Here are the notes:")
        time.sleep(2)
        show_how_to()
    print("")
    print("-----------------------------------------------------------------")

# Call Quiz
require_quiz = input("Would you like to start with a quiz on the theory (yes/no?): ")
if require_quiz == "yes":
    quiz()
elif require_quiz == "no":
    print("Okay. We will skip the quiz.")
else:
    print("Invalid answer. Program will terminate here.")
    quit()

print("")
print("====================================")
print("             EXERCISE")
print("    Putting theory into practice")
print("====================================")
print("Let's try finding the roots of a quadratic equation now.")
# Input coefficients
a = float(input("Please enter a: "))
b = float(input("Please enter b: "))
c = float(input("Please enter c: "))
print("")

# Function: Check the type of roots expected
def check_root_type(root_type, student_root_type):
    if student_root_type == root_type:
        print("That is correct.")
    else:
        print("That is incorrect.")

# Function: Countdown to give student time to calculate answers
def countdown_clock():
    countdown = 15
    print(countdown, end = " ")
    while countdown > 1:
        countdown = countdown - 1
        time.sleep(1)
        print(countdown, end = " ")

# Function: Calculate the roots
def find_roots(a, b, c):

# Ask student to calculate the discriminant
    print("First, calculate the discriminant. You have 5 seconds ...")
    time.sleep(5)
    discriminant = b*b - 4*a*c
    student_discriminant = input("What value was your discriminant? ")
    student_discriminant = float(student_discriminant)
    if student_discriminant == discriminant:
        print(f"Correct! The discriminant = {discriminant}")
    else: 
        print(f"Incorrect. Please recalculate using the formula (b**2 - 4ac).")
        print(f"The correct discriminant = {discriminant}.")
    print("")

# Ask student what kind of roots we are expecting
    print("What type of roots should the solution have?")
    print("(a) Real and different     (b) Real and equal     (c) Complex or not real")
    student_root_type = input("Please enter your answer as a, b or c here: ")

# Calculate possible root answers
    sqrt_discriminant = math.sqrt(abs(discriminant))
    x1 = (-b + sqrt_discriminant)/(2*a)
    x2 = (-b - sqrt_discriminant)/(2*a)
    x = -b /(2*a)

# Assign calculated root answers based on the type of discriminant
    if discriminant > 0:
        root_type = "a"
        check_root_type(root_type, student_root_type)
        print("Discriminant > 0. Therefore roots will be real and different.")
        print("")
        print("Please calculate the roots now. You have 15 seconds before the answers appear ...")
        countdown_clock()
        print("")
        sqrt_discriminant = math.sqrt(discriminant)
        print(f"The roots are {x1} and {x2}.")
    elif discriminant == 0:
        root_type = "b"
        check_root_type(root_type, student_root_type)
        print("Discriminant = 0. Therefore roots will be real and the same.")
        print("")
        print("Please calculate the roots now. You have 15 seconds before the answers appear ...")
        countdown_clock()
        print("")
        x = -b / (2*a)
        print(f"The roots are both = {x}.")
    else:
        root_type = "c"
        check_root_type(root_type, student_root_type)
        print("Discriminant < 0. The roots are complex or not real numbers.")
        time.sleep(2)
        print("")
        print("Please calculate the roots now. You have 15 seconds before the answers appear ...")
        countdown_clock()
        print("")
        x_complex = sqrt_discriminant / (2*a)
        print(f"The first root = {x} + {x_complex}i")
        print(f"The second root = {x} - {x_complex}i")
    return
        
# Check that a is a non-zero value before finding roots
if a == 0:
    print("a cannot equal 0. This quadratic equation cannot be solved.")
    print("This programme will terminate here.")
    print("Please rerun this programme to reenter a new set of coefficients.")
else:
    find_roots(a, b, c)
    print("")

# Check student's roots answer
    input_last_check = input("Did you calculate the roots correctly? Answer yes/no: ")
    if input_last_check == "yes":
        print("<<<<< WELL DONE! >>>>>")
        print("You can rerun the programme to solve different quadratic equations.")
    else:
        print("That's a shame. Remember to use the formula to find the roots of the quadratic equations:")
        print("          x = [-b + sqrt(b**2 - 4ac)] / (2a)")
        print("or        x = [-b - sqrt(b**2 - 4ac)] / (2a)")
        summary_request = input("Would you like to reread the theory notes of how to solve quadratic equations? Answer yes/no: " )
        if summary_request == "yes":
            show_how_to()
        else:
            print("Okay. If you need to go through the lesson again, rerun this programme.")
import math
import random


# checks users enter yes (y) or no (n)
def yes_no(question):
    while True:
        response = input(question).lower()
        # check the user response, question
        # repeats if users don't enter yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes / no")


# Display game instructions
def instructions():
    print('''
    
    *** Square Side Length Area Test Instructions ***
    
    The program will randomly generate the side length of a square,
    and you need to calculate the corresponding area.
    
    You can choose the number of questions , enter and press Enter for unlimited mode.
    The correct answer will be displayed when the answer is wrong, 
    
    and you can view the answer history and statistics after the end .
    
    ''')


# checks for an integer with optional upper /
# lower limits and an optional exit code for infinite mode
# / quitting the game
def int_check(question, low=None, high=None, exit_code=None):
# if any integer is allowed...
    if low is None and high is None:
        error = "Please enter an integer"

    # if the number needs to be more than an
    # integer (ie: rounds / 'high number')
    elif low is not None and high is None:
        error = (f"Please enter an integer that is "
                 f"more than / equal to {low}")

# if the number needs to between low and high
    else:
        error = (f"Please enter an integer that"
                 f" is between {low} and {high} (inclusive)")

    while True:
        response = input(question).lower()

# Check for infinite mode / exit code
        if response == exit_code:
            return response

        try:
            response = int(response)

            # Check the integer is not too low...
            if low is not None and response < low:
                print(error)

            # check response is more than the low number
            elif high is not None and response > high:
                print(error)

# If response is valid return it
            else:
                return response

        except ValueError:
            print(error)


# Main Routine Starts here

# Intialise game variables
mode = "regular"
rounds_played = 0
end_game = "no"
feedback = ""

# Ask if you want to read the instructions
print("Welcome to the Square Area Quiz")
print()

want_instructions = yes_no("Do you want to read the instructions? ")

# checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instructions()

# Ask user for number of rounds / infinite mode
num_questions = int_check("Please enter the number of questions (enter for unlimited mode)",
                          low=1, exit_code="")

if num_questions == "":
    num_questions = float("infinite")

# Ask user if they want to customise the number range
default_params = yes_no("Do you want to use the default game parameters? ")
if default_params == "yes":
    low_num = 0
    high_num = 10

# Allow user to choose the high / low number
else:
    low_num = int_check("Low Number? ")
    high_num = int_check("High Number? ", low=low_num + 1)

# Initialize game variables
questions_answered = 0
end_quiz = "no"
quiz_history = []
all_answers = []

while questions_answered < num_questions and end_quiz != "yes":
# Generate random edge length (integer between 1-10)
    side_length = random.randint(1, 10)
    correct_area = side_length ** 2
    print(f"topic {questions_answered + 1}")
    print(f"The side length of the square is {side_length}，What is the area？")

# Answering logic
    user_answer = int_check("Please enter your answer (enter xxx to exit)：",
                            low=0, exit_code="xxx")

    if user_answer == "xxx":
        end_quiz = "yes"
        break

    questions_answered += 1
    if user_answer == correct_area:
        feedback = f"Correct! The area is indeed {correct_area}"
        all_answers.append("correct")
    else:
        feedback = f"Wrong! The correct answer is {correct_area}"
        all_answers.append("mistake")

    quiz_history.append(f"Side {side_length}  Your answer:{user_answer} | {feedback}")
    print(feedback)

# Quiz end processing
if questions_answered > 0:

# Statistical data calculation
    correct_count = all_answers.count("correct")

# Display statistics
    print("Test Results")
    print(f"Total answers is {questions_answered} question, correct {correct_count} question")

# View history
    see_history = yes_no("Do you want to view your answer history ？")
    if see_history == "yes":
        print("Answering history ：")
        for item in quiz_history:
            print(item)
    else:
        print("You got scared and quit!")

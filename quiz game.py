def new_game():

    guesses = []
    correct_guesses = 0
    questiion_num = 1

    for key in questions:
        print("***************")
        print(key)
        for i in options[questiion_num-1]:
            print(i)

        guess = input("Enter (A, B, C, D): ").upper()

        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key), guess)
        questiion_num += 1

    display_score(correct_guesses, guesses)


def check_answer(answer, guess):

    if answer == guess:
        print("Correct answer.")
        return 1
    else:
        print("Wrong answer.")
        return 0
# ---------------


def display_score(correct_guesses, guesses):

    print("Result")
    print("**************")
    print("Answer: ", end="")
    for i in questions:
        print(questions.get(i), end="")
    print()

    print("Guesses: ", end="")

    for i in guesses:
        print(i, end="")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your sqore is: "+str(score) + "%")
# --------------------


def play_again():

    response = input("Do you want to play again? (yes/no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False

# --------------------


questions = {
    "Who crerated Python?: ": "A",
    "What yaer was Python created?:": "B",
    "Python was tribute to which comedy group?: ": "C",
    "Is the earth round?: ": "A"
}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Mark Zuckerberg", "D. Bill Gates"],
           ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
           ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
           ["A. True", "B. False", "C Sometimes", "D. It.s parallel"]]


new_game()

while play_again():
    new_game()

print("Bye")

import random


QUESTIONS = [
    {
        "question": "What keyword is used to define a function in Python?",
        "choices": {"a": "func", "b": "define", "c": "def", "d": "function"},
        "answer": "c",
    },
    {
        "question": "Which data type is used to store key-value pairs in Python?",
        "choices": {"a": "list", "b": "tuple", "c": "set", "d": "dictionary"},
        "answer": "d",
    },
    {
        "question": "What does the len() function return?",
        "choices": {
            "a": "The data type of an object",
            "b": "The number of items in an object",
            "c": "The memory size of an object",
            "d": "The index of the last item",
        },
        "answer": "b",
    },
    {
        "question": "Which loop is best when the number of iterations is known?",
        "choices": {"a": "while", "b": "do-while", "c": "for", "d": "repeat"},
        "answer": "c",
    },
    {
        "question": "What value does a function return if no return statement is used?",
        "choices": {"a": "0", "b": "False", "c": "An empty string", "d": "None"},
        "answer": "d",
    },
    {
        "question": "Which operator checks whether two values are equal?",
        "choices": {"a": "=", "b": "==", "c": "!=", "d": "is"},
        "answer": "b",
    },
    {
        "question": "What method adds an item to the end of a list?",
        "choices": {"a": "add()", "b": "insert()", "c": "append()", "d": "push()"},
        "answer": "c",
    },
    {
        "question": "How do you start a comment in Python?",
        "choices": {"a": "//", "b": "#", "c": "/*", "d": "--"},
        "answer": "b",
    },
]


def display_question(number, q):
    print(f"\nQuestion {number}: {q['question']}")
    for letter, text in q["choices"].items():
        print(f"  {letter}) {text}")


def get_answer():
    while True:
        response = input("Your answer (a/b/c/d or 'quit'): ").strip().lower()
        if response in ("a", "b", "c", "d", "quit"):
            return response
        print("Invalid input. Please enter a, b, c, or d.")


def run_quiz(questions, num_questions=5):
    selected = random.sample(questions, min(num_questions, len(questions)))
    score = 0
    asked = 0

    print("=" * 40)
    print("   Welcome to the Python Trivia Quiz!")
    print("=" * 40)
    print(f"\nYou will be asked {len(selected)} questions.")
    print("Type 'quit' at any time to stop early.\n")

    for i, q in enumerate(selected, start=1):
        display_question(i, q)
        answer = get_answer()

        if answer == "quit":
            print("\nQuiz ended early.")
            break

        asked += 1
        if answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            correct_text = q["choices"][q["answer"]]
            print(f"Incorrect. The answer was {q['answer']}) {correct_text}")

    show_results(score, asked)


def show_results(score, asked):
    print("\n" + "=" * 40)
    print("           Quiz Results")
    print("=" * 40)
    if asked == 0:
        print("No questions were answered.")
    else:
        pct = round(score / asked * 100)
        print(f"Score: {score} / {asked} ({pct}%)")
        if pct == 100:
            print("Perfect score!")
        elif pct >= 70:
            print("Great job!")
        else:
            print("Keep studying — you'll get there!")


if __name__ == "__main__":
    run_quiz(QUESTIONS)

import random
import time

# Predefined questions with multiple-choice options
QUESTIONS = [
    {
        "question": "What is the capital of France?",
        "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
        "answer": "C",
    },
    {
        "question": "What is 5 + 7?",
        "options": ["A) 10", "B) 12", "C) 15", "D) 14"],
        "answer": "B",
    },
    {
        "question": "Which programming language is known as the 'language of the web'?",
        "options": ["A) Python", "B) Java", "C) JavaScript", "D) C++"],
        "answer": "C",
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["A) Earth", "B) Jupiter", "C) Mars", "D) Saturn"],
        "answer": "B",
    },
    {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["A) Harper Lee", "B) Mark Twain", "C) J.K. Rowling", "D) Ernest Hemingway"],
        "answer": "A",
    },
]

# Function to play the quiz
def play_quiz():
    print("\n--- Welcome to the Quiz Game! ---")
    print("Answer the questions by choosing A, B, C, or D.")
    print("Each correct answer gives you 1 point.\n")
    
    # Shuffle the questions for variety
    random.shuffle(QUESTIONS)
    
    score = 0
    for i, q in enumerate(QUESTIONS, 1):
        print(f"Question {i}: {q['question']}")
        for option in q["options"]:
            print(option)
        
        # Get the user's answer
        answer = input("Your answer: ").strip().upper()
        while answer not in ["A", "B", "C", "D"]:
            print("Invalid input. Please choose A, B, C, or D.")
            answer = input("Your answer: ").strip().upper()
        
        # Check the answer
        if answer == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.\n")
        
        # Pause for readability
        time.sleep(1)
    
    # Display final score
    print("--- Quiz Over ---")
    print(f"Your final score is: {score}/{len(QUESTIONS)}")
    if score == len(QUESTIONS):
        print("Excellent work! You're a quiz master!")
    elif score > len(QUESTIONS) // 2:
        print("Great job! You did well.")
    else:
        print("Better luck next time! Keep practicing.")
    
    print("\nThank you for playing the Quiz Game!")

# Main function to run the quiz
def main():
    while True:
        print("\n--- Quiz Game Menu ---")
        print("1. Play the Quiz")
        print("2. Exit")
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            play_quiz()
        elif choice == "2":
            print("Goodbye! See you next time.")
            break
        else:
            print("Invalid choice. Please choose 1 or 2.")

if __name__ == "__main__":
    main()

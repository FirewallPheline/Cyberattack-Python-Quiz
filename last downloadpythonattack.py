import random

def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Password is too short."
    elif not any(char.isdigit() for char in password):
        return "Weak: Add some numbers to make it stronger."
    elif not any(char.isupper() for char in password):
        return "Medium: Add uppercase letters to make it stronger."
    else:
        return "Strong: Your password is strong!"

def trivia_game():
    print("Welcome to the Cybersecurity Trivia Game!")
    print("Let's test your knowledge about staying safe online.")
    
    questions = [
        {
            "question": "What is the best way to create a strong password?",
            "options": ["1. Use your name and birthday", "2. Use random letters, numbers, and symbols", 
                        "3. Use 'password123'", "4. Share it with friends for safekeeping"],
            "answer": 2
        },
        {
            "question": "What should you do if you receive an email from an unknown sender with a link?",
            "options": ["1. Click the link to see what it is", "2. Ignore or delete the email", 
                        "3. Reply to ask who it is", "4. Share the link on social media"],
            "answer": 2
        },
        {
            "question": "Which of these is a common type of cybersecurity attack?",
            "options": ["1. Phishing", "2. Baking", "3. Fishing", "4. Painting"],
            "answer": 1
        }
    ]
    
    random.shuffle(questions)
    score = 0
    
    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}: {q['question']}")
        for option in q["options"]:
            print(option)
        try:
            answer = int(input("Your answer (1-4): "))
            if answer == q["answer"]:
                print("Correct!")
                score += 1
            else:
                print("Incorrect.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
    
    print(f"\nGame over! You scored {score}/{len(questions)}.")
    print("Tip: Always use strong passwords and stay alert for phishing attempts.")

def main():
    print("Welcome to CyberSec Trainer!")
    while True:
        print("\nChoose an option:")
        print("1. Play the Trivia Game")
        print("2. Test Password Strength")
        print("3. Quit")
        
        choice = input("Enter your choice (1-3): ")
        if choice == "1":
            trivia_game()
        elif choice == "2":
            password = input("Enter a password to test its strength: ")
            print(check_password_strength(password))
        elif choice == "3":
            print("Thanks for playing! Stay safe online.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()

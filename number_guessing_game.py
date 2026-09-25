import random

secret_number = random.randint(1, 100) 

# Display the welcome message
print("Welcome to GuessMe. \nA fun and exciting number guessing game.")

# Display the difficulty options
print("I'm thinking of a number between 1 and 100.")
print("\nPlease select the difficulty level:")
print("1. Easy (10 chances)")
print("2. Medium (7 chances)")
print("3. Hard (5 chances)")

choice = input("\nEnter your choice (1, 2, or 3): ")

if choice == '1':
    chances = 10
elif choice == '2':
    chances = 7
elif choice == '3':
    chances = 5
else:
    print("Invalid choice! Defaulting to Medium difficulty.")
    chances = 7

print(f"\nGreat! You have chosen difficulty level {choice}.")
print(f"You have {chances} chances to guess the correct number. Let's start!\n")

# The loop runs as long as the player has remaining chances
while chances > 0:
    # 1. Ask for a guess inside the loop and convert it to an integer
    guess = int(input("Enter your guess(A number between 1 and 100): "))
    
    # 2. Check the guess against the secret_number
    if guess == secret_number:
        print("Congratulations! You guessed the correct number!")
        break  # Exit the loop immediately since they won!
    elif guess > secret_number:
        print("Incorrect! The number is lower than your guess.")
    else:
        print("Incorrect! The number is higher than your guess.")
        
    # 3. Reduce remaining chances by 1
    chances -= 1
    print(f"Chances left: {chances}\n")

# If the loop finishes because they ran out of chances
if chances == 0:
    print(f"You've exhausted your guesses! The secret number was {secret_number}.")

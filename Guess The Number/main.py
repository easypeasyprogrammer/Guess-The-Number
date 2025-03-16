import random
import time

#score tracking
wins = 0
losses = 0
best_scores = {
    "Easy": None,
    "Medium": None,
    "Hard": None
}
best_times = {
    "Easy": None,
    "Medium": None,
    "Hard": None
}

def play_game():
    global wins, losses

    print("-- GUESS THE NUMBER --")
    print("Choose a difficulty level:")
    print("1-> Easy: 1-10, 5 attempts")
    print("2-> Medium: 1-50, 7 attempts")
    print("3-> Hard: 1-100, 10 attempts")
    print("Press Q to quit the game")

    #select difficulty level
    while True:
        difficulty = input("Enter 1 2 or 3: ")
        if difficulty.lower() == "q":
            return False

        if difficulty == "1":
            target = random.randint(1, 10)
            chance = 5
            number_range = 10
            level = "Easy"
            break
        elif difficulty == "2":
            target = random.randint(1, 50)
            chance = 7
            number_range = 50
            level = "Medium"
            break
        elif difficulty == "3":
            target = random.randint(1, 100)
            chance = 10
            number_range = 100
            level = "Hard"
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

    count = 0
    print(f"\nGuess a number from 1 to {number_range}.\n")

    # Start timing
    start_time = time.time()

    # Game loop
    while count < chance:
        user_input = input(f"Attempt {count + 1}/{chance}. Enter your number: ")

        if user_input.lower() == "q":
            return False

        # Input validation
        try:
            user_input = int(user_input)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        count += 1

        # Check the guess
        if user_input == target:
            # End timing
            end_time = time.time()
            time_taken = end_time - start_time

            print(f"\n🎉 Congrats! You guessed the number in {count} attempt{'s' if count > 1 else ''}!")
            print(f"⏱️ Time taken: {time_taken:.2f} seconds")

            # Updating wins, best score, and best time
            wins += 1
            if best_scores[level] is None or count < best_scores[level]:
                best_scores[level] = count
                print("🏆 New Best Score!")
            if best_times[level] is None or time_taken < best_times[level]:
                best_times[level] = time_taken
                print("⏱️ New Best Time!")

            break
        elif user_input > target:
            print("❌ Guessed too big. Try smaller.")
        else:
            print("❌ Guessed too small. Try bigger.")

    else:
        print(f"\nOopsie! You're out of attempts. The number was {target}.")
        losses += 1

    #scoreboard
    print("\n📊 Scoreboard:")
    print(f"Wins: {wins} | Losses: {losses}")
    print("Best Scores:")
    for level, score in best_scores.items():
        print(f"{level}: {score if score else 'N/A'}")
    print("Best Times:")
    for level, best_time in best_times.items():
        print(f"{level}: {best_time:.2f} seconds" if best_time else f"{level}: N/A")

    print("-" * 50)

    return True

#play again
while True:
    if not play_game():
        break
    play_again = input("\nDo you want to play again? (Y/N): ").strip().lower()
    if play_again != 'y':
        print("Thanks for playing! Goodbye! 👋")
        break

print("-- Game Over --")
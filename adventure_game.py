# Import random and time module
import time
import random

# Define possible colors for the wand and randomly select one
colors = ["blue", "green", "red", "purple", "orange"]
wand_color = random.choice(colors)

# Define possible monsters and randomly select one
monsters = ["Wicked Fairie", "Minotaur", "Golem"]
cave_monster = random.choice(monsters)

# Initialize the player's score and set thresholds for winning and losing
total_score = 0.5
win_threshold = 5
lose_threshold = 0

def print_pause():
    """Print the initial game story with pauses to build atmosphere."""
    print("You find yourself standing in an open field,",
          "filled with grass and yellow wildflowers.")
    time.sleep(2)
    print(f"Rumor has it that a {cave_monster} is somewhere around here",
          "and has been terrifying the nearby village.")
    time.sleep(2)
    print("In front of you is a house.")
    time.sleep(2)
    print("To your right is a dark cave.")
    time.sleep(2)
    print(f"In your hand you hold your trusty {wand_color} magic wand.")
    time.sleep(2)

def again():
    """Handle the game over scenario, prompt for replay,
       and reset the game if needed."""
    global total_score
    print("Your final score is:", total_score)
    time.sleep(2)
    print("GAME OVER")
    time.sleep(2)
    while True:
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again == "yes":
            total_score = 0.5
            main_game()
            break
        elif play_again == "no":
            print("Thank you for playing!")
            print("Your final score is:", total_score)
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def scared():
    """Handle the scenario where the monster is scared
       away and the player wins."""
    global total_score
    print(f"The {cave_monster} Got Scared and is running away!")
    time.sleep(2)
    total_score += 1
    time.sleep(2)
    print("You Won !!")
    time.sleep(2)
    again()

def field2():
    """Handle the scenario where the monster catches
       the player in the field."""
    print(f"The {cave_monster} is catching you !!")
    time.sleep(2)
    print("You Lost !!")
    time.sleep(2)
    again()

def field():
    """Handle the player running away to the field and making a choice."""
    global total_score
    print("You run away to the field.")
    time.sleep(2)
    print(f"The {cave_monster} is running behind you.")
    time.sleep(2)
    print("What will you do?")
    time.sleep(2)
    print("Your score is:", total_score)
    time.sleep(2)
    while True:
        print("Enter 1 to stop running and cast a spell on the monster.")
        time.sleep(2)
        print("Enter 2 to keep running.")
        time.sleep(2)
        answer = input("Please enter 1 or 2: ")

        if answer == "1":
            total_score += 1
            time.sleep(0.5)
            cast()
            break
        elif answer == "2":
            total_score -= 1
            time.sleep(0.5)
            escape()
            break
        else:
            time.sleep(0.5)
            print("Invalid choice.")

def escape():
    """Handle the player deciding to escape and dropping the wand."""
    print("You decide to escape!")
    time.sleep(2)
    print(f"As you escape, your {wand_color} magic wand drops in the field.")
    time.sleep(2)
    print(f"The {cave_monster} catches you!!")
    time.sleep(2)
    print("You Lost !!")
    time.sleep(2)
    again()

def cast():
    """Handle the player casting a spell on the monster."""
    global total_score
    print("You decide to defend yourself.")
    time.sleep(2)
    print(f"You grab your {wand_color} magic wand.")
    time.sleep(2)
    print(f"And start to cast a spell on the {cave_monster}.")
    time.sleep(2)
    print(f"The {cave_monster} is not scared of this spell!!")
    time.sleep(2)
    print("What will you do?")
    time.sleep(2)
    print("Your score is:", total_score)
    time.sleep(2)
    while True:
        print("Enter 1 to cast another spell on the monster.")
        time.sleep(2)
        print("Enter 2 to run away to the field.")
        time.sleep(2)
        answer = input("Please enter 1 or 2: ")

        if answer == "1":
            total_score += 1
            time.sleep(0.5)
            scared()
            break
        elif answer == "2":
            total_score -= 1
            time.sleep(0.5)
            field2()
            break
        else:
            time.sleep(0.5)
            print("Invalid choice.")

def cave():
    """Handle the player peering into the cave and
       deciding their next move."""
    global total_score
    print("You decide to peer into the cave.")
    time.sleep(2)
    print(f"You see a {cave_monster} behind you.")
    time.sleep(2)
    print("What will you do now?")
    time.sleep(2)
    print("Your score is:", total_score)
    time.sleep(2)
    while True:
        print("Enter 1 to cast a spell on the monster.")
        time.sleep(2)
        print("Enter 2 to run away.")
        time.sleep(2)
        answer = input("Please enter 1 or 2: ")

        if answer == "1":
            total_score += 1
            time.sleep(0.5)
            cast()
            break
        elif answer == "2":
            total_score -= 1
            time.sleep(0.5)
            field()
            break
        else:
            time.sleep(0.5)
            print("Invalid choice.")

def house():
    """Handle the player knocking on the door of the house
       and making a choice."""
    global total_score
    print("You knock on the door of the house...")
    time.sleep(2)
    print("You keep knocking but there is no one in the house.")
    time.sleep(2)
    print("What will you do now?")
    time.sleep(2)
    print("Your score is:", total_score)
    time.sleep(2)
    while True:
        print("Enter 1 to continue knocking on the door.")
        time.sleep(2)
        print("Enter 2 to go back to the field.")
        time.sleep(2)
        answer = input("Please enter 1 or 2: ")

        if answer == "1":
            total_score -= 1
            time.sleep(0.5)
            knock()
            break
        elif answer == "2":
            total_score += 1
            time.sleep(0.5)
            field()
            break
        else:
            time.sleep(0.5)
            print("Invalid choice.")

def knock():
    """Handle the player continuing to knock on the door
       and then returning to the field."""
    global total_score
    print("You continue knocking but there is no one in the house.")
    time.sleep(2)
    print(f"You see a {cave_monster} behind you and you run away.")
    time.sleep(2)
    field()

def main_game():
    """Start the main game by presenting initial choices to the player."""
    global total_score
    print_pause()
    print("Enter 1 to knock on the door of the house.")
    time.sleep(2)
    print("Enter 2 to peer into the cave.")
    time.sleep(2)
    while True:
        answer = input("Please enter 1 or 2: ")
        if answer == "1":
            total_score = 1
            time.sleep(0.5)
            house()
            break
        elif answer == "2":
            total_score = 1
            time.sleep(0.5)
            cave()
            break
        else:
            time.sleep(0.5)
            print("Invalid choice.")

# Start the game
main_game()
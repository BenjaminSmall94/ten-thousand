from game_logic import GameLogic
from re import search

rounds_played = 0


def start_game():
    print("Welcome to Ten Thousand\n(y)es to play or (n)o to decline")
    while True:
        play_or_not = input("> ").lower()
        if play_or_not == "y":
            return True
        elif play_or_not == "n":
            print("OK. Maybe another time")
            return False
        else:
            print('Please type "y" or "n"')


def play_game(testing=False):
    banked_score = 0
    shelf_score = 0
    round_num = 0
    dice_remaining = 6
    while banked_score < 10000:
        if shelf_score == 0:
            print(f"Starting round {round_num + 1}\nRolling {dice_remaining} dice...")
        else:
            print(f"Continuing round {round_num + 1}\nRolling {dice_remaining} dice...")
        rolled_dice = GameLogic.roll_dice(dice_remaining, testing)
        print("*** " + ' '.join([str(num) for num in rolled_dice]) + " ***")
        shelfed_dice = shelf_dice(rolled_dice)
        if shelfed_dice is None:
            print(f"Thanks for playing. You earned {banked_score} points")
            return
        roll_score = GameLogic.calculate_score(shelfed_dice)
        if roll_score == 0:
            print("ZILCHED!!")
            shelf_score = 0
            dice_remaining = 6
            round_num += 1
            continue
        shelf_score += roll_score
        dice_remaining -= len(shelfed_dice)
        print(f"You have {shelf_score} unbanked points and {dice_remaining} dice remaining")
        while True:
            print("(r)oll again, (b)ank your points or (q)uit:")
            user_input = input("> ").lower()
            if user_input == "q":
                print(f"Thanks for playing. You earned {banked_score} points")
                return
            elif user_input == "b":
                banked_score += shelf_score
                shelf_score = 0
                dice_remaining = 6
                round_num += 1
                print(f"You banked 50 points in round {round_num}\nTotal score is {banked_score} points")
                break
            elif user_input == "r":
                break
            else:
                print('please type "r" to roll again, "b" to bank your points, or "q" to quit:')

            break
    else:
        print(f"Congratulations!! You have won with {banked_score} points in {round_num} rounds!")


def shelf_dice(rolled_dice):
    while True:
        print("Enter dice to keep, or (q)uit:")
        user_input = input("> ").lower()
        if user_input == "q":
            return None
        if user_input == "":
            return []
        if search(r"[^1-6]", user_input) or len(user_input) > len(rolled_dice):
            print('Please enter "q" or numbers between 1-6 only (no spaces)')
            continue
        shelfed_dice = []
        for char in user_input:
            shelfed_dice.append(int(char))
        if is_valid_selection(shelfed_dice, rolled_dice):
            return shelfed_dice
        else:
            print("You may not enter more of a number than dice you rolled of that number")
            continue


def is_valid_selection(shelfed_dice, rolled_dice):
    for num in shelfed_dice:
        if num not in rolled_dice:
            return False
        elif shelfed_dice.count(num) > rolled_dice.count(num):
            return False
    return True


if __name__ == "__main__":
    if start_game():
        play_game(True)

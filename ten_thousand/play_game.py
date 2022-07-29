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
            return False
        else:
            print('Please type "y" or "n"')


def play_game(predetermined_dice=None):
    banked_score = 0
    round_num = 0
    max_rounds = 20
    while banked_score < 10000 and round_num < max_rounds:
        result = play_round(round_num, predetermined_dice)
        if result is False:
            print(f"Thanks for playing. You earned {banked_score} points")
            return
        else:
            round_num, shelf_score = result[0:2]
            banked_score += shelf_score
            print(f"You banked {shelf_score} points in round {round_num}\nTotal score is {banked_score} points")
    else:
        if banked_score >= 10000:
            print(f"Congratulations!! You have won with {banked_score} points in {round_num} rounds!")
        else:
            print(f"You failed to reach 10,000 in {max_rounds}. You scored {banked_score}. Better luck next time!")


def play_round(round_num, predetermined_dice):
    dice_remaining = 6
    shelf_score = 0
    while True:
        rolling_message(shelf_score, round_num, dice_remaining)
        rolled_dice = roll_dice(dice_remaining, predetermined_dice)
        selection_result = select_score_compare(rolled_dice)
        if selection_result is False:
            return False
        selected_score, roll_score, scoring_dice = selection_result
        if roll_score == 0:
            print_zilch()
            return round_num + 1, 0
        shelf_score += roll_score
        dice_remaining -= len(scoring_dice)
        if dice_remaining == 0:
            dice_remaining = 6
            # print(f"You have {shelf_score} unbanked points and {dice_remaining} dice remaining")
            # continue
        print(f"You have {shelf_score} unbanked points and {dice_remaining} dice remaining")
        user_choice = bank_roll_or_quit()
        if user_choice is False:
            return False
        elif user_choice is True:
            return round_num + 1, shelf_score


def select_score_compare(rolled_dice):
    possible_scorers = GameLogic.get_scorers(rolled_dice)
    if len(possible_scorers) > 0:
        selection_result = select_and_score(rolled_dice)
        if selection_result is False:
            return False
        selected_dice, roll_score, scoring_dice = selection_result
        while len(selected_dice) != len(scoring_dice):
            differences = find_difference(selected_dice, scoring_dice)
            print("Cannot shelf the following dice as they are non scoring")
            print("*** " + ' '.join([str(num) for num in differences]) + " ***")
            print("Please choose again")
            selection_result = select_and_score(rolled_dice)
            if selection_result is False:
                return False
            selected_dice, roll_score, scoring_dice = selection_result
        return selected_dice, roll_score, scoring_dice
    else:
        return [], 0, []


def select_and_score(rolled_dice):
    selected_dice = select_dice(rolled_dice)
    if selected_dice is False:
        return False
    scoring_dice = GameLogic.get_scorers(selected_dice)
    roll_score = GameLogic.calculate_score(scoring_dice)
    return selected_dice, roll_score, scoring_dice


def rolling_message(shelf_score, round_num, dice_remaining):
    if shelf_score == 0:
        print(f"Starting round {round_num + 1}")
    print(f"Rolling {dice_remaining} dice...")


def roll_dice(dice_remaining, predetermined_dice):
    rolled_dice = GameLogic.roll_dice(dice_remaining, predetermined_dice)
    print("*** " + ' '.join([str(num) for num in rolled_dice]) + " ***")
    return rolled_dice


def print_zilch():
    print("****************************************")
    print("**        Zilch!!! Round over         **")
    print("****************************************")


def select_dice(rolled_dice):
    while True:
        print("Enter dice to keep, or (q)uit:")
        user_input = input("> ").lower()
        user_input = user_input.replace(" ", "")
        if user_input == "q":
            return False
        if user_input == "":
            return []
        if search(r"[^1-6]", user_input) or len(user_input) > len(rolled_dice):
            print('You may enter "q" or numbers between 1-6 of the same amount or less than the number of rolled dice')
            continue
        selected_dice = [int(char) for char in user_input]
        if GameLogic.validate_keepers(rolled_dice, selected_dice):
            return selected_dice
        else:
            print("Cheater!!! Or possibly made a typo...")
            print("*** " + ' '.join([str(num) for num in rolled_dice]) + " ***")
            continue


def find_difference(selected_dice, scoring_dice):
    for num in range(1, 7):
        while num in selected_dice and num in scoring_dice:
            selected_dice.remove(num)
            scoring_dice.remove(num)
    return selected_dice


def bank_roll_or_quit():
    while True:
        print("(r)oll again, (b)ank your points or (q)uit:")
        user_input = input("> ").lower()
        if user_input == "q":
            return False
        elif user_input == "b":
            return True
        elif user_input == "r":
            return
        else:
            print('please type "r" to roll again, "b" to bank your points, or "q" to quit:')


if __name__ == "__main__":
    if start_game():
        play_game()
    else:
        print("OK. Maybe another time")

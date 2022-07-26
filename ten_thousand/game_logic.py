import random as r


class GameLogic:

    @staticmethod
    def roll_dice(num_dice):
        rolled_dice = []
        for i in range(num_dice):
            rolled_dice.append(r.randrange(1, 7))
        return tuple(rolled_dice)

    @staticmethod
    def calculate_score(selected_dice):
        shelf_score = 0
        rolled_num = 1
        selected_dice_count = {}
        while rolled_num <= 6:
            if rolled_num == 1:
                ones_count = selected_dice.count(1)
                if ones_count:
                    selected_dice_count[1] = ones_count
                    if selected_dice_count[1] <= 2:
                        shelf_score += 100 * selected_dice_count[1]
                    else:
                        shelf_score += 1000 * (selected_dice_count[1] - 2)
            elif rolled_num == 5 and 1 <= selected_dice.count(5) <= 2:
                selected_dice_count[5] = selected_dice.count(5)
                shelf_score += 50 * selected_dice.count(5)
            else:
                roll_count = selected_dice.count(rolled_num)
                if roll_count:
                    selected_dice_count[rolled_num] = roll_count
                    if selected_dice_count[rolled_num] > 2:
                        shelf_score += rolled_num * 100 * (selected_dice_count[rolled_num] - 2)
            rolled_num += 1
        if len(selected_dice_count) == 6:
            print(selected_dice_count)
            return 1500
        if len(selected_dice_count) == 3:
            if GameLogic.double_trips(selected_dice_count):
                return 1500
        if GameLogic.is_full_house(selected_dice_count):
            print(selected_dice_count)
            if sum(selected_dice_count.values()) == 5:
                return 1500
            else:
                if 1 in selected_dice_count and selected_dice_count[1] == 1:
                    return 1600
                elif 5 in selected_dice_count and selected_dice_count[5] == 1:
                    return 1550
        return shelf_score

    @staticmethod
    def is_full_house(selected_dice_count):
        full_house_criteria = {2: False, 3: False}
        for count in selected_dice_count.values():
            full_house_criteria[count] = True
        if full_house_criteria[2] and full_house_criteria[3]:
            return True
        return False

    @staticmethod
    def double_trips(selected_dice_count):
        for num in selected_dice_count.values():
            if num != 2:
                return False
        return True

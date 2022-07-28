from random import randint


class GameLogic:

    @staticmethod
    def roll_dice(num_dice, round_num=None, predetermined_dice=None):
        if predetermined_dice is None or round_num >= len(predetermined_dice):
            rolled_dice = []
            for i in range(num_dice):
                rolled_dice.append(randint(1, 6))
            return tuple(rolled_dice)
        else:
            return predetermined_dice[round_num]


    @staticmethod
    def get_scorers(selected_dice):
        num_on_dice = 1
        scoring_dice = []
        while num_on_dice <= 6:
            if num_on_dice == 1 or num_on_dice == 5:
                num_count = selected_dice.count(num_on_dice)
                scoring_dice = GameLogic.add_to_scoring_dice(scoring_dice, num_on_dice, num_count)
            num_on_dice += 1
        unique_numbers = len(set(scoring_dice))
        if unique_numbers == 6:
            return 1500, (1, 2, 3, 4, 5, 6)
        if unique_numbers == 3:
            if GameLogic.double_trips(scoring_dice):
                return 1500, tuple(selected_dice)
        return scoring_dice

    @staticmethod
    def calculate_score(scoring_dice):
        roll_score = 0
        num_on_dice = 1
        while num_on_dice <= 6:
            if num_on_dice == 1:
                ones_count = scoring_dice.count(1)
                if ones_count <= 2:
                    roll_score += 100 * ones_count
                else:
                    roll_score += 1000 * (ones_count - 2)
            elif num_on_dice == 5 and scoring_dice.count(5) <= 2:
                roll_score += 50 * scoring_dice.count(5)
            else:
                num_count = scoring_dice.count(num_on_dice)
                if num_count > 2:
                    roll_score += num_on_dice * 100 * (num_count - 2)
            num_on_dice += 1
        unique_numbers = len(set(scoring_dice))
        if unique_numbers == 6:
            return 1500, (1, 2, 3, 4, 5, 6)
        if unique_numbers == 3:
            if GameLogic.double_trips(scoring_dice):
                return 1500, tuple(scoring_dice)
        return roll_score

    @staticmethod
    def add_to_scoring_dice(scoring_dice, num, num_count):
        return [*scoring_dice, *[num for _ in range(num_count)]]

    @staticmethod
    def double_trips(scoring_dice):
        for num in scoring_dice:
            if scoring_dice.count(num) != 2:
                return False
        return True

    @staticmethod
    def validate_keepers(rolled_dice, selected_dice):
        for num in selected_dice:
            if num not in rolled_dice:
                return False
            elif selected_dice.count(num) > rolled_dice.count(num):
                return False
        return True
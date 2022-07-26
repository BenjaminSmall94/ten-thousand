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
        rolled_nums_count = {}
        while rolled_num <= 6:
            if rolled_num == 1:
                ones_count = selected_dice.count(1)
                if ones_count:
                    rolled_nums_count[1] = ones_count
                    if rolled_nums_count[1] <= 2:
                        shelf_score += 100 * rolled_nums_count[1]
                    else:
                        shelf_score += 1000 * (rolled_nums_count[1] - 2)
            elif rolled_num == 5 and 1 <= selected_dice.count(5) <= 2:
                rolled_nums_count[5] = selected_dice.count(5)
                shelf_score += 50 * selected_dice.count(5)
            else:
                roll_count = selected_dice.count(rolled_num)
                if roll_count:
                    rolled_nums_count[rolled_num] = roll_count
                    if rolled_nums_count[rolled_num] > 2:
                        shelf_score += rolled_num * 100 * (rolled_nums_count[rolled_num] - 2)
            rolled_num += 1
        if len(rolled_nums_count) == 6:
            print(rolled_nums_count)
            return 1500
        if len(rolled_nums_count) == 3:
            for num in rolled_nums_count.values():
                if num != 2:
                    break
            return 1500
        return shelf_score

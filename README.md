# Lab 06-08 Code401_d19 - 10,000 Dice Game

1. Lab 06 - Roll Dice, Calculate Score
2. Lab 07 - Shelf dice, bank points, track score/round, implement tests
3. Lab 08 - Find scorers, validate keepers, zilch, hot dice

[Game Logic](ten_thousand/game_logic.py)
[Play Game](ten_thousand/play_game.py)

## Author: Benjamin Small

## How to run application

From the root directory of this project type `python3 ten_thousand/play_game.py` in the terminal/bash. Follow all on-screen instructions to play the game.

## Tests

Run `pytest tests/test_calculate_score.py tests/test_roll_dice.py tests/version_3/test_get_scorers.py tests/version_3/test_validate_keepers.py` from the root directory of this project with pytest installed. Additionally, output can be compared to the tests/version_2 and version_3.txt files. However, the random variable override will need to be clearly specified beforehand to in order to ensure output is 100% the same.

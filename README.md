# Snake Game using Turtle

This is a snake game that is built using Turle and Python commands.

## What the project does?
This project is designed for snake game lovers where you guide your snake to the food and survive as long as you can.
Each time the snake eats food, the score will increase with +1.

Beware of walls!
If you accidentally hit the wall, your snake will die, and sadly game over.
The challenge is to hit the high score before you hit the wall. 😜

## Why the project is useful?
I have created the simple program and sorted it very well so it is easy to understand for beginners in Python. 

Following files in this repository makes it easy to understand the program behind this game.

+ If you go through the repository, you will see a [snake.py file](https://github.com/ArshdeepKaurArora/Snake_Game_using_Turtle/blob/main/snake.py) which contains a class Snake to create a snake and move it around using some amazing methods `create_snake, add_segment, move, extend, up, down, left, right, and reset`.
+ The [food.py file](https://github.com/ArshdeepKaurArora/Snake_Game_using_Turtle/blob/main/food.py) helps to create food for the snake using the class Food. The amazing `refresh` method helps refresh the food's position after snake eats it.
+ The [scoreboard.py file](https://github.com/ArshdeepKaurArora/Snake_Game_using_Turtle/blob/main/scoreboard.py) shows the score on the screen usinf Scoreboard class. This scoreboard updated and appeared wonderful using the mthods `update_score, game_over, and increase_score`.
+ The [highscore.txt file](https://github.com/ArshdeepKaurArora/Snake_Game_using_Turtle/blob/main/high_score.txt) is keeping the track of last highest score on the game.
+ Finally [main.py file](https://github.com/ArshdeepKaurArora/Snake_Game_using_Turtle/blob/main/main.py) create objects from all the required classes, create screen from turtle, and apply while loop for continous working of snake game.

## How user can started with the project

1. Install current version of Python(I have user python 3.11.1).
2. Check the preinstalled packages like turtle and random.
3. Go to the main.py and run the program.




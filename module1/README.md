# AI Nanodegree: Project 1

## Sudoku Solver
![1](https://github.com/shauryabit2k18/udacity_artificial_intelligence/blob/master/module1/Capture.PNG)

In Project 1 of Artificial Intelligence Nanodegree we leverage techniques such as constraint propagation and depth first search search to solve sudoku puzzles. I’m assuming that everyone reading this post understands the rules of sudoku — If not, don’t worry, I was not completely familiar with the game before the project.

## Setting UP and Encoding the board
The first task of the project is to assign variables and write functions that can encode the board. Long story short, the goal is to write a function that can take an 81 character input and store the column/row and box value in a Python dictionary. For example,
![2](https://github.com/shauryabit2k18/udacity_artificial_intelligence/blob/master/module1/Capture2.PNG)

Fortunately, the project provided a function that displays the sudoku board once we have it properly encoded.

![3](https://github.com/shauryabit2k18/udacity_artificial_intelligence/blob/master/module1/Capture3.PNG)

The next step is to assign a value to the boxes that have a nonnumerical value. More specifically, replace all boxes that contain ‘.’ with ‘123456789’.

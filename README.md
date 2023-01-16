# Minesweeper Python

This is a simple implementation of the classic minesweeper game in python

## How to Play

1. Input the desired height, width, and number of bombs for the game board
2. The game board will be generated with bombs randomly placed on the board
3. Choose a cell to reveal its contents :
    - If it's a bomb, the game is over and you lose
    - If it's a number, it represents the number of bombs in the surrounding 8 cells
    - If it's 0, all the surrounding cells with 0 bombs will be revealed
4. Continue to choose cells until you either lose or find all the cells without bombs

## Note

- If you choose a cell that you have already chosen, it will be marked as "already chosen"
- If you choose a bomb, the game is over and you lose
- If you clear all the cells without bombs, you win!

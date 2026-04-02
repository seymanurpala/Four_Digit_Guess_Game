# Number Guessing Game (Bulls and Cows)

A console-based guessing game where the player tries to guess a secret 4-digit number. After each guess, feedback is given showing which digits are correct and in the right position.

## How to Play

One player enters a 4-digit number. The guesser then enters attempts each turn and receives feedback with the following symbols.

- `➕` correct digit, correct position
- `⭕` correct digit, wrong position
- `❌` wrong digit

The game ends when all four digits are guessed in the correct position.

## Example

```
Enter a 4-digit number: 5831
Enter your guess: 1234
Result: ❌ ❌ ➕ ❌
Correct position: 1
Total correct digits: 2
```

## Usage

```bash
python guessing_game.py
```

## Requirements

- Python 3.x
- No external libraries required


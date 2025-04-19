#  Secret Code Breaker Game

A simple Python terminal game where the player must guess a randomly generated number — the (secret code) — within a range based on the selected difficulty level.

## 🎮 How It Works:
- You enter your name and select a difficulty:
  - **Easy**: 1 to 10
  - **Medium**: 1 to 50
  - **Hard**: 1 to 100
- The game generates a secret code (a random number in the chosen range).
- You keep guessing until you find the correct number.
- The game gives hints whether your guess is too high or too low.
- After winning, you're asked if you'd like to play again.

## 🛠 Features:
- Difficulty selection
- Personalized greeting
- Random number generation
- Guess counting
- Replay option
- Clear feedback messages

## 💡 Future Improvements:
- Add limited number of attempts
- Track high scores or best performance
- Colorful outputs using `colorama`
- Add sound or animations using `pygame` (for GUI version)
- Save scores to a file


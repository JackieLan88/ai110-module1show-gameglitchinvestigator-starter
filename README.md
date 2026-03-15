# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable.

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: _"How do I keep a variable from resetting in Streamlit when I click a button?"_
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
      The game's purpose is to guess a secret number in a range of numbers. There are three difficulty levels: easy,normla, and hard. Depending on your guesses, you will score an amount of points, you can also use hints to guess the secrete number. Win or lose, you can always restart the game!
- [ ] Detail which bugs you found.
      One of the biggest bugs I noticed was that I was allowed to enter numbers that weren't inside the number ranges in the game I selected. Also, when choosing a level of difficulty, the game remained the same. Hints were also misleading as I kept following along when guessing the number, and in my last attempt, the number wasn't as high/low as I expected. The attempt counter was also off by 1.
- [ ] Explain what fixes you applied.
      Through careful analysis, I observed all the code to fix logical errors and messages that were misleading as the user played in the game. I also removed extra conditional structures and unnecessary castings that were pushing us from winnning. I also ensured that the user's input was between boundaries.

## 📸 Demo

- [![alt text](image-1.png)][Insert a screenshot of your fixed, winning game here]

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]

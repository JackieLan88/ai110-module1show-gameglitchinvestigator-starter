# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

  Current bugs:
  counter for attempts is off by one
  you can input values that are not inside the range 1-100
  you cannot restart the game
  blue prompt box doesn't display the information correctly regarding the ranges of numbers to guess based on diffculty.
  the hint feature is inaccurate and misleading
  there is no visible score feature
  difficulty level drop-down seems to be a search bar

  Expectations:
  - As I expected to have used all the number of attempts I had listed in the counter
  - It was kind of unexpected that the input box received negative numbers
  - I was trying to guess the number as in a binary search approach, since it takes the same amount of guesses ( which is 7-8) to actually know what is the hidden number. Depening on the hints made me think I would actually guess the number when this feature is not accurate
  - I did think there would be like a score at the end of the game since I didn't see ant scoreboard...I thought maybe resetting that game would allow that feature to pop up, but I couldn't restart the game either.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  For this project, I used AI agents Copilot and Claude.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  When changing a conditional statement that caused the secret number variable to become a string, Claude asserted into removing it completely to avoid imcompatiblity for the rest of the code (comparing integers and strings). I verified that this new code implementation was correct by testing the app as it ran in the webpage. The original issue was that comparing an int and a string was categorizing the user's guess with misleading hints (go higher, go lower.) These were reference in the check_guess() function inside the conditional statements, that automatically evaluated the conditions to be false when they could have been true.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  One example of an AI suggestion that might have been incorrect is misleading was when it was modiyfing a instruction for the user that was displayed in the game's website. It recommended to keep the range 1-100 by default in the message: "Guess a number between 1 and 100. Attempts left: 6". I changed the numbers for placeholders low and high: "Guess a number between {low} and {high}. Attempts left: 6"
  I verified this change with running the game/script and observing this details in the website since it is a text-instruction for the user, that is adaptable on the dificulty level selected.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

With my current experience in python, I was able to follow along with the syntax, logic, operations, and if there was a unknown keyword or built-in library function, I would look over official documentation from python to understand the functionality of that feature.

- Describe at least one test you ran (manual or using pytest)and what it showed you about your code.
  Through the same approach of binary search, I executed the program and changed the difficulty level of the game. I started out guessing the number in a range of halves, until I guessed it. It worked! For each bug I had initially noticed in the website, I knew it was crucial to read the whole script to identify the code that was causing them.
- Did AI help you design or understand any tests? How?
  When I first prompted AI to help me generate test cases for the game, it gave me an output file of the attempts to find any bugs within the logic_utils file and the UI app file. This output file had displayed succesful tests that were applied to almost every feature of the game.
  However, in the test_game_logic file, I was surprised to see test cases that addressed bugs that I didn't consider before. For example: accepting decimal inputs from user instead of rejecting them, through truncation.

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.

The secret number kept changing in the app because as each time the script was being executed, the random int secret number from 1-100 was generated and saved as the user attempted to guess the number.

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  Session states ("session_state") is a feature in streamlit that saves the current state of the webpage, including variable data. Reruns are the executions of the script that allow us to continue playing the game until it is eventually st.stop()ped.
- What change did you make that finally gave the game a stable secret number?
  Through the help of claude, I was able to identify the code snippet that retrieved the secret number as the script was being rerunned. We extended the conditional statement to:
  if "secret" not in st.session_state or st.session_state.get("difficulty") != difficulty:
  st.session_state.secret = random.randint(low, high)
  st.session_state.difficulty = difficulty

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

Reading more python code to improve fluid understanding of logic. Only using claude or copilot to do heavy changes in code like changing the logic function of our app to the logic_utils.py file.
One thing I would do differently next time I would with AI is being very careful when accepting suggestions. AI is very powerful in code generation, I am speechless when I see how fast it manages to adjust to corrections.

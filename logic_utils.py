def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    # possible lowercase/uppercase senstive , will difficulty actually be a string?
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 50
    if difficulty == "Hard":
        return 1, 100  # switch normal and hard ranges
    return 1, 100  # if difficulty string doesn't satisfy any condition, return this default value


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."
    #checks if there is an input from the use

    if raw == "":  # if input is nothing, it will send message below
        return False, None, "Enter a guess."

    try:  # if there is input
        if "." in raw:
            value = int(float(raw))  # check if it is "." (function filters out numbers?)
        else:  # when casting as float and number -- there will be an exception if it is any other primitive type that is not a number
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."  # catch exception and return "not a number" message

    return True, value, None  # "else" it is a number


def check_guess(guess: int, secret: int):  # validate user's input to secret target score
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    try:
        if guess == secret:
            return "Win", "🎉 Correct!"
        if guess > secret:
            return "Too High", "📉 Go LOWER!"   # messages weren't coherent, switched hint messages
        return "Too Low", "📈 Go HIGHER!"
    except TypeError:  # typeError exception is used when an operation is applied to two non-compatible datatypes
        g = int(guess)
        s = int(secret) # claude helped me realze that the int casting function was necessary if both guess and secret were strings
        if g == s:
            return "Win", "🎉 Correct!"
        if g > s:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = max(10, 100 - 10 * (attempt_number + 1))
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score

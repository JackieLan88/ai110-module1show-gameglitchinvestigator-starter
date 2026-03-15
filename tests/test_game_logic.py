from logic_utils import check_guess, parse_guess, get_range_for_difficulty, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


# BUG: counter for attempts is off by one
# update_score receives attempt_number AFTER incrementing, so attempt 1 should give 100 - 10*(1+1) = 80
def test_score_on_first_attempt_win():
    score = update_score(0, "Win", 1)
    assert score == 80  # 100 - 10*(1+1) = 80

# BUG: counter for attempts is off by one
# winning on attempt 0 (before increment) would give 100 - 10*(0+1) = 90, which is too high
def test_score_attempt_zero_not_used():
    score = update_score(0, "Win", 0)
    assert score == 90  # documents the off-by-one: attempt_number=0 gives 90, but first real guess is attempt 1


# BUG: you can input values that are not inside the range
# parse_guess should accept numeric strings; range check is done separately in app.py
def test_parse_guess_valid_number():
    ok, value, err = parse_guess("25")
    assert ok is True
    assert value == 25
    assert err is None

def test_parse_guess_empty_string():
    ok, value, err = parse_guess("")
    assert ok is False
    assert err == "Enter a guess."

def test_parse_guess_none():
    ok, value, err = parse_guess(None)
    assert ok is False
    assert err == "Enter a guess."

def test_parse_guess_non_numeric():
    ok, value, err = parse_guess("abc")
    assert ok is False
    assert err == "That is not a number."

def test_parse_guess_decimal_truncates():
    # decimal inputs should be truncated to int, not rejected
    ok, value, err = parse_guess("7.9")
    assert ok is True
    assert value == 7


# BUG: hint feature is inaccurate and misleading
# check_guess with mismatched types (str secret) should still return correct hint
def test_hint_message_too_high():
    outcome, message = check_guess(80, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_hint_message_too_low():
    outcome, message = check_guess(20, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_hint_message_win():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message


# BUG: no score feature / score not updating correctly
def test_score_does_not_increase_on_too_low():
    score = update_score(50, "Too Low", 1)
    assert score == 45  # should decrease by 5

def test_score_on_even_attempt_too_high():
    score = update_score(50, "Too High", 2)
    assert score == 55  # even attempt: +5

def test_score_on_odd_attempt_too_high():
    score = update_score(50, "Too High", 3)
    assert score == 45  # odd attempt: -5

def test_score_never_below_minimum_on_win():
    # win on very late attempt should give at least 10 points
    score = update_score(0, "Win", 20)
    assert score == 10  # max(10, 100 - 10*21) = 10


# BUG FIX: check_guess had 4 params (guess, secret, low, high) and returned "Out of Range"
# internally — but app.py already validates the range before calling check_guess.
# The duplicate range check caused misleading outcomes. Fixed by removing low/high from
# check_guess so it only compares guess vs secret.
def test_check_guess_only_takes_two_args():
    # should not raise TypeError for missing low/high args
    outcome, message = check_guess(5, 10)
    assert outcome in ("Win", "Too High", "Too Low")

def test_check_guess_no_out_of_range_outcome():
    # check_guess should never return "Out of Range" — that's app.py's responsibility
    outcome, _ = check_guess(999, 10)
    assert outcome != "Out of Range"
    assert outcome == "Too High"

def test_check_guess_out_of_range_low_still_compares():
    # a guess below the range should still get "Too Low", not "Out of Range"
    outcome, _ = check_guess(0, 10)
    assert outcome == "Too Low"

def test_easy_range():
    low, high = get_range_for_difficulty("Easy")
    assert low == 1 and high == 20

def test_normal_range():
    low, high = get_range_for_difficulty("Normal")
    assert low == 1 and high == 50

def test_hard_range():
    low, high = get_range_for_difficulty("Hard")
    assert low == 1 and high == 100

def test_unknown_difficulty_fallback():
    # unknown difficulty should not crash and return a default range
    low, high = get_range_for_difficulty("Extreme")
    assert isinstance(low, int) and isinstance(high, int)
    assert low < high


# BUG FIX: Normal and Hard difficulty ranges were swapped —
# Normal returned (1, 100) and Hard returned (1, 50), making Normal
# harder than Hard. Fixed by assigning Hard -> 100, Normal -> 50.
def test_hard_range_is_wider_than_normal():
    # regression: Hard must have a larger upper bound than Normal
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert hard_high > normal_high, (
        f"Hard upper bound ({hard_high}) should be greater than Normal upper bound ({normal_high}); "
        "ranges were previously swapped"
    )

def test_normal_upper_bound_is_50():
    # regression: Normal should be 1-50, not the old swapped value of 1-100
    low, high = get_range_for_difficulty("Normal")
    assert high == 50, f"Normal high should be 50, got {high} (was swapped with Hard)"

def test_hard_upper_bound_is_100():
    # regression: Hard should be 1-100, not the old swapped value of 1-50
    low, high = get_range_for_difficulty("Hard")
    assert high == 100, f"Hard high should be 100, got {high} (was swapped with Normal)"

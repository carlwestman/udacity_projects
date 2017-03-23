import types
import sys
import unittest

NUMBER_LEVELS = 3
MAX_ERRORS = 5
LEVEL_1_TEXT_W_BLANKS = "Python is a widely used high-level programming __1__ for general-purpose __2__, created by Guido van Rossum and first released in 1991. An interpreted language, Python has a design philosophy which emphasizes code __3__ (notably using __4__ indentation to delimit code blocks rather than curly braces or keywords), and a syntax which allows programmers to express concepts in __5__ lines of code than possible in languages such as C++ or Java."
LEVEL_2_TEXT_W_BLANKS = "Python features a __1__ type system and automatic __2__ management and supports multiple __3__ paradigms, including object-oriented, imperative, __4__ programming, and procedural styles. It has a large and comprehensive standard __5__."
LEVEL_3_TEXT_W_BLANKS = "Python __1__ are available for many operating __2__, allowing __3__ code to run on a wide variety of systems. CPython, the reference __4__ of Python, is __5__ source software and has a community-based __6__ model, as do nearly all of its variant implementations. CPython is managed by the non-profit Python Software Foundation."
LEVEL_1_MISSING_WORDS = ["language", "programming", "readability", "whitespace", "fewer"]
LEVEL_2_MISSING_WORDS = ["dynamic", "memory", "programming", "functional", "library"]
LEVEL_3_MISSING_WORDS = ["interpreters", "systems", "Python", "implementation", "open", "development"]
LEVEL_TEXT_LIST = [LEVEL_1_TEXT_W_BLANKS,
                   LEVEL_2_TEXT_W_BLANKS,
                   LEVEL_3_TEXT_W_BLANKS]
MISSING_WORDS_LIST = [LEVEL_1_MISSING_WORDS,
                      LEVEL_2_MISSING_WORDS,
                      LEVEL_3_MISSING_WORDS]


def main():
    levels_played = 0
    attempts = 0
    print "Welcome to my version of the madlibs game."
    print "Try to figure out what words should fill the blanks."

    current_level = choose_level()

    while current_level <= NUMBER_LEVELS:

        # Print intro message depending on users previous game history
        print intro_msg(levels_played=levels_played,
                        current_level=current_level,
                        attempts=attempts)
        # get text and stuff for current_level
        text, corrected_text, missing_words = get_level_text(level=current_level)
        # play Level
        level_outcome = play_level(text=text,
                                   corrected_text=corrected_text,
                                   missing_words=missing_words)
        # Handle Level outcome and decide where to go from here
        cont, current_level, attempts, levels_played = handle_level_outcome(level_outcome=level_outcome,
                                                                            current_level=current_level,
                                                                            attempts=attempts,
                                                                            levels_played=levels_played)
        # If user doesn't want to continue exit game
        if not cont:
            sys.exit("Come back soon!")


def handle_level_outcome(level_outcome, current_level, attempts, levels_played):
    # Input: 0, 1
    # output tuple: BOOL, INT, INT, INT
    # BOOL = Continue to play
    # INT 1 -> Current_level
    # INT 2 -> Attempts
    # INT 3 -> Levels played
    if level_outcome == -1:
        return handel_loss(current_level, attempts, levels_played)
    elif level_outcome == 1:
        return handel_win(current_level, attempts, levels_played)


def handel_win(current_level, attempts, levels_played):
    # prints out success msg, asks user if they want to play next level
    #   or start over again
    # input: Current_level (int), Attempts (int), Levels_played (int)
    # output tuple: BOOL, INT, INT, INT
    # BOOL = Continue to play
    # INT 1 -> Current_level
    # INT 2 -> Attempts
    # INT 3 -> Levels played
    if current_level < NUMBER_LEVELS:
        next_lev = raw_input(
            "\nYou finished level " + str(
                current_level) + ". Wanna play the next level? Type 'yes' to try again. Type anything else to exit.")
        if next_lev == 'yes':
            return True, current_level + 1, 0, levels_played + 1
        elif next == 'no':
            return False, 0, 0, 0
    else:
        start_over = raw_input(
            "\nI need to add some more levels, you've finished them all!! Want to start over? Type 'yes' to start over. Type anything else to exit.")
        if start_over == 'yes':
            return True, 1, 0, 0
        else:
            return False, 0, 0, 0


def handel_loss(current_level, attempts, levels_played):
    # prints out fail msg, asks user if they want to try again
    # input: Current_level (int), Attempts (int), Levels_played (int)
    # output tuple: BOOL, INT, INT, INT
    # BOOL = Continue to play
    # INT 1 -> Current_level
    # INT 2 -> Attempts
    # INT 3 -> Levels played
    print "\nD*mn*t, you failed..."
    again = raw_input("Do you want to try again? Type 'yes' to try again. Type anything else to exit.")
    if again.lower() == 'yes':
        return True, current_level, attempts + 1, levels_played
    else:
        return False, 0, 0, 0


def play_level(text, corrected_text, missing_words):
    # input: Text with blanks, corrected text with filled blanks, missing words list
    # output:
    #       failed to complete each word in less than MAX_ERROR tries --> -1
    #       Completed each word in less than MAX_ERROR tries --> 1
    correct_answers = 0
    while text != corrected_text:
        print string_w_new_line(text)
        print "\nWhat word do you think fits in the blank with placeholder: __" + str(correct_answers + 1) + "__"
        answer = raw_input("Your answer:")
        tries = 0
        while answer != missing_words[correct_answers]:
            if tries >= MAX_ERRORS - 1:
                return -1
            tries += 1  # increment tries for each loop where answer is wrong
            print "\n" + string_w_new_line(text)
            print "\nOops, that was incorrect. Try again. You have " + str(MAX_ERRORS - tries) + " tries left."
            print "What word do you think fits in the blank with placeholder: __" + str(correct_answers + 1) + "__"
            answer = raw_input("Your answer:")
        correct_answers += 1  # increment on correct answer
        text = replace_blanks(text=text, num_correct_answers=correct_answers, missing_words=missing_words)
        print "\nCorrect! Great work!"
    return 1


def choose_level():
    # input: none
    # output: valid level, int
    # Error, if user fails more than MAX_ERRORS times exit game with snooty error msg
    level = None
    tries = 0
    while level not in range(1, NUMBER_LEVELS + 1):
        if tries in range(1, MAX_ERRORS):
            print "\nOops, invalid input, try again."
        if tries >= MAX_ERRORS:
            sys.exit("You suck at following instructions ;-). The game will now exit.")
        level = validate_level(raw_input("What level would you like to start from? Choose level 1, 2 or 3:"))
        tries += 1
    return level


def validate_level(choosen_level):
    # input raw input STR
    # output : level as int or -1 for error
    if choosen_level in str_level_list():
        return int(choosen_level)
    else:
        return -1


def get_level_text(level):
    # input: Int repr. of level
    # output: Tuple: text with blanks, correct_text, list of missing words
    # ERROR = -1, -1, -1
    if level in [1, 2, 3]:
        text = LEVEL_TEXT_LIST[level-1]
        missing_words = MISSING_WORDS_LIST[level-1]
        correct_text = replace_blanks(text, missing_words, all=True)
        return text, correct_text, missing_words
    else:
        return -1, -1, -1


def replace_blanks(text, missing_words, num_correct_answers=0, all=False):
    # input: text with blanks, list of missing words, number of correct
    # answers(default=0) int, all(default=false) if true will replace all
    #   missing words bool num_correct_answers cannot assume value 0 if
    #   all = false and vice versa, returns error
    # output text with correct words placed in blanks
    # error = -1
    if not isinstance(text, types.StringType) \
            or not isinstance(missing_words, types.ListType) \
            or not isinstance(num_correct_answers, types.IntType) \
            or not isinstance(all, types.BooleanType):
        return -1
    elif num_correct_answers == 0 and all is False:
        return -1

    if all:
        for i, word in enumerate(missing_words):
            placeholder = "__" + str(i + 1) + "__"  # construct place_holder
            text = text.replace(placeholder, word)  # replace placeholder with word
        return text
    else:
        placeholder = "__" + str(num_correct_answers) + "__"
        return text.replace(placeholder, missing_words[num_correct_answers - 1])


def intro_msg(levels_played, current_level, attempts):
    # Prints appropriate message depending on where in game user is
    # 3 possible outcomes, all cases should be covered given that inputs are INTs
    if levels_played == 0 and attempts == 0:
        return "\nGreat, you've chosen to start on level " + str(current_level) + ".\nHere is you first challenge: "
    elif levels_played > 0 and attempts == 0:
        return "\nYou want more, huh! Here's your next challenge: "
    else:
        return "\nGreat, lets try again"


def string_w_new_line(string):
    # Input string
    # Prints string with 10 words per line for readability
    text_with_line_break = ""
    words_per_line = 10
    word_list = string.split()
    for i, word in enumerate(word_list):
        if (i % words_per_line) == 0 and i != 0:
            text_with_line_break += "\n"

        text_with_line_break += word + " "

    return text_with_line_break


def str_level_list():
    # No input
    # Output
    #   List of levels as strings
    res = []
    for level in range(1, NUMBER_LEVELS + 1):
        res.append(str(level))
    return res


# Run the program
main()


# Tests
class TestTestableFuncs(unittest.TestCase):
    def test_validate_level(self):
        self.assertEqual(validate_level('1'), 1)
        self.assertEqual(validate_level('2'), 2)
        self.assertEqual(validate_level('3'), 3)
        self.assertEqual(validate_level(1), -1)
        self.assertEqual(validate_level('a'), -1)
        self.assertEqual(validate_level(True), -1)

    def test_replace_blanks(self):
        self.assertEqual(replace_blanks(text="word __1__ word",
                                        missing_words=["missing"],
                                        all=True),
                         "word missing word")
        self.assertEqual(replace_blanks(text="word __1__ word",
                                        missing_words=["missing"],
                                        num_correct_answers=1),
                         "word missing word")

        self.assertEqual(replace_blanks(text="word __1__ word",
                                        missing_words=["missing"]),
                         -1)

        self.assertEqual(replace_blanks(text="a __1__ b __2__ c __3__ d __4__",
                                        missing_words=["word1", "word2", "word3", "word4"],
                                        all=True),
                         "a word1 b word2 c word3 d word4")

        self.assertEqual(replace_blanks(text="word __2__ word",
                                        missing_words=["word", "missing"],
                                        num_correct_answers=2),
                         "word missing word")

    def test_intro_msg(self):
        self.assertEqual(intro_msg(levels_played=0,
                                   current_level=1,
                                   attempts=0),
                         "\nGreat, you've chosen to start on level 1.\nHere is you first challenge: ")
        self.assertEqual(intro_msg(levels_played=1,
                                   current_level=1,
                                   attempts=0),
                         "\nYou want more, huh! Here's your next challenge: ")
        self.assertEqual(intro_msg(levels_played=1,
                                   current_level=1,
                                   attempts=1),
                         "\nGreat, lets try again")

    def test_string_w_new_line(self):
        # Will fail if LEVEL_2_TEXT_W_BLANKS IS CHANGED
        self.assertEqual(string_w_new_line(string=LEVEL_2_TEXT_W_BLANKS), "Python features a __1__ type system and automatic __2__ management \nand supports multiple __3__ paradigms, including object-oriented, imperative, __4__ programming, \nand procedural styles. It has a large and comprehensive standard \n__5__. ")

    def test_str_level_list(self):
        # Will fail if NUMBER_LEVELS != 3
        self.assertEqual(str_level_list(), ['1', '2', '3'])

"""
if __name__ == '__main__':
    unittest.main()
"""

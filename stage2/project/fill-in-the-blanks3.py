import types
import sys

NUMBER_LEVELS = 3
MAX_ERRORS = 5
LEVEL_1_TEXT_W_BLANKS = "Python is a widely used high-level programming __1__ for general-purpose __2__, created by Guido van Rossum and first released in 1991. An interpreted language, Python has a design philosophy which emphasizes code __3__ (notably using __4__ indentation to delimit code blocks rather than curly braces or keywords), and a syntax which allows programmers to express concepts in __5__ lines of code than possible in languages such as C++ or Java."
LEVEL_2_TEXT_W_BLANKS = "Python features a __1__ type system and automatic __2__ management and supports multiple __3__ paradigms, including object-oriented, imperative, __4__ programming, and procedural styles. It has a large and comprehensive standard __5__."
LEVEL_3_TEXT_W_BLANKS = "Python __1__ are available for many operating __2__, allowing __3__ code to run on a wide variety of systems. CPython, the reference __4__ of Python, is __5__ source software and has a community-based __6__ model, as do nearly all of its variant implementations. CPython is managed by the non-profit Python Software Foundation."
LEVEL_1_MISSING_WORDS = ["language", "programming", "readability", "whitespace", "fewer"]
LEVEL_2_MISSING_WORDS = ["dynamic", "memory", "programming", "functional", "library"]
LEVEL_3_MISSING_WORDS = ["interpreters", "systems", "Python", "implementation", "open", "development"]

def main():
    levels_played = 0
    attempts = 0
    print "Welcome to my version of the madlibs game."
    print "Try to figure out what words should fill the blanks."

    current_level = choose_level()

    while current_level <= NUMBER_LEVELS:

        # Print intro message
        intro_msg(levels_played=levels_played, current_level=current_level, attempts=attempts)
        # get text and stuff for current_level
        text, corrected_text, missing_words = get_level_text(level=current_level)
        # play Level
        level_outcome = play_level(text=text, corrected_text=corrected_text, missing_words=missing_words)
        1
        if level_outcome[0] == -1:
            print ""
            print "D*mn*t, you failed..."
            again = raw_input("Do you want to try again? Type 'yes' or 'no'.") #TODO VALIDATE INPUT
            if again == 'yes':
                attempts += 1
            else:
                print ""
                print "Ok, sorry to see you go. Come back soon. BTW, the correct answer was:"
                string_w_new_line(level_outcome[1])
                sys.exit()
        elif level_outcome[0] == 1:
            levels_played += 1
            print "Great work!!"
            if current_level < NUMBER_LEVELS:
                print ""
                next = raw_input("Want to play the next level? Type 'yes' or 'no'.") #TODO VALIDATE INPUT
                if next == 'yes':
                    current_level += 1
                    attempts = 0
                elif next == 'no':
                    print "Ok, come back soon."
                    sys.exit()
            else:
                print ""
                start_over = raw_input("I need to add some more levels!! Want to start over? Type 'yes' or 'no'.") #TODO VALIDATE INPUT
                if start_over == 'yes':
                    current_level = 0
                    attempts = 0
                    levels_played = 0




#
def play_level(text, corrected_text, missing_words):
    # input: Text with blanks, corrected text with filled blanks, missing words list
    # output:
    #       failed to complete each word in less than MAX_ERROR tries --> -1, correct_text
    #       Completed each word in less than MAX_ERROR tries --> 1, correct_text
    correct_answers = 0
    while text != corrected_text:
        print ""
        string_w_new_line(text)
        print ""
        print "What do you think fits in the blank with placeholder: __" + str(correct_answers+1) + "__"
        answer = raw_input("Your answer:")
        tries = 0
        while answer != missing_words[correct_answers]:
            tries += 1 # increment tries for each loop where answer is wrong
            print ""
            string_w_new_line(text)
            print ""
            print "Oops, that was incorrect. Try again. You have " + str(MAX_ERRORS - tries) + " tries left."
            print "What do you think fits in the blank with placeholder: __" + str(correct_answers + 1) + "__"
            answer = raw_input("Your answer:")
            if tries >= MAX_ERRORS:
                return -1, corrected_text
        correct_answers += 1 # increment on correct answer
        text = replace_blanks(text=text, num_correct_answers=correct_answers, missing_words=missing_words)
    return 1, corrected_text


def choose_level():
    # input: none
    # output: valid level, int
    # Error, if user fails more than 3 times exit game with snooty error msg
    level = None
    tries = 0
    while level not in [1, 2, 3]:
        if tries > 0 and tries < 3:
            print ""
            print "Oops, invalid input, try again."
        elif tries >= 3:
            sys.exit("You suck at following instructions ;-). The game will now exit.")
        level = validate_level(raw_input("What level would you like to start from? Choose level 1, 2 or 3:"))
        tries += 1
    return level

def validate_level(choosen_level):
    # input raw input STR
    # output : level as int or -1 for error
    if choosen_level in ['1','2','3']:
        return int(choosen_level)
    else:
        return -1

def get_level_text(level):
    # input: Int repr. of level
    # output: Tuple: text with blanks, correct_text, list of missing words
    # ERROR = -1, -1, -1
    if level == 1:
        correct_text = replace_blanks(text=LEVEL_1_TEXT_W_BLANKS, missing_words=LEVEL_1_MISSING_WORDS, all=True) #TODO
        return LEVEL_1_TEXT_W_BLANKS, correct_text, LEVEL_1_MISSING_WORDS
    elif level == 2:
        correct_text = replace_blanks(text=LEVEL_2_TEXT_W_BLANKS, missing_words=LEVEL_2_MISSING_WORDS, all=True)  # TODO
        return LEVEL_2_TEXT_W_BLANKS, correct_text, LEVEL_2_MISSING_WORDS
    elif level == 3:
        correct_text = replace_blanks(text=LEVEL_3_TEXT_W_BLANKS, missing_words=LEVEL_3_MISSING_WORDS, all=True)  # TODO
        return LEVEL_3_TEXT_W_BLANKS, correct_text, LEVEL_3_MISSING_WORDS
    else:
        return -1, -1, -1

def replace_blanks(text, missing_words, num_correct_answers=0, all=False):
    # input: text with blanks, list of missing words, number of correct answers(default=0) int, all(default=false) if true will replace all missing words bool
    #   num_correct_answers cannot assume value 0 if all = false and vice versa, returns error
    # output text with correct words placed in blanks
    # error = -1
    if not isinstance(text, types.StringType)\
            or not isinstance(missing_words, types.ListType)\
            or not isinstance(num_correct_answers, types.IntType)\
            or not isinstance(all, types.BooleanType):
        return -1
    elif num_correct_answers == 0 and all is False:
        return -1

    if all:
        i = 0
        while i < len(missing_words):
            # construct place_holder
            placeholder = "__" + str(i+1) + "__"
            text = text.replace(placeholder, missing_words[i])
            i += 1
        return text
    else:
        placeholder = "__" + str(num_correct_answers) + "__"
        return text.replace(placeholder, missing_words[num_correct_answers-1])

def intro_msg(levels_played, current_level, attempts):
    # Prints appropriate message depending on where in game user is
    # 3 possible outcomes, all cases should be covered given that inputs are INTs
    if levels_played == 0 and attempts == 0:
        print ""
        print "Great, you've chosen to start on level " + str(current_level) + "."
        print "Here is you first challenge: "
    elif levels_played > 0 and attempts == 0:
        print ""
        print "You want more, huh! Here's your next challenge: "
    else:
        print ""
        print "Great, lets try again."

def string_w_new_line(string):
    # Input string
    # Prints string with 10 words per line for readability
    text_with_line_break = ""
    words_per_line = 10
    word_list = string.split()
    i = 0
    i_w = 1
    for word in word_list:
        if i_w < len(word_list):
            text_with_line_break += word + " "
        else:
            text_with_line_break += word
        i += 1
        if i == words_per_line:
            text_with_line_break += "\n"
            i = 0

    print text_with_line_break


main()


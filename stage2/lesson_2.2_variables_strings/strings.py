# Lesson 2.2: Strings

# Strings are sequences of characters that are enclosed in quotes.
# We can enclose them with single or double quotes and assign them
# to variables. We can even combine strings by adding them (we call
# this concatenation).

# https://classroom.udacity.com/nanodegrees/nd000/parts/0001345403/modules/356813882475460/lessons/4192698630/concepts/49819819440923

print 'Hello'
print "Hello"

hello = "Howdy"
print hello

# Add your own code and notes here
def process_madlib(mad_lib):
    processed = ""
    # your code here
    # you may find the built-in len function useful for this quiz
    # documentation: https://docs.python.org/2/library/functions.html#len
    str_len = len(mad_lib)
    current_pos = 0
    next_space_pos = mad_lib.find(' ')
    while next_space_pos != -1:
        word = mad_lib[current_pos:next_space_pos].replace(' ','')
        word_to_add = word_transformer(word)
        if word_to_add == word[0]:
            processed = processed + word+' '
        else:
            processed = processed + word_to_add+' '
        current_pos = next_space_pos
        next_space_pos = mad_lib.find(' ', current_pos + 1)
    #add last word
    processed = processed + mad_lib[current_pos:].replace(' ','')
    return processed


def process_madlib(mad_lib):
    processed = ''
    box_length = 4
    str_len = len(mad_lib)
    position = 0

    while position <= str_len:
        box = mad_lib[position:box_length]
        to_add = word_transformer(box)
        if len(to_add) == 1:
            processed = processed + to_add
            position = position + 1
        elif len(to_add) > 1:
            processed = processed + to_add
            position = position + box_length
    return processed
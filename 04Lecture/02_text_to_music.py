# Reference: https://www.youtube.com/watch?v=9Lk4gBBWMqw

from scamp import *

# create a new session with drums
s = Session()
drums = s.new_part("drums")

# create some text
text = """The Simpsons The Simpsons a meadow and they live a lot live live live live a lot (school bell rings) The Simpsons a meadow and they live a lot (work bell rings) The Simpsons a meadow and da da da da (sound makes a sound and hooter hooter)"""

# code to read a text file with the entire lyrics
# with open('data/simpsons_theme.txt') as f:
  #  text = f.read()

# for each character in the text do the following
for char in text:
    # if the character is a blank space then play nothing
    if char == " ":
        wait(0.4)
    # if the character is alpha numeric adjust the pitch according to an alpha numeric value of the integer
    elif char.isalnum():
        print(ord(char))
        drums.play_note(ord(char) - 20, 0.8, 0.06)
        # subtract 20 as high for a midi note
    else:
    # for all other characters, create some space
        wait(0.2)
        drums.play_note(ord(char), 0.8, 0.06)
        wait(0.2)
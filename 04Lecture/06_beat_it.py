# Reference: https://www.youtube.com/watch?v=WhNLNvugNy0
from scamp import *

s = Session()

brass = s.new_part("brass")

def beat_it():
    brass.play_note(40, 1.0, 0.25)
    brass.play_note(43, 1.0, 0.25)
    brass.play_note(47, 1.0, 0.25)
    brass.play_note(55, 1.0, 0.25)
    brass.play_note(52, 1.0, 0.75)
    brass.play_note(54, 1.0, 0.5)
    brass.play_note(52, 1.0, 0.25)
    brass.play_note(50, 1.0, 0.25)
    wait(0.25)
    brass.play_note(50, 1.0, 0.25)
    wait(0.75)

def top_part():
    trumpet.play_note(71, 1.0, 0.25)
    trumpet.play_note(71, 1.0, 1.75)
    trumpet.play_note(71, 1.0, 0.25)
    trumpet.play_note(71, 1.0, 1.5)
    trumpet.play_note(71, 1.0, 0.5)
    trumpet.play_note(71, 1.0, 0.25)
    trumpet.play_note(71, 1.0, 0.25)
    trumpet.play_note(71, 1.0, 0.25)
    trumpet.play_note(74, 1.0, 0.5)
    trumpet.play_note(71, 1.0, 0.25, "staccato")
    trumpet.play_note(74, 1.0, 0.5)
    trumpet.play_note(71, 1.0, 0.25, "stacatto")


# play once
# beat_it()
# add a low note
# brass.play_note(40, 1.0, 0.25)
# play again
# beat_it()

# play the functions for trumpet part and brass together
trumpet = s.new_part("trumpet")
# but aah, this will be sequential and we want to play them at the same time

# can use the function fork, and writing code to fork our function
# if you want to pass in parameters to your function you need to use the arg function. Check our the reference video.

# s.fork(beat_it)
# top_part()

# since the trumpet part is longer it plays on it's own
# reversing the fork order also doesnt sound quite right, so we can fork both functions
s.fork(top_part)
s.fork(beat_it)
# to keep script alive add this
# s.wait_forever()
s.wait_for_children_to_finish()


# Reference
# https://www.youtube.com/watch?v=xwxt32ollv0
# http://scamp.marcevanstein.com/

from scamp import *
from random import random, choice

# create session object
s = Session()

# code to get the default sound presets
# s.print_default_soundfont_presets()

# let's create a cello again
cello = s.new_part("cello")

# we could also add a while statement if we want to continuously loop over

loop_number = 1

while True:
    print(loop_number)
    cello.play_note(60, 0.8, 2)
    cello.play_note(78, 0.5, 0.5)
    # ext the loop after it reaches a certain number of loops
    if loop_number == 1:
        break
    # you could also add this condition in your while loop statement
    loop_number += 1

# you could also loop through play_note and adjust the pitch
print("----")
for pitch in range(65, 72):
# that sounds awful, we could see if we could make this better by specifying a list of pitches
# for pitch in [60, 64, 66, 69]:
    print(pitch)
    # this will loop through all values in the range from the min to the max - 1
    cello.play_note(pitch, 0.8, 0.25)


print("----")
# you could also define a starting pitch and duration and change the interval
interval = 1
starting_time = 0.25
starting_pitch = 72

pitch = starting_pitch
duration = starting_time

while interval < 5:
    print(pitch, duration)
    cello.play_note(pitch + interval, 0.8, duration)
    interval += 1
    pitch = pitch + interval
    duration = duration + (duration % interval)

print("----")
# we could adjust the pitch to go up and down
# to do so, we can create a definition which will wrap the pitch between a specific
def wrap_in_range(pitch, low, high):
    return (pitch - low) % (high - low) + low

cello_pitch = 48
interval = 1

while interval < 5:
    cello.play_note(cello_pitch, 0.8, 0.25)
    cello_pitch = wrap_in_range(cello_pitch + interval, 36, 60)
    interval += 1

print("----")
# can also replace a fixed volume with a defined envelope which will change the volume
# http://scamp.marcevanstein.com/expenvelope/expenvelope.envelope.Envelope.html
forte_piano = Envelope.from_levels_and_durations(
    [0.0, 0.4, 1.0], [0.2, 0.8], curve_shapes=[0, 3]
)
# code to visualise the envelope
forte_piano.show_plot()

# another musical term and use of the envelope function
dimineundo = Envelope.from_levels([0.8, 0.3])

# we can also play around with the duration
while s.time() < 30:
    # 70% of the time we will play with forte piano
    if random() < 0.7:
        cello.play_note(cello_pitch, forte_piano, choice([1.0, 1.5]))
    else:
        cello.play_note(cello_pitch, dimineundo, choice([2.0, 2.5, 3.0]))
        # add a wait function for delay
        wait(choice([1.0, 1.5]))
    cello_pitch = wrap_in_range(cello_pitch + interval, 36, 60)
    interval += 1

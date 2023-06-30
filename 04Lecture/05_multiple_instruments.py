# Reference
# https://www.youtube.com/watch?v=xwxt32ollv0
# http://scamp.marcevanstein.com/

from scamp import *

# create session object
s = Session()

# let's create a cello again
cello = s.new_part("cello")

# we could also add another instrument, apparently bass goes well
# bass = s.new_part("double bass")
bass = s.new_part("bass")

# play them one after the other
# cello.play_note(60, 0.8, 2)
# bass.play_note(80, 0.8, 1.5)
# cello.play_note(78, 0.5, 0.5)
# bass.play_note(77, 1, 2)

# play them in a loop for a set time
# while s.time() < 1:
    # cello.play_note(60, 0.8, 2)
    # bass.play_note(80, 0.8, 1.5)
    # cello.play_note(78, 0.5, 0.5)
    # bass.play_note(77, 1, 2)

print("-----")
# play two musical notes in parallel by adding the blocking = False
# cello.play_note(70, 0.5, 5.0, blocking=False)
# can also play a chord
cello.play_chord([76, 79, 84, 70], 0.5, 5.0)

# but check it out when we play multiple notes
# cello.play_note([76, 79, 84, 70], 0.5, 5.0, blocking=False)
fp_cresc = Envelope.from_levels_and_durations(
    [0.8, 0.2, 1.0], [0.1, 0.9], curve_shapes=[-5, 5]
)
# code to visualise the envelope
fp_cresc.show_plot()

cello.play_note([76, 79, 84, 70], fp_cresc, 5.0)

print("--")
# cello.play_note([76, 79, 84, 70], fp_cresc, 1, blocking=False)
# bass.play_note(80, 0.8, 1)

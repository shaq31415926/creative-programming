from scamp import *

# Create our session object.
# This session, similar to the real world, is where we record and manage our music
# ensemble
# clock
# transcriber

s = Session()
# new part in the session which plays the cello
cello = s.new_part("cello")

# we can play notes or chords, but to start with we will place a singular note

# we need to pass in "pitch", volume of the sound (0 to 1), and the duration (which is in secs if tempo is not set)
# cello.play_note(40, 1, 5)
# we could play several notes, one after the other
# cello.play_note(48, 1, 3)
# cello.play_note(76, 1, 3)

# wrap this as a for loop
pitch = [48, 58, 76]
time = 1

for p in pitch:
    cello.play_note(p, 1, time)

# to reduce the time, you could play with the time parameter or the tempo parameter
s.tempo = 120 # the default is 60 beats per minute, so this is the same as time=0.5
# however, you t does not have to be a number that perfectly divides 120 to get sweet, sweet cello music
time = 0.67

for p in pitch:
    cello.play_note(p, 1, time)

# we can also transcribe the music, but first, we need to set up LilyPond
# if you are set up, what other musical instruments work?

s.start_transcribing()
for p in pitch:
    cello.play_note(p, 1, time)
# need to call to_score() and show() to see the notes of the music
s.stop_transcribing().to_score().show()

# I am no music expert, but you can also add a "time signature" to your score
# s.start_transcribing()
# for p in pitch:
  #  cello.play_note(p, 1, time)
# s.stop_transcribing().to_score(time_signature="3/8").show()

# you can also convert this to an xml file and edit but not for now
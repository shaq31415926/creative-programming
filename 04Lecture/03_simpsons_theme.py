from scamp import *

# Create our session object .
s = Session()

# set the tempo
# s.tempo = 120

# new part in the session which plays the clarinet
clarinet = s.new_part("clarinet")

# wrap this as a for loop
pitch = [60, 64, 66, 69, 67, 64, 60, 57, 54, 54, 55]
time = 0.25

s.start_transcribing()
for p in pitch:
    clarinet.play_note(p, 1, time)
# need to call to_score() and show() to see the notes of the music
s.stop_transcribing().to_score().show()


print("----")
# we can also map a specific time duration for every pitch
pitch = [60, 64, 66, 69, 67, 64, 60, 57, 54, 54, 55]
durs_list = [1.5, 1.0, 1.0, 0.5, 1.5, 1.0, 1.0, 0.5, 0.5, 0.5, 0.5]


s.tempo = 120
s.start_transcribing()
for p, duration in zip(pitch, durs_list):
     print(p, duration)
     clarinet.play_note(p, 0.8, duration)
s.stop_transcribing().to_score().show()


# can add another option that adds a staccato or makes it shar
# check out the documentation here: http://scamp.marcevanstein.com/narrative/note_properties.html#the-note-properties-argument

s.start_transcribing()
for p, d in zip(pitch, durs_list):
     print(p, duration)
     clarinet.play_note(p, 0.8, duration, "#")
s.stop_transcribing().to_score().show()

# ANY IDEAS HOW TO COMPLETE THIS?????
# https://musescore.org/en/plugin-development/note-pitch-values
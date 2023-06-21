import moviepy.editor as mp

audio = mp.AudioFileClip("music/grr.mp3")
video1 = mp.VideoFileClip("video/example.mp4")
final = video1.set_audio(audio)

final.write_videofile("output.mp4")
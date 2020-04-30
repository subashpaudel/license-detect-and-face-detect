from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import time
print(ffmpeg_extract_subclip("video1.mp4", start_time, end_time, targetname="car.mp4"))

import ffmpy

a=ffmpeg -i 'car.mp4' -ss 00.00:02.500 -t 00:00:03.250 -c copy 'sub.mp4'
print(a)

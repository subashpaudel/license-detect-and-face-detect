import time

filename = 'C:/Users/subashpaudel/Desktop/openalpr_64/car.mp4'


def createTrainingData(filename,start,time_stop):
    vidcap = cv2.VideoCapture(filename)
    try:
        os.makedirs("trainingdata_"+filename)
    except OSError:
        pass
    os.chdir("trainingdata_"+filename)
    length = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(vidcap.get(cv2.CAP_PROP_FPS))
    for time in range(time_start,time_stop):
        vidcap.set(cv2.CAP_PROP_POS_MSEC,time*1000)
        success,image = vidcap.read()
        image = cv2.medianBlur(image,7)
        resized = imutils.resize(image, width=800)
        p1 = resized[370:430,220:300]
        p2 = resized[370:430,520:600]
        p1 = cv2.Canny(p1, 400, 100, 255)
        p2 = cv2.Canny(p2, 400, 100, 255)
        cv2.imwrite('p1_'+str(time)+".png",p1)
        cv2.imwrite('p2_'+str(time)+".png",p2)
    os.chdir("..")
    createTrainingData()



from pathlib import Path
from pytube import YouTube
import os
import cv2
import math


def getFrames(path):
    print("Getting frames")
    #path = path.replace(".", "")
    #path = "F:/VIALab/DownloadFrames" + path
    #path = "F:/Repositorios/Youtube_to_Frames" + path
    arq_name = os.listdir(path)[0]
    arq_path = (path + "/" + arq_name)
    print(arq_path.replace("/", "\\"))

    path += "/frames"
    if not os.path.exists(path):
        os.makedirs(path)


    vidcap = cv2.VideoCapture(arq_path)

    def getFrame(sec, currentframe):
        vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
        hasFrames,image = vidcap.read()
        if hasFrames:
            print("Frame " + "[" + str(currentframe) + "]")
            name = path + '/frame' + str(currentframe) + '.jpg'

            cv2.imwrite(name, image) 
            currentframe += 1
        return hasFrames

    currentframe = 0
    sec = 0
    frameRate = 5 # it will capture image in each 0.5 second
    success = getFrame(sec, currentframe)
    while success:
        currentframe += 1
        sec = sec + frameRate
        sec = round(sec, 2)
        success = getFrame(sec, currentframe)

    # Release all space and windows once done 
    cv2.destroyAllWindows() 

def downloadYouTube(video_id):
    print("Downloading the video: " + video_id)
    videourl = "https://www.youtube.com/watch?v=" + video_id
    path = "./videos/" + video_id

    yt = YouTube(videourl)
    yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists(path):
        os.makedirs(path)
    yt.download(path)
    
    currentPATH = str(Path().absolute())
    #print("currentPATH: " + currentPATH)
    path = path.replace(".", "")
    #print("Path1: " + path)
    path = path.replace("/", "\\")
    #print("Path2: " + currentPATH + path)
    path = currentPATH + path

    getFrames(path)


#currentPATH = str(Path().absolute())


# The youtube ID
downloadYouTube('UNzvlXusQro')
downloadYouTube('lk6eACQdY3w')

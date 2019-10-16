from pathlib import Path
from pytube import YouTube
import os
import cv2


def getFrames(path):
    path = path.replace(".", "")
    #path = "F:/VIALab/DownloadFrames" + path
    path = "PATHATUAL" + path
    arq_name = os.listdir(path)[0]
    print("List: " + arq_name)
    cam = cv2.VideoCapture((path + "/" + arq_name)) 

    path += "/frames"
    if not os.path.exists(path):
        os.makedirs(path)
    # frame 
    currentframe = 0
    while(True): 
      
        # reading from frame 
        ret,frame = cam.read() 
    
        if ret: 
            # if video is still left continue creating images 
            name = path + '/frame' + str(currentframe) + '.jpg'
            print ('Creating...' + name) 
    
            # writing the extracted images 
            cv2.imwrite(name, frame) 
    
            # increasing counter so that it will 
            # show how many frames are created 
            currentframe += 20
        else: 
            break
    
    # Release all space and windows once done 
    cam.release() 
    cv2.destroyAllWindows() 

def downloadYouTube(video_id):
    videourl = "https://www.youtube.com/watch?v=" + video_id
    path = "./videos/" + video_id

    yt = YouTube(videourl)
    yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists(path):
        os.makedirs(path)
    yt.download(path)
    getFrames(path)


#thisPATH = str(Path().absolute())


# The youtube ID
downloadYouTube('UNzvlXusQro')

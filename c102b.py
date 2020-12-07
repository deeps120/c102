import cv2
import dropbox
import random
import time 

startTime = time.time()
def takesnapshot():
    number = random.randint(0,100)
    videocaptureobject = cv2.VideoCapture(0)
    result = True 
    
    while(result):
        ret,frame = videocaptureobject.read()
        imgName = 'img'+str(number)+'.png'
        cv2.imwrite(imgName,frame)
        startTime= time.time
        result = False 
    return imgName
    print('snapshot taken')
    videocaptureobject.release()
    cv2.destroyAllWindows()

def uploadfile(imgName):
    accessToken = ''
    file = imagecounter
    filefrom = file 
    fileto = '/newfolder/'+(imgName)
    dbx = dropbox.Dropbox(accessToken)
    
    with open(filefrom,'rb')as f:
        dbx.filesupload(f.read(),fileto,mode = dropbox.files.WriteMode.overwrite)
        print('file uploaded')
        
def main():
    while(True):
        if((time.time()-startTime)>=300):
            name = takesnapshot()
            uploadfiles(name)

main()
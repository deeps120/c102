import cv2
def takesnapshot():
    videocaptureobject = cv2.VideoCapture(0)
    result = True 
    while(result):
        ret,frame = videocaptureobject()
        print(ret)
        cv2.imwrite('newpicture1.jpg',print)
        result = False 
    videocaptureobject.release()
    cv2.destroyAllWindows() 
takesnapshot()
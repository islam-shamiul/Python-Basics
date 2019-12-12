import cv2
import numpy as np

def main():
    img=np.zeros((512,512,3),np.uint8)
    cv2.line(img,(0,100),(100,0),(255,0,10),2)
    cv2.circle(img,(50,200),20,(255,25,100),-1)
    cv2.rectangle(img,(100,200),(200,300),(255,100,150),-1)
    pints=np.array([[200,300],[250,400],[200,150],[350,500],[400,200]])
    cv2.polylines(img,[pints],True,(255.250,0))
    text='test Text'
    cv2.putText(img,text,(100,300),cv2.FONT_HERSHEY_DUPLEX,2,(255,20,20))
    cv2.imshow('lena',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()
import cv2

def main():
    path="D:\\ImageProcessing\\DataSets\\4.2.05.tiff"
    img=cv2.imread(path,1)
    outpath="D:\\ImageProcessing\\output\\4.2.05.jpg"
    
    cv2.imshow('Lena',img)                                      
    cv2.imwrite(outpath,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__=="__main__":
    main()
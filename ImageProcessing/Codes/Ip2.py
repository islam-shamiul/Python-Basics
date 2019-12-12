import cv2

def main():
    path="D:\\ImageProcessing\\DataSets\\lena_color_512.tif"
    img=cv2.imread(path,0)
   
    print(img.dtype)
    print(img.shape)
    print(img.ndim)
    #cv2.imshow('Lena',img)                                      
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
if __name__=="__main__":
    main()
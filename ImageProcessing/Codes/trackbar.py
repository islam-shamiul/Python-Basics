import cv2
import numpy as np


def emptyFunc():
    pass


def main():
    img = np.zeros((512, 512, 3), np.uint8)
    windowname = 'opencv BGR Color palette'
    cv2.namedWindow(windowname)
    cv2.createTrackbar('B', windowname, 0, 255, emptyFunc)
    cv2.createTrackbar('G', windowname, 0, 255, emptyFunc)
    cv2.createTrackbar('R', windowname, 0, 255, emptyFunc)

    while(True):
        cv2.imshow(windowname, img)
        blue = cv2.getTrackbarPos('B', windowname)
        green = cv2.getTrackbarPos('G', windowname)
        red = cv2.getTrackbarPos('R', windowname)
        img[:] = [blue, red, green]
        print(blue, green, red)
        if cv2.waitKey(1) == 27:
            break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()

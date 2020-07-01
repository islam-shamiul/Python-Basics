import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
windowName = 'Drawing'
cv2.namedWindow(windowName)

Drawing = False
mode = True
(ix, iy) = (-1, -1)


def draw_shape(event, x, y, flags, pram):
    global Drawing, mode, ix, iy
    if event == cv2.EVENT_LBUTTONDOWN:
        Drawing = True
        (ix, iy) = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if Drawing == True:
            if mode == True:
                cv2.rectangle(img, (ix, iy), (x, y), (20.240, 52), -1)

            else:
                cv2.circle(img, (x, y), 10, (20, 255, 30), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        Drawing = False
        if mode == True:
            cv2.rectangle(img, (ix, iy), (x, y), (20.240, 52), -1)
        else:
            cv2.circle(img, (x, y), 10, (20, 255, 30), -1)


cv2.setMouseCallback(windowName, draw_shape)


def main():

    while(True):
        global mode
        cv2.imshow(windowName, img)
        k = cv2.waitKey(50)
        if k == ord('m') or k == ord('M'):
            mode = not mode
        elif k == 27:
            break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()

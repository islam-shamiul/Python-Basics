import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
windowName = 'Drawing'
cv2.namedWindow(windowName)


def draw_circle(event, x, y, flags, pram):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 40, (255, 10, 20), -1)
    if event == cv2.EVENT_RBUTTONDBLCLK:
        cv2.circle(img, (x, y), 30, (20, 255, 30), -1)
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 30, (20, 25, 250), -1)


cv2.setMouseCallback(windowName, draw_circle)


def main():

    while(True):
        cv2.imshow(windowName, img)
        if cv2.waitKey(1) == 27:
            break
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()

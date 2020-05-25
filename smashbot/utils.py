import time

import cv2
import mss
import numpy


def SmashRecord():
    with mss.mss() as sct:
        # Part of the screen to capture
        monitor = {"top": 440, "left": 375, "width": 1150, "height": 960}

    while "Screen capturing":
        last_time = time.time()

        # Get raw pixels from the screen, save it to a Numpy array
        img = numpy.array(sct.grab(monitor))

        img = cv2.resize(img, (480, 270))

        print("fps: {}".format(1 / (time.time() - last_time)))

        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break

        return img

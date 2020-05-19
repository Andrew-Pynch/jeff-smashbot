import time
import cv2
import numpy as np
import pyautogui
from utils.DataCollection import DataCollection


# def record():
#     while True:
#         dc = DataCollection()
#         screen = dc.GrabScreen(region=(400, 40, 1500, 1000))
#         last_time = time.time()

#         # Resize to something a little smaller for now
#         screen = cv2.resize(screen, (480, 270))

#         cv2.imshow('view', screen)

#         if cv2.waitKey(25) & 0xFF == ord('q'):
#             cv2.destroyAllWindows()
#             break


if __name__ == '__main__':
    dc = DataCollection()
    dc.Record(region=(400, 40, 1500, 1000))

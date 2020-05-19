import sys
import os
import time
from collections import Counter
import cv2
import numpy as np
import win32gui
import win32ui
import win32con
import win32api


class DataCollection:
    def __init__(self):
        pass

    def GrabScreen(self, region=None):
        hwin = win32gui.GetDesktopWindow()

        if region:
            left, top, x2, y2 = region
            width = x2 - left + 1
            height = y2 - top + 1
        else:
            width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
            height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
            left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
            top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)

        hwindc = win32gui.GetWindowDC(hwin)
        srcdc = win32ui.CreateDCFromHandle(hwindc)
        memdc = srcdc.CreateCompatibleDC()
        bmp = win32ui.CreateBitmap()
        bmp.CreateCompatibleBitmap(srcdc, width, height)
        memdc.SelectObject(bmp)
        memdc.BitBlt((0, 0), (width, height), srcdc,
                     (left, top), win32con.SRCCOPY)

        signedIntsArray = bmp.GetBitmapBits(True)
        img = np.fromstring(signedIntsArray, dtype='uint8')
        img.shape = (height, width, 4)

        srcdc.DeleteDC()
        memdc.DeleteDC()
        win32gui.ReleaseDC(hwin, hwindc)
        win32gui.DeleteObject(bmp.GetHandle())

        return img

    def Record(self, region=None):
        while True:
            dc = DataCollection()
            screen = dc.GrabScreen(region=region)
            last_time = time.time()

            # Resize to something a little smaller for now
            screen = cv2.resize(screen, (480, 270))

            cv2.imshow('view', screen)

            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break

    def GetKeys():
        keyList = ["\b"]
        for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ 123456789,.'£$/\\":
            keyList.append(char)

        def KeyCheck():
            keys = []
            for key in keyList:
                if wapi.GetAsyncKeyState(ord(key)):
                    keys.append(key)
            return keys

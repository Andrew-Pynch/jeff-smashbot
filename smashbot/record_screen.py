import time

import cv2
import mss
import numpy

from utils import SmashRecord


def main():
    while True:
        img = SmashRecord()
        cv2.imshow('game window', img)


if __name__ == "__main__":
    main()

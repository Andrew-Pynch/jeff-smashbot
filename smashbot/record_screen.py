import time
import cv2
import numpy as np
from scalary import DataCollection


if __name__ == '__main__':
    dc = DataCollection()
    dc.Record(region=(400, 40, 1500, 1000), resize=(480, 270))

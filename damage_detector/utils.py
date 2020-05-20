import sys
import cv2
import numpy as np
import scalary

FONT = cv2.FONT_HERSHEY_SIMPLEX


def DrawText(frame, text, show_text, side):
    if (show_text):
        frame = cv2.putText(
            frame,
            text,
            if (side == 'r'):
                (400, 75),
            (255, 0, 0),
            2,
            cv2.LINE_AA
        )
    print(f'Text: {text}')

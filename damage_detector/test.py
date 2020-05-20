# insert at 1, 0 is the script path (or '' in REPL)
from scalary import DataCollection
import sys
import cv2
from fastai.vision import *
from fastai import *


def player_health():
    p1 = dc.GrabScreen(region=(520, 850, 650, 1000))
    p2 = dc.GrabScreen(region=(820, 850, 950, 1000))

    # Drop Alpha channel
    p1 = p1[:, :, :3]
    p2 = p2[:, :, :3]

    p1 = cv2.cvtColor(p1, cv2.COLOR_BGR2GRAY)
    p2 = cv2.cvtColor(p2, cv2.COLOR_BGR2GRAY)


def predict_damage():
    while True:
        learn = load_learner('models/')
        # Screen capture
        dc = DataCollection()

        p2 = dc.GrabScreen(region=(720, 850, 850, 1000))
        p2show = p2.copy()
        cv2.imshow('player 2 health', p2show)

        p2 = cv2.cvtColor(p2, cv2.COLOR_BGRA2BGR)
        p2 = pil2tensor(p2, dtype=np.uint8)
        p2 = p2.float()/255.0
        p2 = Image(p2)

        pred = learn.predict(p2)
        print(pred[0])

        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


if __name__ == '__main__':
    predict_damage()

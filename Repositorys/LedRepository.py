from Services.LedService import LedService
import time


class LedRepository:
    def __init__(self):
        self.ledServ = LedService()

    def Flow(self):
        self.ledServ.blinkSingleLed(0, [255, 255, 255], 0.05)
        self.ledServ.blinkSingleLed(1, [255, 255, 0], 0.05)
        self.ledServ.blinkSingleLed(2, [255, 0, 0], 0.05)
        self.ledServ.blinkSingleLed(3, [0, 255, 0], 0.05)
        self.ledServ.blinkSingleLed(4, [0, 0, 255], 0.05)
        self.ledServ.blinkSingleLed(5, [125, 125, 125], 0.05)
        self.ledServ.blinkSingleLed(6, [125, 125, 0], 0.05)
        self.ledServ.blinkSingleLed(7, [125, 0, 0], 0.05)

        self.ledServ.blinkSingleLed(8, [255, 255, 255], 0.05)
        self.ledServ.blinkSingleLed(9, [255, 255, 0], 0.05)
        self.ledServ.blinkSingleLed(10, [255, 0, 0], 0.05)
        self.ledServ.blinkSingleLed(11, [0, 255, 0], 0.05)
        self.ledServ.blinkSingleLed(12, [0, 0, 255], 0.05)
        self.ledServ.blinkSingleLed(13, [125, 125, 125], 0.05)
        self.ledServ.blinkSingleLed(14, [125, 125, 0], 0.05)
        self.ledServ.blinkSingleLed(15, [125, 0, 0], 0.05)

from Services.LedService import LedService
import time
import math


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
        
        self.ledServ.blinkSingleLed(16, [255, 255, 255], 0.05)
        self.ledServ.blinkSingleLed(17, [255, 255, 0], 0.05)
        self.ledServ.blinkSingleLed(18, [255, 0, 0], 0.05)
        self.ledServ.blinkSingleLed(19, [0, 255, 0], 0.05)
        self.ledServ.blinkSingleLed(20, [0, 0, 255], 0.05)
        self.ledServ.blinkSingleLed(21, [125, 125, 125], 0.05)
        self.ledServ.blinkSingleLed(22, [125, 125, 0], 0.05)
        self.ledServ.blinkSingleLed(23, [125, 0, 0], 0.05)
        
        self.ledServ.blinkSingleLed(24, [255, 255, 255], 0.05)
        self.ledServ.blinkSingleLed(25, [255, 255, 0], 0.05)
        self.ledServ.blinkSingleLed(26, [255, 0, 0], 0.05)
        self.ledServ.blinkSingleLed(27, [0, 255, 0], 0.05)
        self.ledServ.blinkSingleLed(28, [0, 0, 255], 0.05)
        self.ledServ.blinkSingleLed(29, [125, 125, 125], 0.05)
        self.ledServ.blinkSingleLed(30, [125, 125, 0], 0.05)
        self.ledServ.blinkSingleLed(31, [125, 0, 0], 0.05)

    def Rainbow(self, number_leds, blink_length):
        for i in range(number_leds):
            light = math.ceil(i*2.5)
            self.ledServ.blinkSingleLed(i, [255-light, 255-light, 255-light], blink_length)


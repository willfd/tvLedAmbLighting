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
        colors = [[255, 0, 0], [255, 125, 0], [255, 255, 0], [125, 255, 0], [0, 255, 0], [0, 255, 125], [0, 255, 255], [0, 125, 255], [0, 0, 255], [125, 0, 255], [255, 0, 255], [255, 0, 125]]
        for i in range(number_leds):
            c = i
            if c >= len(colors):
                print(f"c is over {len(colors)} c: {c}")
                c = c % len(colors)
                print(c)
            color = colors[c]
            self.ledServ.blinkSingleLed(i, [color[0], color[1], color[2]], blink_length)
            
    def Check(self, number_led, blink_length):
            self.ledServ.blinkSingleLed(number_led, [0, 0, 255], blink_length)

import neopixel
import board
import time


class LedService:
    def __init__(self):
        number_of_pixels = 300
        pi_pin = board.D18
        self.pixels = neopixel.NeoPixel(pi_pin, number_of_pixels)

    def lightSingleLed(self, led_number, colour: [int, int, int]):
        r = colour[0]
        g = colour[1]
        b = colour[2]
        self.pixels[led_number] = (r, g, b)
        print(f"light {led_number} lit")
    
    def turnOffSingleLed(self, led_number):
        self.pixels[led_number] = (0, 0, 0)
        
    def blinkSingleLed(self, led_number, colour: [int, int, int], blink_length):
        r = colour[0]
        g = colour[1]
        b = colour[2]
        self.pixels[led_number] = (r, g, b)
        print(f"light {led_number} lit")
        time.sleep(blink_length)
        self.turnOffSingleLed(led_number)

    def lightAllLed(self, colour: [int, int, int]):
        r = colour[0]
        g = colour[1]
        b = colour[2]
        self.pixels.fill((r, g, b))

    def turnOffAllLed(self):
        self.pixels.fill((0, 0, 0))

    def show(self):
        self.pixels.show()

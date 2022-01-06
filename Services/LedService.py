import neopixel
import board


class LedService:
    def __init__(self):
        # led_freq = 800000
        number_of_pixels = 300
        pi_pin = board.D18
        self.pixels = neopixel.NeoPixel(pi_pin, number_of_pixels)

    def lightSingleLed(self, led_number, colour: [int, int, int]):
        r = colour[0]
        g = colour[1]
        b = colour[2]
        self.pixels[led_number] = (r, g, b)
        print(f"light {led_number} lit")

    def lightAllLed(self, colour: [int, int, int]):
        r = colour[0]
        g = colour[1]
        b = colour[2]
        self.pixels.fill((r, g, b))

    def show(self):
        self.pixels.show()

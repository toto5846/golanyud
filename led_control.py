import neopixel
from machine import Pin

# Define LED colors
COLORS = [
    (255, 20, 147),  # HOT_PINK
    (0, 255, 255),   # AQUA
    (0, 255, 0),     # LIME
    (238, 130, 238), # VIOLET
    (255, 165, 0)    # ORANGE
]

class LEDControl:
    def __init__(self, pin, num_leds):
        self.num_leds = num_leds
        self.np = neopixel.NeoPixel(Pin(pin, Pin.OUT), num_leds)
        self.current_led = 0

    def moving_colors(self):
        """Cycles through colors for a moving effect."""
        for i in range(self.num_leds):
            color_idx = (self.current_led + i) % len(COLORS)
            self.np[i] = COLORS[color_idx]
        self.np.write()
        self.current_led = (self.current_led + 1) % self.num_leds

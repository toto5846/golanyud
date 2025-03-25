from machine import Pin, SPI
from GolanDisplay import GolanDisplay

def init_display():
    """Initializes and returns the display object."""
    spi = SPI(1, baudrate=33000000, sck=Pin(18), mosi=Pin(23), miso=Pin(19))
    cs = Pin(5)
    dc = Pin(25)
    rst = Pin(33)
    return GolanDisplay(spi, cs, dc, rst)

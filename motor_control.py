import time
from machine import Pin, PWM
import neopixel

# צבעים
COLOR_OFF = (0, 255, 0)  # ירוק - כשהמנוע לא פועל
COLOR_ON = (255, 0, 0)   # אדום - כשהמנוע פועל

class SimpleMotor:
    def __init__(self, in1_pin, in2_pin, led_pin, buzzer_pin=21, neopixel_pin=22, num_leds=4):
        self.in1 = PWM(Pin(in1_pin), freq=1000, duty=0)
        self.in2 = PWM(Pin(in2_pin), freq=1000, duty=0)
        self.led = Pin(led_pin, Pin.OUT)
        self.buzzer = PWM(Pin(buzzer_pin), freq=2000, duty=0)

        # הגדרת נאופיקסל
        self.np = neopixel.NeoPixel(Pin(neopixel_pin, Pin.OUT), num_leds)
        self.num_leds = num_leds
        self.set_np_color(COLOR_OFF)

    def set_np_color(self, color):
        for i in range(self.num_leds):
            self.np[i] = color
        self.np.write()

    def motgo(self, speed):
        """Controls motor direction and speed."""
        if speed > 0:
            self.in1.duty(1000)
            self.in2.duty(0)
        elif speed < 0:
            self.in1.duty(0)
            self.in2.duty(1000)
        else:
            self.in1.duty(0)
            self.in2.duty(0)

    def move_for_time(self, speed, duration, light_hold_time=2):
        """Moves the motor for a specified duration, and keeps red light on longer."""
        self.led.value(1)
        self.set_np_color(COLOR_ON)  # מפעיל אור אדום כשהמנוע עובד
        self.buzzer.duty(512)        # מפעיל באזר
        try:
            self.motgo(speed)
            time.sleep(duration)
        finally:
            self.motgo(0)            # עוצר מנוע
            self.buzzer.duty(0)      # מכבה באזר מיד
            self.led.value(0)



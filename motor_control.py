import time
from machine import Pin, PWM

class SimpleMotor:
    def __init__(self, in1_pin, in2_pin, led_pin, buzzer_pin=21):
        self.in1 = PWM(Pin(in1_pin), freq=1000, duty=0)
        self.in2 = PWM(Pin(in2_pin), freq=500, duty=0)
        self.led = Pin(led_pin, Pin.OUT)
        self.buzzer = PWM(Pin(buzzer_pin), freq=2000, duty=0)  # בזר מחובר לפין 21

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

    def move_for_time(self, speed, duration):
        """Moves the motor for a specified duration."""
        self.led.value(1)
        self.buzzer.duty(512)  # הפעלת הבאזר כשהלד נדלק
        try:
            self.motgo(speed)
            time.sleep(duration)
        finally:
            self.motgo(0)
            self.led.value(0)
            self.buzzer.duty(0)  # כיבוי הבאזר כשהלד נכבה

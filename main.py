from machine import Pin, PWM, ADC

led = machine.Pin(14, Pin.OUT)
led2 = machine.Pin(13)

fan = machine.Pin(20)
fan_pwm = PWM(fan)
led_pwm = PWM(led)
led_pwm2 = PWM(led2)
duty_step = 129

frequency = 5000
fan_pwm.freq(frequency)
led_pwm.freq(frequency)

pot = ADC(Pin(26))
led = machine.Pin(14, Pin.OUT)
led2 = machine.Pin(13, Pin.OUT)
led3 = machine.Pin(11, Pin.OUT)

while True:
    pot_value = pot.read_u16()
    fan_pwm.duty_u16(pot_value)
    if pot_value < 4000:
        led.value(0)
        led2.value(0)
        led3.value(0)
    elif pot_value < 50000:
        led.value(1)
        led2.value(0)
        led3.value(0)
    elif pot_value < 60000:
        led.value(1)
        led2.value(1)
        led3.value(0)
    elif pot_value > 60000:
        led.value(1)
        led2.value(1)
        led3.value(1)

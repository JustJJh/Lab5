from hal import hal_adc as adc
from hal import hal_servo as servo


def main():
    global spi
    spi=spidev.SpiDev() #create SPI object
    spi.open(0,0)

    GPIO.setmode(GPIO.BCM)  # choose BCM mode
    GPIO.setwarnings(False)
    GPIO.setup(26, GPIO.OUT)  # set GPIO 26 as output

    adc.get_adc_value()
    servo.set_servo_position()
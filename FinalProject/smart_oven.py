from fhict_cb_01.custom_telemetrix import CustomTelemetrix
import time

board = CustomTelemetrix()

GREEN_LED = 5
RED_LED = 4
# DHT_PIN = 12
BUZZER = 3
REGULAR_PIZZA = 15 
THIN_CRUST_PIZZA = 5 

def setup():
    board.displayOn()
    board.set_pin_mode_digital_output(GREEN_LED)
    board.set_pin_mode_digital_output(RED_LED)
    board.set_pin_mode_analog_output(BUZZER)

def pizza_in(cooking_time):
    board.digital_write(RED_LED, 1)
    board.digital_write(GREEN_LED, 0)
    count_down_timer(cooking_time)

def count_down_timer(count_from_time):
    counter = count_from_time
    while counter != -1:
        time.sleep(1)
        board.displayShow(counter)
        print(counter)
        counter -= 1
    pizza_done()

def pizza_done():
    board.digital_write(GREEN_LED, 1)
    board.digital_write(RED_LED, 0)

pizza_in(THIN_CRUST_PIZZA)
pizza_in(REGULAR_PIZZA)
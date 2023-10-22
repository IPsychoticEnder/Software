from fhict_cb_01.custom_telemetrix import CustomTelemetrix
import time

board = CustomTelemetrix()


LDR_PIN = 2



def callback_ldr(data):
    sensor_value = data[2]
    resistance_sensor = (1023-sensor_value)*10/sensor_value
    print(
        f"The resistance of the light sensor is: {resistance_sensor:.1f} KOhm")

    klux = 325 * pow(resistance_sensor, -1.4) / 1000
    board.displayShow(klux)
    print(f"Illuminance is approximately {klux:.3f} Kilo lux")



board.set_pin_mode_analog_input(LDR_PIN, callback=callback_ldr, differential=50)

while True:
    try:
        time.sleep(0.01)
    except KeyboardInterrupt:
        break

# clean up
print("Shutting down...")
board.shutdown()

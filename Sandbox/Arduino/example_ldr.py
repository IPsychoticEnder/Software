from fhict_cb_01.custom_telemetrix import CustomTelemetrix
import time

board = CustomTelemetrix()


LDR_PIN = 2



def callback_ldr(data):
    sensor_value = data[2]
    print(sensor_value)



board.set_pin_mode_analog_input(LDR_PIN, callback=callback_ldr, differential=50)

while True:
    try:
        time.sleep(0.01)
    except KeyboardInterrupt:
        break

# clean up
print("Shutting down...")
board.shutdown()

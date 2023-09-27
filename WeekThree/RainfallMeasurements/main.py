from my_functions import rainfall_measurer


rainfall = rainfall_measurer.set_rainfall_measurements()

print("What segment would you like? ")
start = int(input("Start: "))
end = int(input("End: "))

weekly = rainfall_measurer.get_segment_average(rainfall, 1, 7)
monthly = rainfall_measurer.get_segment_average(rainfall, 1, 30)
custom = rainfall_measurer.get_segment_average(rainfall, start, end)

print(f"Weekly: {weekly}")
print(f"Monthly: {monthly}")
print(f"Custom: {custom}")
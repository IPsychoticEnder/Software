rainfall = [1.2, 2.4, 1.6, 0.2, 0.6, 3.2, 1.2, 2.6, 3.0, 1.2, 1.2, 2.4, 1.6, 0.2, 0.6, 3.2, 1.2, 2.6, 3.0, 1.2, 1.2, 2.4, 1.6, 0.2, 0.6, 3.2, 1.2, 2.6, 3.0, 1.2]

def set_rainfall_measurements():
    while True:
        print("Please enter a rainfall measurement:")
        user_input = input("> ")
        if user_input == "":
            break
        else:
            rainfall.append(float(user_input))
    return rainfall

def get_average(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum

def get_segment_average(numbers, start, end):
    sum = 0
    j = 0
    for i in range(start -1, end):
        sum += numbers[i]
        j +=1
    return sum / j
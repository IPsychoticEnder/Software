import requests, time

while True:
    user_input = input(">")
    if user_input == "n":
        break
    one = "again_one"
    two = "again_two"
    three = "again_three"

    data = {'one': one, 'two': two, 'three': three}

    time.sleep(5)
    
    response = requests.post('http://localhost:5000/receive-sample', json=data)


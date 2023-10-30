import requests, csv

def write_to_csv(humidity, temperature, light):
    with open('data/adurino_data.csv', 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([f"\n Humidity: {humidity} \n Temperature: {temperature} \n light level: {light} \n"])

def getSamples():

    response = requests.get('http://localhost:5000/get-list')
    data = response.json()

    if data == {}:
        print("No samples collected.")
        return
    temperature = data['sent_samples'][0]
    humidity = data['sent_samples'][1]
    light_level = data['sent_samples'][2]

    write_to_csv(temperature, humidity, light_level)
    print("Done...")
    


while True:
    answer = input("what to do? (y/n) ")

    if answer == "n":
        break

    getSamples()
import csv


def write_to_csv():
    with open('adurino_data.csv', 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["one", "two", "three"])

write_to_csv()
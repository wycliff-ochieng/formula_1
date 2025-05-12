import requests
import json
import csv
#from pprint import pPrint

def get_car_data():
    car_data = requests.get("https://api.openf1.org/v1/car_data?session_key=9159&speed>=315")
    result_json = json.loads(car_data.text)
    with open("data/raw/cars.csv", mode="w",newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        
        if result_json and isinstance(result_json, list):
            header = result_json[0].keys()
            csv_writer.writerow(header)
            
            for row in result_json:
                csv_writer.writerow(row.values())
    print(f"Succesffuly saved to",{"data/raw/cars.csv"})
 
get_car_data()

def get_driver():
    drivers = requests.get("https://api.openf1.org/v1/drivers?session_key=9158")

    drivers_json = json.loads(drivers.text)

    with open("data/raw/drivers.csv", mode="w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)

        if drivers_json and isinstance(drivers_json, list):
            header = drivers_json[0].keys()
            csv_writer.writerow(header)

            for row in drivers_json:
                csv_writer.writerow(row.values())

get_driver()

#print(drivers_json)


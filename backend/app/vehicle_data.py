from datetime import datetime
import csv
from typing import List
import glob
from pathlib import Path

VEHICLES = []

# get all csv file name stems from app/data folder for initial import
vehicle_ids = [ Path(file).resolve().stem for file in glob.glob("app/data/*.csv") ]
    
def load_vehicle_data(vehicle_ids : List[str]):
    for v_id in vehicle_ids:
        with open('app/data/' + v_id + '.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count > 0:
                    row = {
                        "vehicle_id" : str(v_id),
                        "timestamp" : datetime.strptime(row[0][:10] + "T" + row[0][11:], "%Y-%m-%dT%H:%M:%S.%f"),
                        "speed" : int(row[1]) if row[1] != "NULL" else "NULL",
                        "odometer" : row[2],
                        "soc" : int(row[3]),
                        "elevation" : int(row[4]),
                        "shift_state" : row[5],
                    }
                    VEHICLES.append(row)
                line_count += 1
            print(f'Processed {line_count - 1} lines.')

load_vehicle_data(vehicle_ids)
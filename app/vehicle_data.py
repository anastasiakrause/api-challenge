from datetime import datetime
import csv
from typing import List, Union

VEHICLES = []

# TODO: get to read file names from data directory directly
vehicle_ids = [
    '1bbdf62b-4e52-48c4-8703-5a844d1da912',
    '06ab31a9-b35d-4e47-8e44-9c35feb1bfae',
    'f212b271-f033-444c-a445-560511f95e9c',
]
    
def load_vehicle_data(vehicle_ids : List[str]):
    uuid = 1
    for v_id in vehicle_ids:
        with open('app/data/' + v_id + '.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count > 0:
                    row = {
                        "id" : uuid,
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
                uuid  += 1
            print(f'Processed {line_count} lines.')

load_vehicle_data(vehicle_ids)
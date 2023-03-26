import csv
import glob
from pathlib import Path

def load_vehicle_data():
    VEHICLES = []

    # get all csv file name stems from app/data folder for initial import
    vehicle_ids = [ Path(file).resolve().stem for file in glob.glob("app/data/*.csv") ]
    for v_id in vehicle_ids:
        with open('app/data/' + v_id + '.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count > 0:
                    row = {
                        "vehicle_id" : str(v_id),
                        "timestamp" : row[0][:10] + "T" + row[0][11:],
                        "speed" : int(row[1]) if row[1] != "NULL" else "NULL",
                        "odometer" : row[2],
                        "soc" : int(row[3]),
                        "elevation" : int(row[4]),
                        "shift_state" : row[5],
                    }
                    VEHICLES.append(row)
                line_count += 1
            print(f'Processed {line_count - 1} lines.')
    return VEHICLES

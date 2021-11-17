import json
import csv
from elevator import Elevator
from calls import Calls


class Building:
    def __init__(self, file_name: str):
        try:
            with open(file_name, "r") as f:
                build_dic = json.load(f)
                self.minFloor = build_dic["_minFloor"]
                self.maxFloor = build_dic["_maxFloor"]
                self.elevators = []
                for k in build_dic["_elevators"]:
                    ele = Elevator(k)
                    self.elevators.append(ele)

        except IOError as e:
            print(e)

    def my_elevators(self):
        return self.elevators


class Csv:
    def __init__(self, file_name: str):  # loud from csv
        self.calls = []
        with open(file_name, "r") as f:
            csvreader = csv.reader(f)
            for ce in csvreader:
                call = Calls(callelev=ce[0], time=ce[1], source=int(ce[2]), destention=int(ce[3]), flag=ce[4], index=ce[5])
                self.calls.append(call)

    def my_calls(self):
        return self.calls

   

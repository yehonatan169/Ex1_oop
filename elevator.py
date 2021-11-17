import math


class Elevator:

    def __init__(self, dic):
        self.id = dic["_id"]
        self.speed = dic["_speed"]
        self.minFloor = dic["_minFloor"]
        self.maxFloor = dic["_maxFloor"]
        self.closeTime = dic["_closeTime"]
        self.openTime = dic["_openTime"]
        self.startTime = dic["_startTime"]
        self.stopTime = dic["_stopTime"]
        self.elevatorsStations = [0]
        self.elevatorTimes = [0]

    def elevators_stations(self):
        return self.elevatorsStations

    def elevator_times(self):
        return self.elevatorTimes



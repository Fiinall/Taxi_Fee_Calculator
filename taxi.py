from inspect import stack
from driver import Driver

class taxi:
    def __init__(self,taxi_id,driver,vehicle,status):
        self.taxi_id = taxi_id
        self.driver = driver
        self.vehicle = vehicle
        self.status = status



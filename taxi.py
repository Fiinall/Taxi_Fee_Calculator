from inspect import stack
from driver import Driver
from vehicle import Vehicle

class Taxi(Vehicle):
    def __init__(self,brand,model,km,taxi_id,driver,vehicle,status):
        super().__init__(brand,model,km)
        self.taxi_id = taxi_id
        self.driver = driver
        self.vehicle = vehicle
        self.status = status



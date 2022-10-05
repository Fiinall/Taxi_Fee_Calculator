

import random

def random_distance():
    distance = round(random.uniform(1,50),2)
    return distance

def random_traffic():
    traffic_coefficient = round(random.uniform(1,5),2)
    round(traffic_coefficient,2)
    return  traffic_coefficient

def ETA(distance,traffic_coefficient): #estimated time of arrival
    eta = distance*traffic_coefficient
    round(eta,2)
    return eta


def random_input():
    distance = random_distance()
    traffic_coefficient = random_traffic()
    eta = round(ETA(distance,traffic_coefficient),2)
    return distance, traffic_coefficient, eta




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


class Service():

    def random_input():
        distance = random_distance()
        traffic_coefficient = random_traffic()
        eta = round(ETA(distance,traffic_coefficient),2)
        return distance, traffic_coefficient, eta

    distance,traffic_coefficient,eta = random_input()

    def fee_calculator(distance,eta):
        distance_fare = distance * 0.5
        time_fare = eta * 0.6
        base_fee = 4
        total_fee = base_fee + distance_fare + time_fare 
        print(
        f"\n\nDistance : {distance}\n"
        f"Distance Fare : {distance_fare}\n"
        f"Estimated Time of Arrical : {eta}\n"
        f"Time Fare : {time_fare}\n"
        f"Base Fee : {base_fee}\n"
        f"Total Fee = Base Fee + Distance Fare + Time Fare = £{total_fee}\n"
        )
        return total_fee
    
    total_fee = fee_calculator(distance,eta) 

    
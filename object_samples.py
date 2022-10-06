import person
import driver
import vehicle
import taxi

person1 = person.Person("Fatih","Istanbul","9323","ffatihinal")

driver1 = driver.Driver("Fatih","Istanbul","9323","ffatihinal",1,10.0,6) 

vehicle1 = vehicle.Vehicle("Mercedes","E300",0)

taxi1 = taxi.Taxi("Mercedes","E300",0,1,driver1,vehicle1,"regular")


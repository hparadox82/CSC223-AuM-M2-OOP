#Project 1: Parking Ticket Simulator
from parkedcar import PCar
from parkingmeter import PMeter
from police import Police


#Scenario A: A car has run out of minutes!

#Generating vehicle...
car_a = PCar("Mazda", "3", "White", "HJA-2382")

#Car has been parked for 113 minutes.
car_a.minspark = 113

#Parking Meter is now created:
meter_a = PMeter(mins_buy=60)

#Here comes the officer:
officer_a = Police("Jens Kidman", "33")
#Who then inspects...
officer_a.inspect_car(car_a, meter_a)
#And finds that this car is indeed over its limit:


#Scenario B: No violation here.

#Generating vehicle...
car_b = PCar("Yugo", "GVX", "Blue", "NVG-3838")

#The Yugo still has some time left.
car_b.minspark = 15

#It's parked next to another parking meter:
meter_b = PMeter(mins_buy=60)

#Another officer:
officer_b = Police("Tomas Haake", "7665")
officer_b.inspect_car(car_b, meter_b)




#Scenario B: Officer Kidman spots another car that's been here for quite some time!
car_c = PCar("Jeep", "Wrangler", "Olive", "NVR-DRTY")
car_c.minspark = 480
meter_c = PMeter(mins_buy = 60)
officer_a.inspect_car(car_c, meter_c)
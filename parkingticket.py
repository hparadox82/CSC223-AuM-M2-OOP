import math

from parkedcar import PCar
from parkingmeter import PMeter
from police import Police
class PTicket:
    BASEFINE = 25.00
    HOURLYFINE = 10.00

    def __init__(self, officer:Police, car: PCar, meter: PMeter):
        self.officer_name = officer.name
        self.officer_badge = officer.badge_num
        self.car_make = car.make
        self.car_model = car.model
        self.car_license = car.lic_no
        self.minspark = car.minspark
        self.mins_buy = meter.mins_buy
        self.fine = 0.0

    def calc_fine(self):
        if self.minspark > self.mins_buy:
            self.fine = self.BASEFINE
            minsover = self.minspark-self.mins_buy
            hrsover = math.ceil(minsover / 60)

            if hrsover > 1:
                self.fine += (hrsover-1)*self.HOURLYFINE

    def issue_tix(self):
        if self.minspark > self.mins_buy:
           self.calc_fine()

           print("\n--- PARKING VIOLATION ISSUED ---\n")
           print(f"Issuing Officer: {self.officer_name}, Badge No. {self.officer_badge}\n")
           print("--- VEHICLE INFO ---\n")
           print(f"Make: {self.car_make}\nModel: {self.car_model}\nLicense: {self.car_license}")
           print("\n--- VIOLATION DETAILS ---\n")
           print(f"Purchased Time: {self.mins_buy} minutes\nTime Parked: {self.minspark} minutes\n")
           print(f"CALCULATED FINE: ${self.fine:2f}")
           print("---------------------------------")

        else:
            print ("No parking violation observed. Moving onto next vehicle.")





from parkingmeter import PMeter
from parkingticket import PTicket
from parkedcar import PCar

class Police:
    def __init__(self, name: str, badge_num: str):
        self.name = name
        self.badge_num = badge_num

    def inspect_car(self, car: PCar, meter: PMeter):
        print (f"\nOfficer {self.name}, Badge No. {self.badge_num} is inspecting vehicle with license plate {car.lic_no}...\n")
        ticket = PTicket(officer=self, car=car, meter=meter)
        ticket.issue_tix()






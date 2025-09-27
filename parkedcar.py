class PCar:
    #Inits Parked Car object
    def __init__(self, make: str, model:str, color:str, lic_no:str):
        self.make = make
        self.model = model
        self.color = color
        self.lic_no = lic_no
        self.minspark = 60
    
    #Minutes parked getter
    @property
    def minspark(self) -> int:
        return self.minspark

    @minspark.setter
    def minspark(self, value: int):
        #Minutes parked setter w/ value checking
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Parked Minutes has to be a positive number.")
        self.minspark = value

    def __str__(self) -> str:
        #Prints Parked Car info.
        return (f"Car Information:\n"
                f"Make: {self.make}\n"
                f"Model: {self.model}\n"
                f"Color: {self.color}\n"
                f"License Number: {self.lic_no}\n"
                f"Minutes Parked: {self.minspark}\n")







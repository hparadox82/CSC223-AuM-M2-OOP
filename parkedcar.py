class PCar:
    #Inits Parked Car object
    def __init__(self, make: str, model:str, color:str, lic_no:str):
        self.make = make
        self.model = model
        self.color = color
        self.lic_no = lic_no
        self._minspark = 0
    
    #Minutes parked getter
    @property
    def minspark(self) -> int:
        return self._minspark

    @minspark.setter
    def minspark(self, value: int):
        #Minutes parked setter w/ value checking
        if not isinstance(value, int) or value < 0:
            raise ValueError("Parked Minutes has to be a positive number.")
        self._minspark = value







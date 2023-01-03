
class Build:

    def __init__(self, adress, floor):
        self.adress = adress
        self.floor = floor

    def get_adress(self):
        return self.adress

    def get_floor(self):
        return self.floor

    def __repr__(self):
        return f"adresse : {self.adress}, étage : {self.floor} "


class Building(Build):

    def __init__(self, adress, floor):
        super().__init__(adress, floor)
        self.balcony = 10

    def __repr__(self):
        return super().__repr__() + f"Nombre de balcon : {self.balcony}"

class Supermarket(Build):

    def __init__(self, adress, floor):
        super().__init__(adress, floor)
        self.ray = 5

    def __repr__(self):
        return super().__repr__() + f"Nombre de rayon : {self.ray}"

class Bank(Build):

    def __init__(self, adress, floor):
        super().__init__(adress, floor)
        self.chest = 7

    def __repr__(self):
        return super().__repr__() + f"Nombre de coffre : {self.chest}"


building1 = Building("10, Rue de GravenCity", 5)
building2 = Building("15, Rue de GravenCity", 10)
building3 = Building("10, Rue de GravenCity", 8)

supermarket1 = Supermarket("50, Rue de GravenCity", 20)
supermarket2 = Supermarket("52, Rue de GravenCity", 15)

bank1 = Bank("25, Rue de GravenCity", 7)


print(f"Immeuble : {building1}\nImmeuble : {building2}\nImmeuble : {building3}")
print(f"Supermarché : {supermarket1}\nSupermarché : {supermarket2}")
print(f"Banque : {bank1}")
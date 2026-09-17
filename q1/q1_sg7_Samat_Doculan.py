class Glassware:
    def __init__(self, material):
        self.material = material


class Beaker(Glassware):
    def __init__(self, material, volume):
        super().__init__(material)
        self.volume = volume

    def display_information(self):
        print(f"Beaker: {self.volume} mL, {self.material}")


class Tray:
    def __init__(self):
        self.beakers = [
            Beaker("Borosilicate Glass", 100),
            Beaker("Borosilicate Glass", 250),
            Beaker("Borosilicate Glass", 500),
            Beaker("Polypropylene", 100),
            Beaker("Polypropylene", 250)
        ]

    def display_beakers(self):
        for beaker in self.beakers:
            beaker.display_info()
    
    def __del__(self):
        print("Tray deleted. Its beakers are no longer accessible.")


tray = Tray()
tray.display_beakers()

del tray

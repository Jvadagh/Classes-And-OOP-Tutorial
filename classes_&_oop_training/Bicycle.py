class Bike():
    def __init__(self, Color, Type):
        print('A bike object is being created!')
        self.Color = Color
        self.Type = Type

    def printH(self):
        print('hello')


class MTB(Bike):
    def __init__(self, name, WS, FS):
        super().__init__("red", 'yo')
        self.name = name
        self.WS = WS
        self.FS = FS

    def Bike_Info(self):
        print(self.name + ' - ' + str(self.WS) +
              ' - ' + str(self.FS) + ' - ' + self.Color)


class Road(Bike):
    def __init__(self, Material, Color, Type):
        super().__init__(Color, Type)
        self.Material = Material

    def printRoad(self):
        print('this ' + self.Material + ' bicycle for race and road training ' + 'its color is ' + self.Color)

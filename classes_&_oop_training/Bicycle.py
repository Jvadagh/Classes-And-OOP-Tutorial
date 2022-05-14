class Bike():
    def __init__(self, Color, Type):
        self.Color = Color
        self.Type = Type


class MTB(Bike):
    def __init__(self, name, WS, FS):
        self.name = name
        self.WS = WS
        self.FS = FS

    def Bike_Info(self):
        print(self.name + ' - ' + str(self.WS) +
              ' - ' + str(self.FS) + ' - ' + Bike.Color)


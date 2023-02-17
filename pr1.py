class car:

    def __init__(self, color, cartype, year):
        self.color = color
        self.type = cartype
        self.year = year

    def start(self):
        print("Автомобиль заведен")

    def stop(self):
        print("Автомобиль заглушен")

    def setyear(self, year):
        self.year = year

    def settype(self, cartype):
        self.type = cartype

    def setcolor(self, color):
        self.color = color


car = car('pink', 'sedan', '1999')
car.start()
car.stop()
car.setyear(2005)
car.settype("hatchback")
car.setcolor('red')
class Car:

    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def start(self):
        print(f"Автомобиль заведен")

    def stop(self):
        print(f"Автомобиль заглушен")

    def set_color(self):
        print(f"ЦВЕТ {self.color}")

    def set_year(self):
        print(f"ГОД {self.year}")

    def set_type(self):
        print(f"ТИП {self.type}")

old = Car(color = 'blue', type = 'AWT', year = '2006')
old.start()
old.set_color()
old.set_type()
old.set_year()
old.stop()

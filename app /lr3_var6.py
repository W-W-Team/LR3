import math

class Circle:
    def __init__(self, radius):
        try:
            radius = float(radius)
            if radius <= 0:
                print("Ошибка: Радиус должен быть положительным числом больше нуля.")
                self.radius = None
            else:
                self.radius = radius
        except ValueError:
            print("Ошибка: Радиус должен быть числом.")
            self.radius = None

    @staticmethod
    def about():
        print("Программа разработана командой pr6, состоящей из 3 разработчиков:\n"
              "1 разработчик: Мухамедов \n"
              "2 разработчик: Кильмухаметов \n"
              "3 разработчик: Хайриддинов")

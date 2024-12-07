import math

class Circle:
    def __init__(self, radius):
        try:
            radius = float(radius)
            if radius <= 0:
                print("Ошибка: Радиус должен быть положительным числом больше нуля.")
                self._radius = None
            else:
                self._radius = radius
        except ValueError:
            print("Ошибка: Радиус должен быть числом.")
            self._radius = None

    @property 
    def area(self):
        if self._radius is None:
            print("Ошибка: Площадь не может быть рассчитана, так как радиус не был корректно задан.") 
            return None 
        try: 
            return math.pi * self.radius ** 2 
        except TypeError: 
            print("Ошибка: Радиус должен быть числом для вычисления площади круга.") 
            return None

    @property 
    def radius(self): 
        return self._radius

    @staticmethod
    def about():
        print("Программа разработана командой pr6, состоящей из 3 разработчиков:\n"
              "1 разработчик: Мухамедов \n"
              "2 разработчик: Кильмухаметов \n"
              "3 разработчик: Хайриддинов")

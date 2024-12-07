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

class Ball(Circle):
    def __init__(self, radius, height):
        super().__init__(radius)
        try:
            height = float(height)
            if height <= 0:
                print("Ошибка: Высота должна быть положительным числом больше нуля.")
                self._height = None
            else:
                self._height = height
        except ValueError:
            print("Ошибка: Высота должна быть числом.")
            self._height = None
            
    @staticmethod
    def about():
        print("Программа расчета объема шарового сектора, выполненая командой состоящей из трёх разработчиков:\n"
              "1 разработчик: Мухамедов \n"
              "2 разработчик: Кильмухаметов \n"
              "3 разработчик: Хайриддинов")
              
    def sector_volume(self, height=None):
        if self._radius is None:
            print("Ошибка: Объем шарового сектора не может быть рассчитан, так как радиус не был корректно задан.")
            return None
        
        if height is None:
            height = self._height
            
        if height is None:
            print("Ошибка: Высота не задана для расчета объема шарового сектора.")
            return None

        try:
            height = float(height)
            if height <= 0:
                print("Ошибка: Высота должна быть положительным числом больше нуля.")
                return None
            return 2 / 3 * math.pi * self.radius ** 2 * height
        except (ValueError, TypeError):
            print("Ошибка: Высота и радиус должны быть числами для вычисления объема шарового сектора.")
            return None

Ball.about()

while True:
    try:
        radius = input("Введите радиус шара (или 'exit' для завершения): ")
        if radius.lower() == 'exit':
            print("Программа завершена.")
            break

        height = input("Введите высоту для расчета сектора (или 'exit' для завершения): ")
        if height.lower() == 'exit':
            print("Программа завершена.")
            break

        if radius and height:
            ball = Ball(radius, height)
            sector_volume = ball.sector_volume()

            if sector_volume is not None:
                print("Объем шарового сектора:", sector_volume)
        else:
            print("Радиус и высота должны быть заданы для выполнения расчетов.")
        print('')
    except Exception as e:
        print("Произошла ошибка:", e)

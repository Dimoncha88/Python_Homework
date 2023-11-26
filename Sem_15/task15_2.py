'''
Возьмите любые 1-3 задания из прошлых домашних заданий. Добавьте к ним логирование ошибок и полезной информации. 
Также реализуйте возможность запуска из командной строки с передачей параметров. 
'''

# Возьмите код из прошлой задачи "Класс Rectangle".
# Напишите к ней тесты, используя unittest и лежать в class TestRectangle(unittest.TestCase)


import unittest
import logging

logging.basicConfig(level=logging.INFO, filename="file_task2.log", encoding="utf-8")
logger = logging.getLogger(__name__)

class NegativeValueError(ValueError):
    pass

class Rectangle:

    def __init__(self, width, height=None):
        if width <= 0:
            logger.error(f'Ширина должна быть положительной, а не {width}')
            raise NegativeValueError(f'Ширина должна быть положительной, а не {width}')
            
        self._width = width
        if height is None:
            self._height = width
        else:
            if height <= 0:
                logger.error(f'Высота должна быть положительной, а не {height}')
                raise NegativeValueError(f'Высота должна быть положительной, а не {height}')
            self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {value}')

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            raise NegativeValueError(f'Высота должна быть положительной, а не {value}')

    def perimeter(self):        
        return 2 * (self._width + self._height)

    def area(self):
        return self._width * self._height

    def __add__(self, other):
        width = self._width + other._width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self._width - other._width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

class TestRectangle(unittest.TestCase):

    def test_width(self):
        r = Rectangle(5)
        self.assertEqual(r.width, 5)

    def test_height(self):
        r = Rectangle(3, 4)
        self.assertEqual(r.height, 4)

    def test_perimeter(self):
        r = Rectangle(5)
        self.assertEqual(r.perimeter(), 20)
        logger.info(f'Ширина = {r.width}, Периметр = {r.perimeter()}')
 
    def test_area(self):
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)
        logger.info(f'Ширина = {r.width}, Высота = {r.height}, Площадь = {r.area()}')

    def test_addition(self):
        self.assertEqual(str(Rectangle(5) + Rectangle(3, 4)), str(Rectangle(8, 6)))

    def test_subtraction(self):
        self.assertEqual(str(Rectangle(10) - Rectangle(3, 4)), str(Rectangle(7, 5)))

    def test_negative_width(self):
        r = Rectangle(-5)
        self.assertEqual(r.width, NegativeValueError(f'Ширина должна быть положительной, а не {r.width}'))

    def test_negative_height(self):
        r = Rectangle(3, -4)
        self.assertEqual(r.height, NegativeValueError(f'Высота должна быть положительной, а не {r.height}'))
        

unittest.main(verbosity=2)
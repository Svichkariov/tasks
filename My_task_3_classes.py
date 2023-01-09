'''
Задание 3.
Классы. Наследование, волшебные методы.
'''


# Необходимо реализовать семейство классов, обеспечивающих прозрачную работу с такими единицами
# измерения, как миллиметры, сантиметры, метры, километры, дюймы, футы, ярды, фэнь, чи и инь.
# Требуется реализовать метод __str__, который будет возвращать текущее значение и единицу измерения,
# например "1 км", "2.35 мили" и т. д.
# Требуется реализовать методы __eq__ и __lt__ для сравнения любых единиц измерения между собой.
# Требуется реализовать методы __add__, __iadd__, __sub__ и __isub__, принимающие в качестве
# аргумента любой класс единиц, а также просто число. Если в качестве аргумента выступает число,
# то оно трактуется, как количество текущих единиц измерения.
# Требуется реализовать методы __mul__ и __imul__, принимающие числовое значение в качестве аргумента.
# Требуется реализовать методы __div__ и __idiv__, принимающие как числовое значение, так и любой класс
# единиц измерения. В случае, если в качестве аргумента выступает числовое значение, то результат
# возвращается в тех же единицах измерения, что и текущая. В остальных случаях возвращается число.
# Требуется добавить способ конвертации из одной системы единиц в другую (желательно с использованием
# __init__.
# Необходимо выбрать базовую единицу измерения, к которой во время выполнения операций будут
# приводиться все значения. Ее же использовать и в базовом классе. Практически вся функциональность
# реализуется в базовом классе. Иерархию наследования можно сделать двухуровневой, задача подходит
# для этого.
class LengthUnits:
    """Базовое значение примем 1 метр"""

    def __init__(self, value, lehgth_units='метр', value_basic=1):
        self.value = value
        self.lehgth_units = lehgth_units
        self.value_basic = value_basic

    def __eq__(self, other):
        if isinstance(other, LengthUnits):
            return self.value_basic == other.value_basic
        return False

    def __lt__(self, other):
        return self.value_basic < other.value_basic

    def __add__(self, other):
        return f"{self.value_basic + other.value_basic} метров "

    def __iadd__(self, other):
        self.value_basic = self.value_basic + other.value_basic
        return f"{self.value_basic} метров"

    def __sub__(self, other):
        return LengthUnits(self.value_basic - other.value_basic, self.lehgth_units)

    def __isub__(self, other):
        self.value_basic = self.value_basic - other.value_basic
        return self.value_basic

    def __mul__(self, other):
        return LengthUnits(self.value_basic * other.value_basic, self.lehgth_units)

    def __imul__(self, other):
        self.value_basic = self.value_basic * other.value_basic
        return self.value_basic

    def __divmod__(self, other):
        self.value_basic = self.value_basic / other.value_basic
        return self.value_basic

    def __idiv__(self, other):
        self.value_basic = self.value_basic / other.value_basic
        return self.value_basic

    def __str__(self):
        return f"{self.value} {self.lehgth_units}"


class Millimeters(LengthUnits):
    def __init__(self, value, value_basic=1, lehgth_units='миллиметров'):
        super(Millimeters, self).__init__(value_basic)
        self.value = value
        self.lehgth_units = lehgth_units
        self.value_basic = self.value / 1000

    def __str__(self):
        return f"{self.value} {self.lehgth_units}"


class Centimeters(LengthUnits):
    def __init__(self, value, value_basic=1, lehgth_units='сантиметров'):
        super(Centimeters, self).__init__(value_basic)
        self.value = value
        self.lehgth_units = lehgth_units
        self.value_basic = self.value / 100

    def __str__(self):
        return f"{self.value} {self.lehgth_units}"


class Meters(LengthUnits):
    def __init__(self, value, value_basic=1, lehgth_units='метров'):
        super(Meters, self).__init__(value_basic)
        self.value = value
        self.lehgth_units = lehgth_units
        self.value_basic = self.value / 1

    def __str__(self):
        return f"{self.value} {self.lehgth_units}"


class Kilometers(LengthUnits):
    def __init__(self, value, value_basic=1, lehgth_units='километров'):
        super(Kilometers, self).__init__(value_basic)
        self.value = value
        self.lehgth_units = lehgth_units
        self.value_basic = self.value * 1000

    def __str__(self):
        return f"{self.value} {self.lehgth_units}"


class Inches(LengthUnits):
    def __init__(self, value, value_basic=1, lehgth_units='дюймов'):
        super(Inches, self).__init__(value_basic)
        self.value = value
        self.lehgth_units = lehgth_units
        self.value_basic = self.value * 0.0254

    def __str__(self):
        return f"{self.value} {self.lehgth_units}"


class Feets(LengthUnits):
    def __init__(self, value, value_basic=1, lehgth_units='футов'):
        super(Feets, self).__init__(value_basic)
        self.value = value
        self.lehgth_units = lehgth_units
        self.value_basic = self.value * 0.3

    def __str__(self):
        return f"{self.value} {self.lehgth_units}"


class Yards(LengthUnits):
    def __init__(self, value, value_basic=1, lehgth_units='ярдов'):
        super(Yards, self).__init__(value_basic)
        self.value = value
        self.lehgth_units = lehgth_units
        self.value_basic = self.value * 0.91

    def __str__(self):
        return f"{self.value} {self.lehgth_units}"


class Miles(LengthUnits):
    def __init__(self, value, value_basic=1, lehgth_units='миль'):
        super(Miles, self).__init__(value_basic)
        self.value = value
        self.lehgth_units = lehgth_units
        self.value_basic = self.value * 1.61

    def __str__(self):
        return f"{self.value} {self.lehgth_units}"


class Fen(LengthUnits):
    def __init__(self, value, value_basic=1, lehgth_units='фэн'):
        super(Fen, self).__init__(value_basic)
        self.value = value
        self.lehgth_units = lehgth_units
        self.value_basic = self.value / 10000

    def __str__(self):
        return f"{self.value} {self.lehgth_units}"


class Chi(LengthUnits):
    def __init__(self, value, value_basic=1, lehgth_units='чи'):
        super(Chi, self).__init__(value_basic)
        self.value = value
        self.lehgth_units = lehgth_units
        self.value_basic = self.value * 0.32

    def __str__(self):
        return f"{self.value} {self.lehgth_units}"


class In(LengthUnits):
    def __init__(self, value, value_basic=1, lehgth_units='ин'):
        super(In, self).__init__(value_basic)
        self.value = value
        self.lehgth_units = lehgth_units
        self.value_basic = self.value * 0.0254

    def __str__(self):
        return f"{self.value} {self.lehgth_units}"




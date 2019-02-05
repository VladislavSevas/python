print('Prudnikov Vladislav')
print()
print('Задача-1:')
print()
#  Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math
class treygol(object):
    A: list
    B: list
    C: list
    
    def __init__(self, A, B, C):
        self.a = A
        self.b = B
        self.c = C
        
    def S_tr(self):
        x1 = self.a[0] - self.c[0]
        x2 = self.a[1] - self.c[1]
        x3 = self.b[0] - self.c[0]
        x4 = self.b[1] - self.c[1]
        Str = 0.5 * (x1 * x4 - x2 * x3)
        print('Площадь треугольника = {} у.е.'.format(abs(Str)))
        
    def P_tr(self):
        c = self.c
        b = self.b
        a = self.a
        AB = math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
        AC = math.sqrt((a[0] - c[0]) ** 2 + (a[1] - c[1]) ** 2)
        BC = math.sqrt((b[0] - c[0]) ** 2 + (b[1] - c[1]) ** 2)
        ABC = AB + AC + BC
        print('Длины сторон: \n'
              'AB = {} у.е., AC = {} у.е., BC = {} у.е.\n'
              'Периметр: \n'
              'ABC = {} у.е.'.format(round(AB,2), round(AC,2), round(BC,2), round(ABC,2)))

    def H_tr(self):
        c = self.c
        b = self.b
        a = self.a
        HA = abs((b[1] - c[1]) * a[0] + \
                 (c[0] - b[0]) * a[1] + \
                 (b[0] * c[1] - c[0] * b[1])) / \
                 math.sqrt((b[1] - c[1]) ** 2 + (c[0] - b[0]) ** 2)
        HB = abs((a[1] - c[1]) * b[0] + \
                 (c[0] - a[0]) * b[1] + \
                 (a[0] * c[1] - c[0] * a[1])) / \
                 math.sqrt((a[1] - c[1]) ** 2 + (c[0] - a[0]) ** 2)
        HC = abs((b[1] - a[1]) * c[0] + \
                 (a[0] - b[0]) * c[1] + \
                 (b[0] * a[1] - a[0] * b[1])) / \
                 math.sqrt((self.b[1] - self.a[1]) ** 2 + (self.a[0] - self.b[0]) ** 2)
        print('Высоты треугольника: \n'
              'Из вершины A = {} у.е. \n'
              'Из вершины B = {} у.е. \n'
              'Из вершины C = {} у.е.'.format(round(HA,2), round(HB,2), round(HC,2)))

tr1 = treygol((0, 0), (13, 6), (6, 23))
tr1.S_tr()
tr1.P_tr()
tr1.H_tr()
print()
tr2 = treygol((3, 10), (33, 26), (16, 53))
tr2.S_tr()
tr2.P_tr()
tr2.H_tr()

print()
print('Задача-2:')
print()
# Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class trapeciya(object):
    A: list
    B: list
    C: list
    D: list

    def __init__(self, A, B, C, D):
        self.a = A
        self.b = B
        self.c = C
        self.d = D

    def ABandCD(self):
        AB = (abs(self.a[0] - self.b[0]), abs(self.a[1] - self.b[1]))
        CD = (abs(self.c[0] - self.d[0]), abs(self.c[1] - self.d[1]))
        if AB == CD:
            print('Трапеция равнобочная')
        else:
            print('Трапеция не равнобочная')

    def PStrap(self):
        c = self.c
        b = self.b
        a = self.a
        d = self.d
        AB = math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
        BC = math.sqrt((b[0] - c[0]) ** 2 + (b[1] - c[1]) ** 2)
        CD = math.sqrt((c[0] - d[0]) ** 2 + (c[1] - d[1]) ** 2)
        AD = math.sqrt((a[0] - d[0]) ** 2 + (a[1] - d[1]) ** 2)
        ABCD = AB + BC + CD + AD
        H = math.sqrt(AB ** 2 - (((AD - BC) ** 2 + AB ** 2 - CD ** 2) / (2 * (AD - BC))) ** 2)
        Strap = ((BC + AD) / 2) * H
        print('Длины сторон: \n'
              'AB = {} у.е., BC = {} у.е., CD = {} у.е., AD = {} у.е.\n'
              'Периметр: \n'
              'ABCD = {} у.е. \n'
              'Площадь: \n'
              'ABCD = {} у.е. \n'
              ''.format(round(AB,2), round(BC,2), round(CD,2), round(AD,2), round(ABCD,2), round(Strap,2)))
# не знаю, можно ли round() сделать 1 на всех или нет, если можно подскажите как.
# не вставлял round() в расчетах, что бы были более точные цифры.       


    

trap1 = trapeciya((0,0), (2,10), (12,14), (14,4))
trap1.ABandCD()
trap1.PStrap()

trap2 = trapeciya((2,3), (3,15), (12,16), (12,5))
trap2.ABandCD()
trap2.PStrap()



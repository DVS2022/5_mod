class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    
    def dist(self, other):
        return (((other.x-self.x)**2 + (other.y-self.y)**2)**0.5)
         
    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def __str__(self):
        return f'{self.x},{self.y}'
    

x1 = (int(input('Введите х1 = ')))
y1 = (int(input('Введите y1 = ')))
x2 = (int(input('Введите х2 = ')))
y2 = (int(input('Введите y2 = ')))

t1 = Point(x1, y1)
t2 = Point(x2, y2)

print('\nТочка А = (',(t1), ')')
print('Точка B = (',(t2), ')')

print('\nСложение = ', t1 + t2)
print('Вычитание = ', t1 - t2)
print('Скалярное произведение = ', t1 * t2)
print('Расстояние между точками =', Point.dist(t1,t2))
class ComplexNumber:
    def __init__(self, real, fake):
        self.real = real
        self.fake = fake

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.fake + other.fake)

    def __mul__(self, other):
        return ComplexNumber(self.real * other.real - self.fake * other.fake,
                             self.real * other.fake + self.fake * other.real)

    def __str__(self):
        return f'{self.real}+{self.fake}j' if self.fake >= 0 else f'{self.real}{self.fake}j'


number_1 = ComplexNumber(2, 3)
number_2 = ComplexNumber(-1, 2)
number_3 = ComplexNumber(4, -3)
number_4 = ComplexNumber(-10, -13)
number_5 = ComplexNumber(0, 7)
for i in (number_1, number_2, number_3, number_4, number_5):
    print(i)
print('=' * 50)
print(number_1 + number_2)
print(number_3 + number_4)
print(number_1 * number_2)
print(number_3 * number_4)

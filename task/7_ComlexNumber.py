class ComplexNumber:
    __slots__ = ('real', 'imag')  # Оптимизация памяти

    def __init__(self, real, imag) -> None:
        self.real = real
        self.imag = imag

    def conjugate(self):
        return ComplexNumber(self.real, -self.imag)

    def modulus_squared(self):
        return self.real**2 + self.imag**2

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return ComplexNumber(
            self.real * other.real - self.imag * other.imag,
            self.real * other.imag + self.imag * other.real
        )

    def __truediv__(self, other):
        conjugate = other.conjugate()
        numerator = self * conjugate
        denominator = other.modulus_squared()
        return ComplexNumber(numerator.real / denominator, numerator.imag / denominator)

    def __repr__(self):
        return f"ComplexNumber(real={round(self.real, 3)}, imag={round(self.imag, 3)})"

if __name__ == "__main__":
    a = ComplexNumber(5,9)
    b = ComplexNumber(7,3)
    c = a / b
    print(c)
    pass
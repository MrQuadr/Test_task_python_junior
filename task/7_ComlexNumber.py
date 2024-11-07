class ComplexNumber:
    def __init__(self, real, imag) -> None:
        self.real = real
        self.imag = imag
        pass

    def __add__(self, other):
        return ComplexNumber((self.real+other.real),\
                             (self.imag+other.imag))

    def __sub__(self, other):
        return ComplexNumber((self.real-other.real),\
                             (self.imag-other.imag))

    def __mul__(self, other):
        result_real = self.real*other.real -\
                        self.imag*other.imag
        result_imag = self.real*other.imag +\
                        self.imag*other.real
        return ComplexNumber(result_real, result_imag)

    def __truediv__(self, other):
        denominator = other.real**2 + other.imag**2
        result = self * ComplexNumber(other.real, (-1)*other.imag)
        result.real /= denominator
        result.imag /= denominator
        return result

if __name__ == "__main__":
    a = ComplexNumber(5,9)
    b = ComplexNumber(7,3)
    c = a / b
    print(c.real, c.imag)
    pass
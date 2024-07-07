from package.maths.terms import Hexagono

def workspace():
    lado = float(input("digite o lado do hexagono: "))
    objHexagono = Hexagono(lado)

    area = objHexagono.area()
    perimetro = objHexagono.perimetro()

    print(f"area: {area}")
    print(f"perimetro: {perimetro}")

workspace()

from package.maths.terms import Hexagono

def workspace():
    lado = float(input("digite o lado do hexagono: "))
    x = float(input("x: "))
    y = float(input("y: "))
    objHexagono = Hexagono(lado,x,y)

    area = objHexagono.area()
    perimetro = objHexagono.perimetro()

    print(f"area: {area}")
    print(f"perimetro: {perimetro}")


if __name__ == "__main__":

    print("O arquivo 'testbench.py' foi envocado como programa")
    print(f'__name__ == {__name__}')
    workspace()

else:

    print("o arquivo 'testbench.py' foi envocado como modulo")
    print(f'__name__ == {__name__}')

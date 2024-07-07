from package.maths.terms import Losango

def workspace():
    lado = float(input("digite o lado do losango: "))
    diagonal_menor = float(input("digite a diagonal menor: "))
    diagonal_maior = float(input("digite a diagonal maior: "))

    objLosango = Losango(lado, diagonal_maior, diagonal_menor)

    area = objLosango.area()
    perimetro = objLosango.perimetro()

    print(f"area: {area}")
    print(f"perimetro: {perimetro}")
workspace()

if __name__ == "__main__":

    print("O arquivo 'testbench.py' foi envocado como programa")
    print(f'__name__ == {__name__}')
    workspace()

else:

    print("o arquivo 'testbench.py' foi envocado como modulo")
    print(f'__name__ == {__name__}')

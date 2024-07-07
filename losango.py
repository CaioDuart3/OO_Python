from package.maths.terms import Losango

lado = float(input("digite o lado do losango: "))
diagonal_menor = float(input("digite a diagonal menor: "))
diagonal_maior = float(input("digite a diagonal maior: "))

objLosango = Losango(lado, diagonal_maior, diagonal_menor)

area = objLosango.area()
perimetro = objLosango.perimetro()

print(f"area: {area}")
print(f"perimetro: {perimetro}")
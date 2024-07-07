from package.maths.terms import TriangEquilatero

def workspace():
    print('rodando triangulo equilatero...\n')

    a = int(input("digite o valor do lado a: "))
    b = int(input("digite o valor do lado b: "))
    c = int(input("digite o valor do lado c: "))

    obj_eq = TriangEquilatero(a,b,c)
    area = obj_eq.area()
    altura = obj_eq.altura()
    perimetro = obj_eq.perimetro()

    print(a)
    print(f'area: {area}')
    print(f'altura: {altura}')
    print(f'perimetro: {perimetro}')

workspace()

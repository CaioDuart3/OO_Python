from package.maths.terms import TriangIsosceles

def workspace():
    print('rodando triangulo isosceles...\n')

    a = float(input("digite o valor do lado a: "))
    b = float(input("digite o valor do lado b: "))
    c = float(input("digite o valor do lado c: "))

    obj_es = TriangIsosceles(a,b,c)
    
    area = obj_es.area()
    altura = obj_es._altura()
    perimetro = obj_es.perimetro() #é impresso através de herança
    type
    print(f'area: {area}')
    print(f'altura: {altura}')
    print(f'perimetro: {perimetro}')

workspace()
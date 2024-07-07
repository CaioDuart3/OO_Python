from package.maths.terms import TriangEscaleno

def workspace():
    print('rodando triangulo escaleno...\n')

    a = float(input("digite o valor do lado a: "))
    b = float(input("digite o valor do lado b: "))
    c = float(input("digite o valor do lado c: "))

    obj_es = TriangEscaleno(a,b,c)
    
    obj_es.angulosInternos()
    area = obj_es.area()
    altura = obj_es._altura() # ? note que está imprimindo um método protegido.
    perimetro = obj_es.perimetro()

    print(f'area: {round(area,2)}')
    print(f'altura: {altura}')
    print(f'perimetro: {perimetro}')

workspace()
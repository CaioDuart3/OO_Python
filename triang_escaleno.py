from package.maths.terms import TriangEscaleno

def workspace():
    print('rodando triangulo escaleno...\n')

    a = float(input("digite o valor do lado a: "))
    b = float(input("digite o valor do lado b: "))
    c = float(input("digite o valor do lado c: "))

    obj_es = TriangEscaleno(a,b,c)
    
    obj_es.angulosInternos()
    area = obj_es.area()
    altura = obj_es.altura() # note que está imprimindo um método protegido.
    perimetro = obj_es.perimetro()

    print(f'area: {area}')
    print(f'altura: {altura}')
    print(f'perimetro: {perimetro}')


if __name__ == "__main__":

    print("O arquivo 'testbench.py' foi envocado como programa")
    print(f'__name__ == {__name__}')
    workspace()

else:

    print("o arquivo 'testbench.py' foi envocado como modulo")
    print(f'__name__ == {__name__}')
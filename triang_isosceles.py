from package.maths.terms import TriangIsosceles

def workspace():
    print('rodando triangulo isosceles...\n')

    a = float(input("digite o valor do lado a: "))
    b = float(input("digite o valor do lado b: "))
    c = float(input("digite o valor do lado c: "))

    obj_is = TriangIsosceles(a,b,c)
    
    area = obj_is.area()
    altura = obj_is.altura()
    perimetro = obj_is.perimetro() #é impresso através de herança
    obj_is.angulosInternos()
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
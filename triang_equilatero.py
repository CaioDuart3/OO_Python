from package.maths.terms import TriangEquilatero

def workspace():
    print('rodando triangulo equilatero...\n')

    a = float(input("digite o valor do lado a: "))
    b = float(input("digite o valor do lado b: "))
    c = float(input("digite o valor do lado c: "))
    x = float(input("x: "))
    y = float(input("y: "))

    obj_eq = TriangEquilatero(a,b,c,x,y)
    area = obj_eq.area()
    altura = obj_eq.altura()
    perimetro = obj_eq.perimetro()

    print(a)
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

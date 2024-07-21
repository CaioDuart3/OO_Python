from package.maths.terms import Coo_unica

def workspace():
    x = float(input("digite o valor de x: "))
    y = float(input("digite o valor de y: "))

    objCoo = Coo_unica(x,y)
    coo_x = objCoo.getX
    coo_y = objCoo.getY
    print(f'x digitado: {coo_x}')
    print(f'y digitado: {coo_y}')


if __name__ == "__main__":

    print("O arquivo 'testbench.py' foi envocado como programa")
    print(f'__name__ == {__name__}')
    workspace()
else:

    print("o arquivo 'testbench.py' foi envocado como modulo")
    print(f'__name__ == {__name__}')

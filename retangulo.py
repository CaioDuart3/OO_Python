from package.maths.terms import Retangulo

def workspace():
    c = float(input("e1: "))
    h = float(input("e2: "))
    x = float(input("x: "))
    y = float(input("y: "))
    obj_r = Retangulo(c,h,x,y)
    a = obj_r.area()
    p = obj_r.perimetro()
    d = obj_r.diagonal()
    print(f"area: {a}\nperimetro: {p}\ndiagonal: {d}")


if __name__ == "__main__":

    print("O arquivo 'testbench.py' foi envocado como programa")
    print(f'__name__ == {__name__}')
    workspace()

else:

    print("o arquivo 'testbench.py' foi envocado como modulo")
    print(f'__name__ == {__name__}')

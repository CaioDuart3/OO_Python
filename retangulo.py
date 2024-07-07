from package.maths.terms import Retangulo

def workspace():
    e1 = float(input("e1: "))
    e2 = float(input("e2: "))
    obj_r = Retangulo(e1,e2)
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

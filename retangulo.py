from package.maths.terms import Retangulo

def workspace():
    e1 = int(input("e1: "))
    e2 = int(input("e2: "))
    obj_r = Retangulo(e1,e2)
    a = obj_r.area()
    p = obj_r.perimetro()
    d = obj_r.diagonal()
    print(f"area: {a}\nperimetro: {p}\ndiagonal: {d}")
workspace()
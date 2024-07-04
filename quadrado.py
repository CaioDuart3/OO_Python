from package.maths.terms import Quadrado

def workspace():
    l = int(input("lado: "))
    obj_q = Quadrado(l)
    a = obj_q.area()
    p = obj_q.perimetro()
    d = obj_q.diagonal()
    print(f'area: {a}\nperimetro: {p}\ndiagonal: {d}')
workspace()


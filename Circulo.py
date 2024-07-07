from package.maths.terms import Circulo, coo_circulo
def workspace():
    coo = coo_circulo() #criar instancia para ser utilizada nos parametros de outra instancia, como forma de associação.
    r = int(input("digite o raio: "))
    obj_cir = Circulo(coo.coordenadaX(),coo.coordenadaY(), r) #agregação, pois a utilizade dele vem dessa relação
    c = obj_cir.circunferencia()
    print(f"circunferencia: {c}")
    a =obj_cir.areaCirculo()
    print(f"area: {a}")
    d = obj_cir.diametro()
    print(f"diametro: {d}")
workspace()
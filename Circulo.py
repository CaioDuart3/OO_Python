from package.maths.terms import Circulo, coo_circulo
def workspace():
    obj_cu = coo_circulo() #criar instancia para ser utilizada nos parametros de outra instancia, como forma de associação.
    r = int(input("digite o raio: "))
    obj_cir = Circulo(obj_cu.coordenadaX(),obj_cu.coordenadaY(), r) #agregação, pois são 2 duas instaciação forte
    c = obj_cir.circunferencia()
    print(f"circunferencia: {c}")
    a =obj_cir.areaCirculo()
    print(f"area: {a}")
    d = obj_cir.diametro()
    print(f"diametro: {d}")
workspace()
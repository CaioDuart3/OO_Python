from package.maths.terms import Circulo, coo_circulo
def workspace():
    coo = coo_circulo() #criar instancia para ser utilizada nos parametros de outra instancia, como forma de associação.
    r = float(input("digite o raio: "))
    obj_cir = Circulo(coo.coordenadaX(),coo.coordenadaY(), r) #agregação, pois a utilizade dele vem dessa relação
    c = obj_cir.circunferencia()
    print(f"circunferencia: {c}")
    a =obj_cir.areaCirculo()
    print(f"area: {a}")
    d = obj_cir.diametro()
    print(f"diametro: {d}")

if __name__ == "__main__":

    print("O arquivo 'testbench.py' foi envocado como programa")
    print(f'__name__ == {__name__}')
    workspace()

else:

    print("o arquivo 'testbench.py' foi envocado como modulo")
    print(f'__name__ == {__name__}')

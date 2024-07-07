from package.maths.terms import TrapezioIsosceles
def workspace():
    b = float(input("base menor: "))
    B = float(input("base maior: "))
    h = float(input('altura: '))

    obj_ti = TrapezioIsosceles(b,B,h)
    area_Ti = obj_ti.area()
    p_Ti = obj_ti.perimetro()
    getAlturaTi= obj_ti.getAltura()

    print(f'area Ti: {area_Ti}')
    print(f'perimetro Ti: {p_Ti}')
    print(f"getTi: {getAlturaTi}")

workspace()

if __name__ == "__main__":

    print("O arquivo 'testbench.py' foi envocado como programa")
    print(f'__name__ == {__name__}')
    workspace()

else:

    print("o arquivo 'testbench.py' foi envocado como modulo")
    print(f'__name__ == {__name__}')

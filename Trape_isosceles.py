from package.maths.terms import TrapezioIsosceles
def workspace():
    b = int(input("base menor: "))
    B = int(input("base maior: "))
    h = int(input('altura: '))

    obj_ti = TrapezioIsosceles(b,B,h)
    area_Ti = obj_ti.area()
    p_Ti = obj_ti.perimetro()

    print(f'area Ti: {area_Ti}')
    print(f'perimetro Ti: {p_Ti}')
    getAlturaTi= obj_ti.getAltura()
    print(f"getTi: {getAlturaTi}")

workspace()


from package.maths.terms import TrapezioRetangulo

def workspace():
    b = int(input("base menor: "))
    B = int(input("base maior: "))
    h = int(input('altura: '))
    # obj_ti = TrapezioIsosceles(b,B,h)
    # area_Ti = obj_ti.area()
    # p_Ti = obj_ti.perimetro()
    # print(f'area Ti: {area_Ti}')
    # print(f'perimetro Ti: {p_Ti}')
    # getAlturaTi= obj_ti.getAltura()
    # print(f"getTi: {getAlturaTi}")


    obj_tr = TrapezioRetangulo(b,B,h)
    area_Tr = obj_tr.area()
    p_Tr = obj_tr.perimetro()
    print(f"area Tr: {area_Tr}")
    print(f"perimetro Tr: {p_Tr}")
    getAlturaTr = obj_tr.getAltura()
    print(f"getTr: {getAlturaTr}")
workspace()


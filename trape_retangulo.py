from package.maths.terms import TrapezioRetangulo

def workspace():
    b = float(input("base menor: "))
    B = float(input("base maior: "))
    h = float(input('altura: '))

    obj_tr = TrapezioRetangulo(b,B,h)
    area_Tr = obj_tr.area()
    p_Tr = obj_tr.perimetro()
    getAlturaTr = obj_tr.getAltura()

    print(f"area Tr: {area_Tr}")
    print(f"perimetro Tr: {p_Tr}")
    print(f"getTr: {getAlturaTr}")



if __name__ == "__main__":

    print("O arquivo 'testbench.py' foi envocado como programa")
    print(f'__name__ == {__name__}')
    workspace()

else:

    print("o arquivo 'testbench.py' foi envocado como modulo")
    print(f'__name__ == {__name__}')


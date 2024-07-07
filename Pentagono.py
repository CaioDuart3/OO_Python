from package.maths.terms import Pentagono

def workspace():
    lado = float(input("digite o lado do pentagono: "))
    objPentagono = Pentagono(lado)
    
    area = objPentagono.area()
    perimetro = objPentagono.perimetro()
    
    print(f'area {area}')
    print(f'perimetro: {perimetro}')

workspace()
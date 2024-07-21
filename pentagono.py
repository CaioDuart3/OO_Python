from package.maths.terms import Pentagono

def workspace():
    lado = float(input("digite o lado do pentagono: "))
    x = float(input("x: "))
    y = float(input("y: "))
    objPentagono = Pentagono(lado,x,y)
    
    area = objPentagono.area()
    perimetro = objPentagono.perimetro()
    raio = objPentagono.raio
    print(f'area {area}')
    print(f'perimetro: {perimetro}')
    print(f'raio: {raio}')
    

if __name__ == "__main__":

    print("O arquivo 'testbench.py' foi envocado como programa")
    print(f'__name__ == {__name__}')
    workspace()

else:

    print("o arquivo 'testbench.py' foi envocado como modulo")
    print(f'__name__ == {__name__}')

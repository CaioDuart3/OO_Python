from package.maths.terms import Quadrado

def workspace():
    lado = float(input("lado: "))
    objQuadrado = Quadrado(lado) #quadrado recebe lado como um dado privado

    diagonal_quadrado = objQuadrado.diagonal()
    area_quadrado = objQuadrado.area()
    perimetro_quadrado = objQuadrado.perimetro()

    print(f'area: {area_quadrado}\nperimetro: {perimetro_quadrado}\ndiagonal: {diagonal_quadrado}')

    # ! print(objQuadrado.__l) não funciona pois "__l" é privado, precisa de um método acessor(get).
    # * agora __l pode ser impresso através de um método acessor (get).
    get = objQuadrado.getLado()
    print(f'get: {get}') # encapsulamento de atríbuto.

workspace()

if __name__ == "__main__":

    print("O arquivo 'testbench.py' foi envocado como programa")
    print(f'__name__ == {__name__}')
    workspace()

else:

    print("o arquivo 'testbench.py' foi envocado como modulo")
    print(f'__name__ == {__name__}')

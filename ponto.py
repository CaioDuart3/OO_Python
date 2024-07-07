from package.maths.terms import Ponto

def workspace():
    n = float(input("digite a quantidade de pontos: "))
    objPonto = Ponto(n)

    cor = objPonto.cor()
    coo = objPonto.coordenada()
    print(f"cores: {cor}\n")
    print(f"coordenadas: {coo}\n")

    objPonto.setPontosX(coo) 
    objPonto.setPontosY(coo) 

    x = objPonto.retornarPontosX(coo)
    y = objPonto.retornarPontosY(coo)
    print(f'{x}')
    print(f'{y}')
    print(f'novas coordenadas: {coo}')

workspace()

if __name__ == "__main__":

    print("O arquivo 'testbench.py' foi envocado como programa")
    print(f'__name__ == {__name__}')
    workspace()

else:

    print("o arquivo 'testbench.py' foi envocado como modulo")
    print(f'__name__ == {__name__}')

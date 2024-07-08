from package.maths.terms import Ponto

def workspace():
    n = int(input("digite a quantidade de pontos: "))
    objPonto = Ponto(n)

    cor = objPonto.cor()
    coo = objPonto.coordenada()
    print(f"cores: {cor}\n")
    print(f"coordenadas: {coo}\n")

    objPonto.setPontosX(coo) 
    objPonto.setPontosY(coo) 

    vetor_x = objPonto.retornarPontosX(coo)
    vetor_y = objPonto.retornarPontosY(coo)
    print(f'{vetor_x}')
    print(f'{type(vetor_y)}')
    print(f'novas coordenadas: {coo}')

    objPonto.exibirPonto(coo,cor)

if __name__ == "__main__":

    print("O arquivo 'testbench.py' foi envocado como programa")
    print(f'__name__ == {__name__}')
    workspace()

else:

    print("o arquivo 'testbench.py' foi envocado como modulo")
    print(f'__name__ == {__name__}')

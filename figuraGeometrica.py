from package.maths.terms import FigurasGeometricas, Coo_unica, Quadrado

def workspace():
    formas = FigurasGeometricas()

    
    while(True):
        print('\nescolha o número da opção que deseja criar:')
        print('1- coordenada unica')
        print('2- quadrado')
        print('3- listar formas criadas')
        print('4- remover forma criada')
        print('5- sair')
        escolha = int(input("opção: "))
        if escolha == 1:
            x = float(input("x: "))
            y = float(input("y: "))
            coo = Coo_unica(x,y)
            formas.inserirForma(coo)
            escolha = 0
            print('coordenada unica criada. \n')
        elif escolha == 2:
            lado = float(input("lado: "))
            quadrado = Quadrado(lado)
            formas.inserirForma(quadrado)
            print('quadrado criado. \n')
        elif escolha == 3:
            formas.listarFormas()
            print('\n')
        elif escolha == 4:
            key = input("escolha a criação que você deseja apagar: ")
            formas.listarFormas()
            formas.removerForma(key)
            print('\n')
        elif escolha == 5:
            print('\n fechando sistema... ')
            break
    
if __name__ == "__main__":

    print("O arquivo 'testbench.py' foi envocado como programa")
    print(f'__name__ == {__name__}')
    workspace()

else:

    print("o arquivo 'testbench.py' foi envocado como modulo")
    print(f'__name__ == {__name__}')

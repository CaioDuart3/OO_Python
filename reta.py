from package.maths.terms import Reta
def workspace():
    n = int(input("digite a qtd de pontos na reta: "))

    obj_Reta = Reta(n) #instanciação
    m = obj_Reta.inclinacao() #
    b = obj_Reta.coefLinear(obj_Reta.inclinacao()) #associação.
    d = obj_Reta.distancia()

    print(f"m: {m}")
    print(f"b: {b}")
    print(f"distância: {d}")

    i = int(input("quantidade de iterações:"))
    obj_Reta.montarTabela(m,b,i)
    
    y = obj_Reta.interpolar(obj_Reta.inclinacao(),b,i) #associação, pois usa a inclinação, mas não chega a possui-la
    print(f'interpolar, y = {y}')


if __name__ == "__main__":

    print("O arquivo 'testbench.py' foi envocado como programa")
    print(f'__name__ == {__name__}')
    workspace()

else:

    print("o arquivo 'testbench.py' foi envocado como modulo")
    print(f'__name__ == {__name__}')

from package.maths.terms import Reta
def workspace():
    n = float(input("digite a qtd de pontos na reta: "))

    obj_Reta = Reta(n) #instanciação
    m = obj_Reta.inclinacao() #
    b = obj_Reta.CoefLinear(obj_Reta.inclinacao()) #associação.

    print(f"m: {m}")
    print(f"b: {b}")

    i = float(input("quantidade de iterações:"))
    obj_Reta.montarTabela(m,b,i)
    
    y = obj_Reta.interpolar(m,b,i)
    print(y)
workspace()

if __name__ == "__main__":

    print("O arquivo 'testbench.py' foi envocado como programa")
    print(f'__name__ == {__name__}')
    workspace()

else:

    print("o arquivo 'testbench.py' foi envocado como modulo")
    print(f'__name__ == {__name__}')

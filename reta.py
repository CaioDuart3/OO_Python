from package.maths.terms import Reta
def workspace():
    n = int(input("digite a qtd de pontos na reta: "))

    obj_Reta = Reta(n) #instanciação
    m = obj_Reta.inclinacao() #
    b = obj_Reta.CoefLinear(obj_Reta.inclinacao()) #associação.

    print(f"m: {m}")
    print(f"b: {b}")

    i = int(input("quantidade de iterações:"))
    obj_Reta.montarTabela(m,b,i)
    
    y = obj_Reta.interpolar(m,b,i)
    print(y)
workspace()
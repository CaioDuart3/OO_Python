from package.maths.terms import Reta
def workspace():
    n = int(input("digite a qtd de pontos na reta: "))
    obj_Reta = Reta(n)
    m = obj_Reta.inclinacao()
    print(f"m: {m}")
    b = obj_Reta.CoefLinear(obj_Reta.inclinacao()) #associação.
    print(f"b: {b}")
    # obj_Reta.montarTabela()
    # a = obj_Reta.retornarTabela(2,-1)
    # print(a)
workspace()
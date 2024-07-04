from package.maths.terms import Ponto

def workspace():
    while(True):
        navegador = int(input("digite a função que deseja:\n1- criar ponto.\n2- exibir pontos X criados.\n3- exibir pontos Y criados.\n4- mudar valores de X.\n5- mudar valores de Y.\n6- exibir pontos criados.\n7-fechar programa.\n"))
        
        if navegador == 1:
            qtdPontos = int(input("qtd de pontos:"))
            objPonto = Ponto(qtdPontos)
            cor = objPonto.cor()
            pontos = objPonto.coordenada()
            print(cor)
            print(pontos)
        
        if navegador == 2:
            objPonto.getPontoX(pontos)
        
        if navegador == 3:
            objPonto.getPontoY(pontos)
        
        if navegador == 4:
            objPonto.setPontoX(pontos)
        
        if navegador == 5:
            objPonto.setPontoY(pontos)
        
        if navegador == 6:
            objPonto.getPonto(pontos,cor)
        
        if navegador == 7:
            break
workspace()
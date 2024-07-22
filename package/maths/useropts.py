from package.maths.terms import *

class FigurasGeometricas: #AGREGAÇÃO, pois vai possuir formas geometricas 
    def __init__(self):
        self.formas = {}
        self.count = 0
        self.retas = {}
    def inserirForma(self, instancia): #set
        self.count+=1
        self.formas[str(self.count) + instancia.identificador()] = instancia
    
    def removerForma(self, key):
        del self.formas[key]

    def listarFormas(self): #get
        for instancia in self.formas.keys():
            print(instancia)
            
    def retornarForma(self,key):
        return self.formas[key]
    
    def inserirReta(self,objReta): #método auxiliar para ser utilizado na opção de verificar relação com reta.
        self.retas[str(self.count) + objReta.identificador()] = objReta
    
    def listarRetas(self):
        for objReta in self.retas.keys():
            print(objReta)
            
    def retornarReta(self,key):
        return self.retas[key]

class interferencia:
    @staticmethod
    def verificacaoSegReta(coo_unica,reta):
        x = coo_unica.getX
        y = coo_unica.getY
        distancia = reta.distancia()
        
        ponto1 = reta.primeiroPonto()
        pontoN = reta.ultimoPonto()
        
        distancia1 = ((pontoN[0]-x)**2+(pontoN[1]-y)**2)**0.5
        distancia2 = ((ponto1[0]-x)**2+(ponto1[0]-y)**2)**0.5
        distancia1_2_3 = distancia1 + distancia2 
        if distancia1_2_3 <= 1.1 * distancia:
            return True
        else: 
            return False
    
    # @staticmethod
    # def verificar_distancia(self,ponto1, ponto2): #associação
    #     self.xPonto1 = ponto1.getX
    #     self.yPonto1 = ponto1.getY
    #     self.xPonto2 = ponto2.getX
    #     self.yPonto2 = ponto2.getY

    # @staticmethod
    # def distancia(self):
    #     distancia = ((self.xPonto2 - self.xPonto1)**2 + (self.yPonto2 - self.yPonto1)**2)**0.5
    #     return distancia

class Menu:
    
    #escolha - menu # option criaçãode formas # user - calculo
    def __init__(self):
        self.forma = FigurasGeometricas()
        self.tb_circulo
        self.tb_pontos

    def crash(self):
        if self.forma.formas == {}:
            print('Você não criou nenhuma forma geométrica. Volte e crie formas geométricas para utilizar esta opção.')
            print('=='*50)
        else:
            print('formas geométricas criadas:')
            self.forma.listarFormas()
            print('--'*50+'\n')
            print('Escolha uma das opções para consultar.')
            while True:
                
                print('1- Verificar formas geométricas criadas e seus detalhes.') 
                print('2- Verificar interferência.')
                print('3- Verificar relação de ponto com reta.')
                print('4- Deletar forma geométrica criada.')
                print('5- Voltar para o menu inicial.')
                escolha = input('digite oque deseja consultar: ')

                print('=='*13,end='')
                print(' resultado de escolha. ',end='')
                print('=='*25)
                

                if escolha == '1':
                    self.forma.listarFormas()
                    print('--'*50+'\n')
                    while True:
                        try:
                            escolha = input('digite a forma geométrica que você deseja visualizar melhor: ')
                            if escolha.upper() == 'EXIT':
                                break
                            else:
                                forma_temp = self.forma.retornarForma(escolha)
                                forma_temp.detalhes()
                                break
                        except KeyError:
                            print('Escreva corretamente o nome da forma geométrica que você deseja verificar OU digite "EXIT" para voltar ao menu.')
                            
                elif escolha == '2':
                    while True:
                        try:
                            print('Digite a coordenada x e y do ponto que você deseja verificar se está contido em uma forma geométrica.')
                            x_p = float(input('x: '))
                            y_p = float(input('y: '))
                            break
                        except ValueError:
                            print('Entrada inválida. Digite somente números do tipo flutante.')
                    while True:
                        try:
                            print('--'*50+'\n')
                            self.forma.listarFormas()
                            print('--'*50+'\n')
                            escolha = input('digite a forma geométrica que você deseja ver a relação de dominio: ')
                            if escolha.upper() == 'EXIT':
                                break
                            else:
                                forma_temp = self.forma.retornarForma(escolha)
                                forma_temp.verificar_interferencia(x_p,y_p)
                                break
                        except KeyError:
                            print('Escreva corretamente o nome da forma geométrica que você deseja verificar OU digite "EXIT" para voltar ao menu.')
                    
                elif escolha == '3':
                    if self.forma.retas == {}:
                        print('Você não possui retas criadas. Volte para o menu e crie alguma reta.')
                    else:
                        while True:
                            try:
                                x = float(input('digite o valor x do ponto: '))
                                y = float(input('digite o valor y do ponto: '))
                                break
                            except ValueError:
                                print('Entrada inválida. Digite somente números do tipo flutante.')
                        
                        coo_unica = Coo_unica(x,y)
                        self.forma.listarRetas()
                        
                        while True:
                            try:
                                escolha = input('digite a reta que deseja verificar: ')
                                if escolha.upper() == 'EXIT':
                                    break
                                else:
                                    reta = self.forma.retornarReta(escolha)
                                    break
                            except KeyError:
                                print('Escreva corretamente o nome da reta que você deseja verificar OU digite "EXIT" para voltar ao menu.')
                            
                        if escolha == 'EXIT':
                            break

                        bool = interferencia.verificacaoSegReta(coo_unica,reta)
                        if bool == True:
                            print('\nseu ponto tem relação com esta reta.')
                        else:
                            print('\nseu ponto não tem relação com esta reta.')
                elif escolha == '4':
                    while True:
                        self.forma.listarFormas()
                        try:
                            escolha = input('digite a forma geométrica que você deseja DELETAR da lista ou digite "EXIT" para cancelar: ')
                            if escolha.upper() == 'EXIT' :
                                break
                            else:
                                self.forma.removerForma(escolha)
                                print(f'a forma {escolha} foi deletada com sucesso.')
                                break
                        except KeyError:
                            print('Escreva corretamente o nome da forma geométrica que você deseja DELETAR.')
                elif escolha == '5':
                    break
                
                else:
                    print('Escolha uma opção válida.')
                print('=='*50)
    def tb_circulo(self):
        
        print('digite o valor de X, Y, e o raio:')
        while True:
            try:
                x = float(input('x: '))
                y = float(input('y: '))
                r = float(input('digite o raio:'))
                break
            except ValueError:
                print('Entrada inválida. Digite somente números do tipo flutante.')

        objCirculo = Circulo(x,y,r)
        self.forma.inserirForma(objCirculo)

        print('\ncirculo criado.\n')

        while(True):
            print('1- Área.')
            print('2- Diametro.')
            print('3- Circunferencia.')
            print('4- Voltar para o menu.')

            escolha = input("digite oque deseja calcular:")
            print('=='*13,end='')
            print(' resultado de escolha. ',end='')
            print('=='*25)
            if escolha == '1':
                a = objCirculo.areaCirculo()
                print(f'Área: {a}')

            elif escolha == '2':
                d = objCirculo.diametro()
                print(f'Diãmetro: {d}')
                
            elif escolha == '3':
                c = objCirculo.circunferencia()
                print(f'Circunferência: {c}')
            elif escolha == '4':
                print('Voltando para o menu...')
                print('=='*50)
                break
            else: 
                print('Escolha uma opção válida.')
            print('=='*50)
            
    def tb_pontos(self):
        while True:
            try:
                n = int(input('digite a quantidade de pontos a serem criados: '))
                if n < 1:
                    print('Digite uma quantidade válida.')
                else:
                    break
            except ValueError:
                print('Entrada inválida. Digite apenas números do tipo inteiro.')

        objPonto = Ponto(n)
        self.forma.inserirForma(objPonto)

        coo = objPonto.coordenada()

        print('\nconjunto de pontos criado.\n')

        while(True):
            print('1- Visualizar o conjunto de pontos criado.')
            print('2- Conferir os Xi criados.')
            print('3- Conferir os Yi criados.')
            print('4- Mudar os valores de Xi.')
            print('5- Mudar os valores de Yi.')
            print('6- Distância até a origem.')
            print('7- Distância entre dois pontos.')
            print('8- Voltar para o menu.')

            escolha = input("digite oque deseja calcular:")
            print('=='*13,end='')
            print(' resultado de escolha. ',end='')
            print('=='*25)

            if escolha == '1':
                objPonto.detalhes()

            elif escolha == '2':
                v_x = objPonto.retornarPontosX(coo)
                print(f'seus Xi: {v_x}')

            elif escolha == '3':
                v_y = objPonto.retornarPontosY(coo)
                print(f'seus Yi: {v_y}')

            elif escolha == '4':
                objPonto.setPontosX(coo)
                print(f'coordenadas alteradas.')

            elif escolha == '5':
                objPonto.setPontosY(coo)
                print(f'coordenadas alteradas.')

            elif escolha == '6':
                print(f'pontos armazenados em uma lista: {coo}')
                while True:
                        try:
                            ponto = int(input("digite a index do ponto: "))
                            distancia = ((coo[ponto][0])**2+(coo[ponto][1])**2)**0.5
                            x = coo[ponto][0]
                            y = coo[ponto][1]
                            break
                        except ValueError:
                            print('Entrada inválida. Digite apenas valores do tipo inteiro.')
                        except IndexError:
                            print(f'Entrada inválida. Digite apenas valores de 0 a {n-1}.')

                print(f'a distancia do seu ponto ({x} , {y}) até a origem é: {distancia}')

            elif escolha == '7':
                if n == 1:
                    print('você não possui pontos suficientes para esta tarefa.')
                else:
                    print(f'pontos armazenados em uma lista: {coo}')
                    while True:
                        try:
                            inicio = int(input("digite a index do primeiro ponto: "))
                            ultimo = int(input("digite a index do segundo ponto: "))
                            x1 = coo[inicio][0]
                            x2 = coo[ultimo][0]
                            y1 = coo[inicio][1]
                            y2 = coo[ultimo][1]
                            distancia = ((x2-x1)**2 + (y2-y1)**2)**0.5
                            break
                        except ValueError:
                            print('Entrada inválida, digite apenas valores do tipo inteiro.')
                        except IndexError:
                            print(f'Entrada inválida. Digite apenas valores de 0 a {n-1}.')
                    
                    print(f'você selecionou: {coo[inicio]} e {coo[ultimo]}')
                    print(f'a distância entre os pontos ({x1} , {y1}) e ({x2}, {y2}) é: {distancia}')

            elif escolha == '8':
                print('Voltando para o menu...')
                print('=='*50)
                break
            else:
                print('Escolha uma opção válida.')
            print('=='*50)

    def tb_reta(self):
        while True:
            try: 
                n = int(input("Digite a quantidade de pontos da reta: "))
                if n < 2:
                    print('essa quantidade de pontos não formam uma reta, é necessário um número maior que 1. Digite novamente o valor.')
                else:
                    break
            except ValueError:
                print('Entrada inválida. Digite apenas números do tipo inteiro.')
        
        objReta = Reta(n)
        self.forma.inserirForma(objReta)
        self.forma.inserirReta(objReta)

        while True:
            print('1- Inclinação da reta.')
            print('2- Coeficiente Linear.')
            print('3- Achar valor de y.')
            print('4- Tamanho do segmento de reta.')
            print('5- Voltar para o menu principal.')

            escolha = input("digite oque deseja calcular:")

            print('=='*13,end='')
            print(' resultado de escolha. ',end='')
            print('=='*25)

            m = objReta.inclinacao()
            b = objReta.coefLinear(m)
            d = objReta.distancia()
            if escolha == '1':
                print(f'Inclinação da reta: {m}')
            elif escolha == '2':
                print(f'Coeficiente linear: {b}')
            elif escolha == '3':

                while True:
                    try:
                        x = float(input('digite o valor de x: '))
                        break
                    except:
                        print('Entrada inválida. Digite apenas números do tipo flutuante.')
                print(type(m))
                print(type(b))
                if type(m) == float and type(b) == float:
                    y = objReta.interpolar(m,b,x)
                    print(f'y = m * x + b\ny = ({m}) * ({x}) + ({b})\ny = {y}')
                else:
                    print('seus pontos criaram uma reta vertical. aonde y pertence a qualquer valor dos reais reais.')

            elif escolha == '4':
                print(f'Tamanho do segmento de reta: {d}')
            
            elif escolha == '5':
                print('Voltando para o menu...')
                print('=='*50)
                break
            else:
                print('Escolha uma opção válida.')
            print('=='*50)
    def tb_triang_equila(self):
        while True:
            try:
                print('Digite o valor o lados A, B, C e a coordenada x e y: ')
                A = float(input('A: '))
                B = float(input('B: '))
                C = float(input('C: '))
                x= float(input('x: '))
                y= float(input('y: '))
                if A == B == C:
                    break
                else:
                    print("as entradas não são válidas. Note que os lados devem ser iguais para este triângulo, volte e reescreva os lados.")
            except ValueError:
                print('Entrada inválida. Digite apenas números do tipo flutante.')
        
        objTriang_eq = TriangEquilatero(A,B,C,x,y)
        self.forma.inserirForma(objTriang_eq)

        print('triângulo equilátero criado.')

        while True:
            print('1- Altura.')
            print('2- Área.')
            print('3- Perimetro.')
            print('4- Voltar para o menu.')

            escolha = input("digite oque deseja calcular:")
            print('=='*13,end='')
            print(' resultado de escolha. ',end='')
            print('=='*25)

            if escolha == '1':
                h = objTriang_eq.altura()
                print(f'Altura: {h}')
            elif escolha == '2':
                a = objTriang_eq.area()
                print(f'Área: {a}')
            elif escolha == '3':
                p = objTriang_eq.perimetro()
                print(f'Perimetro: {p}')
            elif escolha == '4':
                break
            else:
                print('Escolha uma opção válida.')
            print('=='*50)
            
    def tb_triang_isos(self):
        while True:
            try:
                print('Digite o valor o lados A, B, C e a coordenada x e y: ')
                A = float(input('A: '))
                B = float(input('B: '))
                C = float(input('C: '))
                x= float(input('x: '))
                y= float(input('y: '))
                if ((A == B and C != A) or (A == C and B != A) or (C == B and C != A)) and ((A + B) > C and (A + C) > B and (B + C) > A):
                    break
                else:
                    print("as entradas não são válidas. Os valores não formam um triângulo isoscéles. volte e reescreva os lados.")
            except ValueError:
                print('Entrada inválida. Digite apenas números do tipo flutante.')
        
        objTriang_is = TriangIsosceles(A,B,C,x,y)
        self.forma.inserirForma(objTriang_is)

        print('triângulo isoscéles criado.')

        while True:
            print('1- Altura.')
            print('2- Área.')
            print('3- Perimetro.')
            print('4- Voltar para o menu.')

            escolha = input("digite oque deseja calcular:")
            print('=='*13,end='')
            print(' resultado de escolha. ',end='')
            print('=='*25)

            if escolha == '1':
                h = objTriang_is.altura()
                print(f'Altura: {h}')
            elif escolha == '2':
                a = objTriang_is.area()
                print(f'Área: {a}')
            elif escolha == '3':
                p = objTriang_is.perimetro()
                print(f'Perimetro: {p}')
            elif escolha == '4':
                break
            else:
                print('Escolha uma opção válida.')
            print('=='*50)
    def tb_triang_esca(self):
        while True:
            try:
                print('Digite o valor o lados A, B, C e a coordenada x e y: ')
                A = float(input('A: '))
                B = float(input('B: '))
                C = float(input('C: '))
                x= float(input('x: '))
                y= float(input('y: '))
                if (A != B != C) and ((A + B) > C and (A + C) > B and (B + C) > A):
                    break
                else:
                    print("as entradas não são válidas. Os valores não formam um triângulo escaleno, volte e reescreva os lados.")
            except ValueError:
                print('Entrada inválida. Digite apenas números do tipo flutante.')
        
        objTriang_es = TriangEscaleno(A,B,C,x,y)
        self.forma.inserirForma(objTriang_es)

        print('triângulo escaleno criado.')



        while True:
            print('1- Altura.')
            print('2- Área.')
            print('3- Perimetro.')
            print('4- Ângulos internos.')
            print('5- Voltar para o menu.')

            escolha = input("digite oque deseja calcular:")
            print('=='*13,end='')
            print(' resultado de escolha. ',end='')
            print('=='*25)

            if escolha == '1':
                h = objTriang_es.altura()
                print(f'Altura: {h}')
            elif escolha == '2':
                a = objTriang_es.area()
                print(f'Área: {a}')
            elif escolha == '3':
                p = objTriang_es.perimetro()
                print(f'Perimetro: {p}')
            elif escolha == '4':
                objTriang_es.angulosInternos()
                
            elif escolha == '5':
                break
            else:
                print('Escolha uma opção válida.')
            print('=='*50)
            
    def tb_quadrado(self):
        while True:
            try: 
                print('Digite o lado do quadrado e a coordenada x e y.')
                l = float(input("lado: "))
                x = float(input("x: "))
                y = float(input("y: "))
                break
            except ValueError:
                print('Entrada inválida. Digite apenas números do tipo flutante.')
        
        objQuadrado = Quadrado(l,x,y)
        self.forma.inserirForma(objQuadrado)

        while True:
            print('1- Área.')
            print('2- Perímetro.')
            print('3- Diagonal.')
            print('4- Voltar para o menu.')

            escolha = input("digite oque deseja calcular:")

            print('=='*13,end='')
            print(' resultado de escolha. ',end='')
            print('=='*25)

            a = objQuadrado.area()
            p = objQuadrado.perimetro()
            d = objQuadrado.diagonal()

            if escolha == '1':
                print(f'Área: {a}')
            elif escolha == '2':
                print(f'Perímetro: {p}')
            elif escolha == '3':
                print(f'Diagonal: {d}')
            elif escolha == '4':
                print('Voltando para o menu...')
                print('=='*50)
                break
            else:
                print('Escolha uma opção válida.')
            print('=='*50)
            
    def tb_losango(self):
        while True:
            try: 
                print('Digite o lado, a diagonal menor, a diagonal maior, e a coordenada do losango.')
                l = float(input("lado: "))
                D = float(input("diagonal maior: "))
                d = float(input("diagonal menor: "))
                x = float(input("x: "))
                y = float(input("y: "))
                break
            except ValueError:
                print('Entrada inválida. Digite apenas números do tipo flutante.')
        
        objLosango = Losango(l,D,d,x,y)
        self.forma.inserirForma(objLosango)

        while True:
            print('1- Área.')
            print('2- Perímetro.')
            print('3- Voltar para o menu.')

            escolha = input("digite oque deseja calcular:")

            print('=='*13,end='')
            print(' resultado de escolha. ',end='')
            print('=='*25)

            a = objLosango.area()
            p = objLosango.perimetro()
            d = objLosango.diagonal()

            if escolha == '1':
                print(f'Área: {a}')
            elif escolha == '2':
                print(f'Perímetro: {p}')
            elif escolha == '3':
                print('Voltando para o menu...')
                print('=='*50)
                break
            else:
                print('Escolha uma opção válida.')
            print('=='*50)
            
    def tb_retangulo(self):
        while True:
            try:
                print('Digite o valor da largura, da altura do retangulo e de x e y.')
                largura = float(input("largura: "))
                altura = float(input("altura: "))
                x = float(input("x: "))
                y = float(input("y: "))
                break
            except ValueError:
                print('Entrada inválida. Digite apenas números do tipo flutuante.')
        
        objRetangulo = Retangulo(largura,altura,x,y)
        self.forma.inserirForma(objRetangulo)

        print('\nretangulo criado.\n')

        while(True):
            print('1- Área.')
            print('2- Perímetro.')
            print('3- Diagonal.')
            print('4- Voltar para o menu.')

            escolha = input("digite oque deseja calcular:")
            print('=='*13,end='')
            print(' resultado de escolha. ',end='')
            print('=='*25)
            if escolha == '1':
                a = objRetangulo.area()
                print(f'Área: {a}')
    
            elif escolha == '2':
                p = objRetangulo.perimetro()
                print(f'Perímetro: {p}')
    
            elif escolha == '3':
                d = objRetangulo.diagonal()
                print(f'Diagonal: {d}')
    
            elif escolha == '4':
                print('Voltando para o menu...')
                print('=='*50)
                break
            else: 
                print('Escolha uma opção válida.')
            print('=='*50)

    def tb_pentagono(self):
        while True:
            try:
                print('Digite o valor do lado do pentagono, e de x e y.')
                lado = float(input("lado: "))
                x = float(input("x: "))
                y = float(input("y: "))
                break
            except ValueError:
                print('Entrada inválida. Digite apenas números do tipo flutuante.')
        
        objPentagono = Pentagono(lado,x,y)
        self.forma.inserirForma(objPentagono)

        print('\npentagono criado.\n')

        while(True):
            print('1- Área.')
            print('2- Perímetro.')
            print('3- Raio.')
            print('4- Voltar para o menu.')

            escolha = input("digite oque deseja calcular:")
            print('=='*13,end='')
            print(' resultado de escolha. ',end='')
            print('=='*25)
            if escolha == '1':
                a = objPentagono.area()
                print(f'Área: {a}')
            elif escolha == '2':
                p = objPentagono.perimetro()
                print(f'Perímetro: {p}')
            elif escolha == '3':
                r = objPentagono.raio()
                print(f'Raio: {r}')
            elif escolha == '4':
                break
            else: 
                print('Escolha uma opção válida.')
            print('=='*50)

    def tb_hexagono(self):
        while True:
            try:
                print('Digite o valor do lado do hexagono, e de x e y.')
                lado = float(input("lado: "))
                x = float(input("x: "))
                y = float(input("y: "))
                break
            except ValueError:
                print('Entrada inválida. Digite apenas números do tipo flutuante.')
        
        objHexagono = Hexagono(lado,x,y)
        self.forma.inserirForma(objHexagono)

        print('\nhexagono criado.\n')

        while(True):
            print('1- Área.')
            print('2- Perímetro.')
            print('3- Voltar para o menu.')

            escolha = input("digite oque deseja calcular:")
            print('=='*13,end='')
            print(' resultado de escolha. ',end='')
            print('=='*25)
            if escolha == '1':
                a = objHexagono.area()
                print(f'Área: {a}')
            elif escolha == '2':
                p = objHexagono.perimetro()
                print(f'Perímetro: {p}')
            elif escolha == '3':
                break
            else: 
                print('Escolha uma opção válida.')
            print('=='*50)
            
    def criar(self):
            print('Escolha uma opção:')
            print('1- Circulo.')
            print('2- Pontos.')
            print('3- Reta.')
            print('4- Triangulo equilátero.')
            print('5- Triangulo isoscéles.')
            print('6- Triangulo escaleno.')
            print('7- Quadrado')
            print('8- Losango')
            print('9- Retângulo.')
            print('10- Pentagono.')
            print('11- Hexagono.')
            print('12- Voltar para o menu.')
            option = input("digite o numero da sua escolha: ")

            print('\n')
            print('=='*50)
            

            if option == '1':
                print('Criando circulo...\n')
                self.tb_circulo()

            elif option == '2':
                print('Criando conjunto de pontos...\n')
                self.tb_pontos()

            elif option =='3':
                print('Criando reta...\n')
                self.tb_reta()

            elif option =='4':
                print('Criando triângulo equilátero...\n')
                self.tb_triang_equila()

            elif option == '5':
                print('Criando triângulo isoscéles...\n')
                self.tb_triang_isos() 
                
            elif option == '6':
                print('Criando triângulo escaleno...\n')
                self.tb_triang_esca() 
            
            elif option =='7':
                print('Criando quadrado...\n')
                self.tb_quadrado()

            elif option =='8':
                print('Criando losango...\n')
                self.tb_losango()

            elif option =='9':
                print('Criando retângulo...\n')
                self.tb_retangulo()
            elif option =='10':
                print('Criando pentagono...\n')
                self.tb_pentagono()
                
            elif option =='11':
                print('Criando hexagono...')
                self.tb_hexagono()

            elif option =='12':
                print("voltando para o menu principal...\n")
            else:
                print('digite uma opção válida.')
                print('=='*50)


    def run(self):
        while(True):
            print('Escolha uma opção:')
            print('1- Criar forma geométrica.')
            print('2- Verificar formas geométricas.')
            print('3- Sair.')
            escolha = input("digite o numero da sua escolha: ")
            print('\n')
            print('=='*50)
            if escolha == '1':
                self.criar()
            elif escolha == '2':
                self.crash()
            elif escolha == '3':
                print('encerrando sistema.')
                break
            else:
                print('digite uma opção válida.')
                print('=='*50)


from math import pi,cos,tan,sin,radians

class Ponto:
    def __init__(self,n):
        self.n = n
        self.temp = []
    def coordenada(self):
        coo_ponto = []
        for i in range(0,self.n):
            while True:
                try:
                    X = float(input(f"digite a coordenada de X{i}: "))
                    Y = float(input(f"digite a coordenada de Y{i}: "))
                    v=[]
                    v.append(X)
                    v.append(Y)
                    coo_ponto.append(v)
                    break
                except ValueError:
                    print('Entrada inválida. Digite apenas números do tipo flutuante.')
        self.temp = coo_ponto
        return coo_ponto

    def retornarPontosX(self, p):
        self.p = p
        v_x = {}
        for i in range(0,self.n):
            v_x[f'X{i}'] = self.p[i][0]
        return v_x

    def retornarPontosY(self, p): 
        self.p = p
        v_y = {}
        for i in range(0,self.n):
            v_y[f'Y{i}'] = self.p[i][1]
        return(v_y)
    
    def setPontosY(self,p):
        self.p = p
        for i in range(0,self.n):
            while True:
                try:
                    nY = float(input(f'digite o novo valor de Y{i}: '))
                    break
                except ValueError:
                    print('digite um valor do tipo flutuante.')
            p[i].pop()
            p[i].append(nY)

    def setPontosX(self,p):
        self.p = p
        for i in range(0,self.n):
            while True:
                try:
                    nX = float(input(f'digite o novo valor de X{i}: '))
                    break
                except ValueError:
                    print('digite um valor do tipo flutuante.')
            p[i].pop(0)
            p[i].insert(0,nX)

    def detalhes(self):
            for num in range(0,self.n):
                print(f"ponto {num+1} - coordenada: {self.temp[num]}")

    def identificador(self):
        return '_ponto'

class Reta: 
    def __init__(self,n):
        self.n = n
        self.objPonto = Ponto(n) #composição
        self.coo = self.objPonto.coordenada()
        self.b = 0
    def inclinacao(self):
        if len(self.coo) >=2:
            deltaX = self.coo[1][0]-self.coo[0][0]
            deltaY = self.coo[1][1]-self.coo[0][1]
            if deltaX != 0:
                inclina = deltaY/deltaX
                return inclina
            else:
                return 'delta X é igual 0, tente outro caso.'
            
        elif len(self.coo) == 1:
            inclina = self.coo[0][1]/self.coo[0][0]
            return inclina

    def distancia(self):
        distancia = ((self.coo[self.n-1][1]-self.coo[0][1])**2+(self.coo[self.n-1][0]-self.coo[0][0])**2)**0.5
        return distancia

    def primeiroPonto(self):
        ponto1 = [self.coo[0][0] , self.coo[0][1]]
        return ponto1

    def ultimoPonto(self):
        pontoN = [self.coo[self.n-1][0], self.coo[self.n-1][1]]
        return pontoN

    def coefLinear(self,m): #m é o coeficiente angular q vem de inclinação, portanto ele tem uma ASSOCIAÇÃO
        self.m = m
        if type(self.m) == float:
            b = self.coo[0][1] - self.coo[0][0]* self.m
            self.b = b
            return b
        else:
            return "delta X é igual 0, tente outro caso."

    def montarTabela(self,m,b,i): #assosiação    self-association
        print(f"__TABELA__\n  X | Y  ")
        for x in range(0,i):
            y = m*x + b
            print(f"  {x} | {y}  ")

    def interpolar(self,m,b,x): #associação   self-association
        y = m*x+b
        return y
    
    def verificar_interferencia(self,x_p, y_p):
        m = self.inclinacao()
        b = self.coefLinear(m)
        
        if y_p == m * x_p + b:
            print('este ponto interfere com está reta.')
        else:
            print('este ponto não interfere com está reta.')

    def detalhes(self):
        d = self.distancia()
        m = self.inclinacao()
        b = self.b
        print(f'\nquantidade de pontos para a reta: {self.n}\ndistância do segmento de reta: {d}\ninclinação da reta: {m}\ncoeficiente linear: {b}')
    
    def identificador(self):
        return '_reta'
    
class Coo_unica: #classe auxiliar  que retorna x ou y, serve para exemplo prático e simples de associação com circulo que precisa de um ponto somente
    def __init__(self,x,y):
        self.__x = x
        self.__y = y
        
    @property #quando chamado usa-se: exemplo = coo_unica.getX      sem os parenteses, pois agr o método é chamado como um atributo.
    def getX(self):
        return self.__x
    
    @property
    def getY(self):  #get para pegar um atributo privado.
        return self.__y

    def distancia_origem(self):
        distancia = ((self.__x)**2+(self._y)**2)**0.5
        return distancia
    
    def identificador(self):
        return '_coordenada_unica'

class Circulo: 
    def __init__(self,x,y,r):
        self.x = x
        self.y = y
        self.r = r

    def circunferencia(self):
        C = 2*pi*self.r 
        return C

    def diametro(self):
        D = 2*self.r
        return D

    def areaCirculo(self):
        A = pi*(self.r**2)
        return A
    
    def verificar_interferencia(self,x_p, y_p):
        distancia = ((self.x - x_p)**2 + (self.y - y_p)**2)**0.5 #distância do ponto pra origem.
        if distancia <= self.r:
            print('este ponto está contido neste círculo.')
        else:
            print('este ponto não está contido neste círculo.')
    
    def detalhes(self):
        c= self.circunferencia()
        d = self.diametro()
        a = self.areaCirculo()
        print(f'\nraio: {self.r}\ncircunferência: {c}\ndiametro: {d}\nárea: {a}\ncentro: ({self.x},{self.y})')
        
    def identificador(self):
        return '_circulo'

class TriangEquilatero:
    #todos lados iguais
    def __init__(self,a,b,c,x,y):
        self.a = a 
        self.b = b
        self.c = c
        self.x = x
        self.y = y
    
    def _verificarTriangulo(self): #tem como imprimir no testbench e ser usada na filha
        if(self.a + self.b) > self.c and (self.a + self.c) > self.b and (self.b + self.c) > self.a:
            return True
        else:
            return False

    def _verificarLados(self):
        if self.a == self.b == self.c:
            return True
        else:
            return False

    def altura(self):
        verificarTriang = self._verificarTriangulo()
        verificarLado = self._verificarLados()
        perimetro = self.perimetro()
        if verificarTriang == True and verificarLado == True and type(perimetro) == float :
            semiP = perimetro/2
            h = (2/self.a)*(semiP*(semiP-self.a)*(semiP-self.b)*(semiP-self.c))**0.5
            return h
        else:
            return "as entradas não são válidas."

    def area(self):
        verificarTriang = self._verificarTriangulo()
        verificarLado = self._verificarLados()
        perimetro = self.perimetro()
        if verificarTriang == True and verificarLado == True:
            s = perimetro/2
            A = (s*(s-self.a)*(s-self.b)*(s-self.c))**0.5 #fórmula de Heron
            return A
        else:
            return "as entradas não são válidas."

    def perimetro(self): # será utilizado no isosceles através de herança.
        verificarTriang = self._verificarTriangulo()
        verificarLados = self._verificarLados()
        if verificarTriang == True and verificarLados == True:
            P = self.a+self.b+self.c #é a soma dos lados, só q como a=b=c, pode ser feito a*3, ao inves de a+b+c.
            return P
        else:
            return "as entradas não são válidas."
    
    def _area_aux(self, ponto1,ponto2,ponto3):
        area = abs(0.5*(ponto1.getX*(ponto2.getY-ponto3.getY) + 
                        ponto2.getX*(ponto3.getY-ponto1.getY) + 
                        ponto3.getX*(ponto1.getY-ponto2.getY)))
        return area
    
    def verificar_interferencia(self,x_p, y_p):
        h = self.altura()
        pontos = { 'ponto1':[self.x,self.y+h/2], 'ponto2':[self.x-self.c/2,self.y-h/2], 'ponto3':[self.x+self.c/2,self.y-h/2]}
        
        ponto1 = Coo_unica(pontos['ponto1'][0],pontos['ponto1'][1])
        ponto2 = Coo_unica(pontos['ponto2'][0],pontos['ponto2'][1])
        ponto3 = Coo_unica(pontos['ponto3'][0],pontos['ponto3'][1])
        pontoN = Coo_unica(x_p,y_p)
        
        area1 = self._area_aux(ponto1, ponto2,pontoN)
        area2 = self._area_aux(ponto2,ponto3,pontoN)
        area3 = self._area_aux(ponto1,ponto3,pontoN)
        areatotal = self._area_aux(ponto1,ponto2,ponto3)
        if area1 + area2 + area3 == areatotal:
            print('este ponto está contido neste triângulo.')
        else:
            print('este ponto não está contido neste triângulo.')

    def detalhes(self):
        a = self.area()
        p = self.perimetro()
        h = self.altura()
        print(f'\nlados: A:{self.a} ; B:{self.b} ; C:{self.c}\nárea: {a}\nperímetro: {p}\naltura: {h}\ncentro: ({self.x},{self.y})')
        
    def identificador(self):
        return '_triangulo_equilatero'

class TriangEscaleno(TriangEquilatero): #neta(mãe) # lados diferentes
    def __init__(self,a,b,c,x,y):
        super().__init__(a,b,c,x,y)

    def _verificarLados(self): #encapsulamento de método, não tem como imprimir no testbench e não tem como usar na filha 
        if self.a != self.b and self.c != self.b and self.c != self.a:
            return True
        else: 
            return False
        
    def __menorAngulo(self):
        m = min(self.a,self.b,self.c) #achar angulo, para assim conseguir achar a altura, e com h achar a area. h= c*sen(teta), a = h*b/2
        aux = 180/(self.a + self.b + self.c)
        menorTeta = aux*m
        return menorTeta
        
    def __maiorAngulo(self):
        m = max(self.a,self.b,self.c)
        aux = 180/(self.a + self.b + self.c)
        maiorTeta = aux*m
        return maiorTeta
    
    def angulosInternos(self):
        verificarTriang = self._verificarTriangulo()
        verificarLados = self._verificarLados()

        if verificarTriang == True and verificarLados == True:
            menorTeta = self.__menorAngulo()
            maiorTeta = self.__maiorAngulo()
            TetaMeio = 180 - menorTeta - maiorTeta
            print(f"{maiorTeta} graus, {menorTeta} graus, {TetaMeio} graus")
        else: 
            print("as entradas não são válidas aqui.")
    
    def identificador(self):
        return '_triangulo_escaleno'

class TriangIsosceles(TriangEscaleno, TriangEquilatero): #filho(mae1,mae2) #herança multipla
    # dois lados iguais

    def __init__(self,a,b,c,x,y):
        super().__init__(a,b,c,x,y)

    def _verificarLados(self): #polimorfismo
        if self.a == self.b and self.c != self.a:
            return True
        if self.a == self.c and self.b != self.a:
            return True
        if self.c == self.b and self.c != self.a:
            return True
        else: 
            return False
    
    def identificador(self):
        return '_triangulo_isosceles'

class Quadrado:
    def __init__(self, l,x,y):
        self._l = l #encapsulamento de atríbuto, privado
        self.x = x
        self.y = y
    def diagonal(self):
        d = self._l * 2**0.5
        return d
    
    def verificar_interferencia(self,x_p,y_p):
        pontos = {'ponto1':[self.x-self._l/2,self.y+self._l/2], 'ponto2': [self.x+self._l/2, self.y+self._l/2],
                'ponto3':[self.x-self._l/2,self.y-self._l/2], 'ponto4':[self.x + self._l/2, self.y - self._l/2]}
        
        print(pontos)
        if pontos['ponto1'][0] < x_p <= pontos['ponto4'][0] and pontos['ponto4'][1] <= y_p <= pontos['ponto1'][1]:
            print('este ponto está contido neste quadrado.')
            
        else:
            print('este ponto não está contido neste quadrado.')
        
    def area(self):
        A = self._l**2
        return A
    
    def perimetro(self):
        p = self._l*4
        return p
    
    def getLado(self):
        return self._l #get para acessar o atríbuto privado
    
    def detalhes(self):
        d = self.diagonal()
        a = self.area()
        p = self.perimetro()
        print(f'\nlado: {self._l}\ndiagonal: {d}\nárea: {a}\nperímetro: {p}\ncentro: ({self.x},{self.y})')
        
    def identificador(self):
        return '_quadrado'

class Losango(Quadrado): #herança

    def __init__(self,l,dMaior,dMenor,x ,y ):
        self.dMaior = dMaior
        self.dMenor = dMenor
        super().__init__(l,x,y)

    def area(self):
        A = (self.dMaior * self.dMenor)/2
        return A

    def verificar_interferencia(self,x_p,y_p): #polimorfismo
        pontos = {
                'ponto1': [self.x , self.y+self.dMaior/2],
                'ponto2':[self.x + self.dMenor/2,self.y],
                'ponto3':[self.x, self.y-self.dMaior/2],
                'ponto4':[self.x-self.dMenor/2,self.y]
                }
        if pontos['ponto4'][0] <= x_p <= pontos['ponto2'][0] and pontos['ponto3'][1] <= y_p <= pontos['ponto1'][1]:
            print('este ponto está contido neste losango.')
        else:
            print('este ponto não está contido neste losango.')
    
    def detalhes(self):
        dMa = self.dMaior
        dMe = self.dMenor
        a = self.area()
        p = self.perimetro()
        print(f'\nlado: {self._l}\ndiagonal maior: {dMa}\ndiagonal menor: {dMe}\nárea: {a}\nperímetro: {p}\ncentro: ({self.x},{self.y})')
        
    def identificador(self):
        return '_losango'

class Retangulo:
    def __init__(self, a,b,x,y):
        self.a = a
        self.b = b
        self.x = x
        self.y = y

    def __verificarRetangulo(self): #encapsulamento
        if self.a != self.b:
            return True
        else:
            return False
        
    def perimetro(self):
        flag = self.__verificarRetangulo() #encapsulamento de método
        if flag == True:
            p = self.a*2 + self.b*2
            return p
        else:
            return "as entradas não são válidas aqui."
        
    def area(self):
        flag = self.__verificarRetangulo()
        if flag == True:
            A = self.a*self.b
            return A
        else:
            return "as entradas não são válidas aqui."
        
    def diagonal(self):
        d = (self.a**2 + self.b**2)**0.5    
        return d
    
    def verificar_interferencia(self,x_p,y_p):
        pontos = {
            'ponto1':[self.x-self.a/2,self.y+self.b/2],'ponto2':[self.x+self.a/2,self.y+self.b/2],
            'ponto3':[self.x-self.a/2,self.y-self.b/2], 'ponto4':[self.x+self.a/2, self.y-self.b/2]
                }
        if pontos['ponto1'][0]<= x_p <= pontos['ponto4'][0] and pontos['ponto3'][1] <= y_p <= pontos['ponto2'][1]:
            print('este ponto está contido neste retangulo.')
        else:
            print('este ponto não está contido neste losango.')

    def detalhes(self):
        d = self.diagonal()
        A = self.area()
        p = self.perimetro()
        print(f'\nlargura: {self.b}\naltura: {self.b}\ndiagonal: {d}\nárea: {A}\nperímetro: {p}\ncentro: ({self.x},{self.y})')
        
    def identificador(self):
        return '_retangulo'

from abc import ABC, abstractmethod 

class Poligono(ABC): 
    #class abstrata que será modelo referência para os poligonos: pentagono, hexagono...
    @abstractmethod
    def area(self):
        pass

    def perimetro(self):
        p = self.i*self.a
        return p
    
    def identificador(self):
        return '_poligono'

    def _area_aux(self, ponto1,ponto2,ponto3):
        area = abs(0.5*(ponto1.getX*(ponto2.getY-ponto3.getY) + 
                        ponto2.getX*(ponto3.getY-ponto1.getY) + 
                        ponto3.getX*(ponto1.getY-ponto2.getY)))
        return area
    
class Pentagono(Poligono): #herança com classe abstrata, filho 1
    def __init__(self,a,x,y):
        self.a = a
        self.i = 5

    def area(self): #polimorfismo
        apotema = self.a / (2 * tan(pi / 5))
        
        # Calcular a área
        area = (5 / 2) * self.a * apotema
        return area


    def raio(self):
        sen = sin(pi/self.i)
        R = self.a/(2*sen)
        return R

    def verificar_interferencia(self, x_p, y_p):
        R = self.raio()
        pontos = {
            'ponto1': [self.x + R*cos(0), self.y + R*sin(0)], 
            'ponto2': [self.x + R*cos(2*pi/self.i), self.y + R*sin(2*pi/self.i)],
            'ponto3': [self.x + R*cos(4*pi/self.i), self.y + R*sin(4*pi/self.i)],
            'ponto4': [self.x + R*cos(6*pi/self.i), self.y + R*sin(6*pi/self.i)],
            'ponto5': [self.x + R*cos(8*pi/self.i), self.y + R*sin(8*pi/self.i)]
        }
        ponto1 = Coo_unica(pontos['ponto1'][0], pontos['ponto2'][1])
        ponto2 = Coo_unica(pontos['ponto2'][0], pontos['ponto2'][1])
        ponto3 = Coo_unica(pontos['ponto3'][0], pontos['ponto3'][1])
        ponto4 = Coo_unica(pontos['ponto4'][0], pontos['ponto4'][1])
        ponto5 = Coo_unica(pontos['ponto5'][0], pontos['ponto5'][1])
        pontoN = Coo_unica(x_p,y_p)
        
        areaN1 = self._area_aux(ponto1,ponto2,pontoN)
        areaN2 = self._area_aux(ponto2,ponto3,pontoN)
        areaN3 = self._area_aux(ponto3,ponto4,pontoN)
        areaN4 = self._area_aux(ponto4,ponto5,pontoN)
        areaN5 = self._area_aux(ponto5,ponto1,pontoN)

        area = self.area()
        sumAreaN = areaN1 + areaN2 + areaN3 + areaN4 + areaN5
        if area == sumAreaN:
            print('este ponto está contido neste retangulo.')
        else:
            print('este ponto não está contido neste retangulo.')

    def detalhes(self):
        p = self.perimetro()
        A = self.area()
        r = self.raio()
        print(f'\nlado: {self.a}\nraio: {r}\nárea: {A}\nperímetro: {p}\ncentro: ({self.x},{self.y})')

    def identificador(self):
        return '_pentagono'

class Hexagono(Poligono): #herança com classe abstrata, filho 2
    def __init__(self,a,x,y):
        self.a = a
        self.x = x
        self.y = y
        self.i = 6

    def area(self): #polimorfismo
        A = ((3*self.a**2)*3**0.5)/2
        return A
    
    def verificar_interferencia(self, x_p, y_p):
        l = self.x + self.y
        pontos = {
                'ponto1':[self.x+l * cos(0),self.y+l * sin(0)],
                'ponto2': [self.x+l * cos(pi/3),self.y+l * sin(pi/3)],
                'ponto3': [self.x+l * cos(2*pi/3),self.y+l * sin(2*pi/3)],
                'ponto4': [self.x+l * cos(pi),self.y+l * sin(pi)],
                'ponto5': [self.x+l * cos(4*pi/3),self.y+l * sin(4*pi/3)],
                'ponto6': [self.x+l * cos(5*pi/3),self.y+l * sin(5*pi/3)],
        }
        
        ponto1 = Coo_unica(pontos['ponto1'][0], pontos['ponto1'][1])
        ponto2 = Coo_unica(pontos['ponto2'][0], pontos['ponto2'][1])
        ponto3 = Coo_unica(pontos['ponto3'][0], pontos['ponto3'][1])
        ponto4 = Coo_unica(pontos['ponto4'][0], pontos['ponto4'][1])
        ponto5 = Coo_unica(pontos['ponto5'][0], pontos['ponto5'][1])
        ponto6 = Coo_unica(pontos['ponto6'][0], pontos['ponto6'][1])
        pontoN = Coo_unica(x_p,y_p)

        areaN1 = self._area_aux(ponto1,ponto2,pontoN)
        areaN2 = self._area_aux(ponto2,ponto3,pontoN)
        areaN3 = self._area_aux(ponto3,ponto4,pontoN)
        areaN4 = self._area_aux(ponto4,ponto5,pontoN)
        areaN5 = self._area_aux(ponto5,ponto6,pontoN)
        areaN6 = self._area_aux(ponto6,ponto1,pontoN)
        
        
        areaTotal = self.area()
        sumAreaN = areaN1 + areaN2 + areaN3 + areaN4 + areaN5 + areaN6
        if areaTotal == sumAreaN:
            print('este ponto está contido neste hexágono.')
        else:
            print('este ponto não está contido neste hexágono.')

    def detalhes(self):
        p = self.perimetro()
        A = self.area()
        print(f'\nlado: {self.a}\nárea: {A}\nperímetro: {p}\ncentro: ({self.x},{self.y})')


    def identificador(self):
        return '_hexagono'

class TrapezioIsosceles:
    def __init__(self,bMenor, bMaior, _h):
        self.bMaior = bMaior
        self._h = _h #encapsulamento de atríbuto, protegido.
        self.bMenor = bMenor

    def area(self):
        A = ((self.bMenor + self.bMaior)*self._h)/2
        return A
    
    def __lado(self): #não tem como retornar nada no testbench, só serve neste escopo.
        aux = (self.bMaior - self.bMenor)/2
        l = (self._h**2 + aux**2)**0.5
        return l
    
    def perimetro(self):
        lado = self.__lado()
        p = lado*2 + self.bMenor + self.bMaior
        return p
    
    def getAltura(self):
        return self._h

    def identificador(self):
        return '_trapezio_isosceles'
    
class TrapezioRetangulo(TrapezioIsosceles): #herança
    #filho não precisa do construtor, pois o construtor dele é o mesmo da mãe
    def __lado(self): 
        aux = self.bMaior - self.bMenor
        l = (aux**2 + self._h**2)**0.5
        return l
    
    def perimetro(self): #polimorfismo
        lado = self.__lado()
        p = self.bMaior + self.bMenor + lado + self._h
        return p

    def identificador(self):
        return '_trapezio_retangulo'
    
# todo mudanças feitas:
#exclusão do metodo cor da class ponto.
#arquivos testbenches de ponto e de quadrado devem ser refeitos.
#colocar tudo pro primeiro quadrante
#adicionar property e outros ngcs desses ai
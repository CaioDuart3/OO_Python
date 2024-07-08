
class Ponto:
    def __init__(self,n):
        self.n = n

    def cor(self):
        cor_ponto=[]
        for i in range(0,self.n):
            cor = str(input(f"escolha a cor do seu ponto {i}: "))
            cor_ponto.append(cor)
        return cor_ponto

    def coordenada(self):
        coo_ponto = []
        for i in range(0,self.n):
            X = float(input(f"digite a coordenada de X{i}: "))
            Y = float(input(f"digite a coordenada de Y{i}: "))
            v=[]
            v.append(X)
            v.append(Y)
            coo_ponto.append(v)
        return coo_ponto

    def retornarPontosX(self, p):
        self.p = p
        v_x = {}
        for i in range(0,self.n):
            v_x[f'X{i}'] = self.p[i][0]
        return v_x

    def retornarPontosY(self,p): 
        self.p = p
        v_y = {}
        for i in range(0,self.n):
            v_y[f'Y{i}'] = self.p[i][1]
        return(v_y)

    def setPontosY(self,p):
        self.p = p
        for i in range(0,self.n):
            nY = float(input(f'digite o novo valor de Y{i}: '))
            p[i].pop()
            p[i].append(nY)

    def setPontosX(self,p):
        self.p = p
        for i in range(0,self.n):
            nY = float(input(f'digite o novo valor de X{i}: '))
            p[i].pop(0)
            p[i].insert(0,nY)

    def exibirPonto(self, p,c): #c é o vetor das cores
            # o vetor p, a ser recebido tem que ser um vetor de listas, com pontos x e y; vetores só de x ou só de y, não funcionam.
            num = int(input(f"dados os pontos: {p}\n digite a index do ponto que você quer consultar as informações: ")) 
            print(f"vetor solicitado: {p[num]}\ncor: {c[num]}")
    
    def identificador(self):
        return '_ponto'

class Reta: 

    def __init__(self,n):
        self.n = n
        self.objPonto = Ponto(n) #composição
        self.coo = self.objPonto.coordenada()

    def inclinacao(self):
        if len(self.coo) >=2:
            deltaX = self.coo[1][0]-self.coo[0][0]
            deltaY = self.coo[1][1]-self.coo[0][1]
            if deltaX >0:
                inclina = deltaY/deltaX
                return inclina
            else:
                return 'delta X é igual 0, tente outro caso.'
            
        elif len(self.coo) == 1:
            inclina = self.coo[0][1]/self.coo[0][0]
            return inclina

    def coefLinear(self,m): #m é o coeficiente angular q vem de inclinação, portanto ele tem uma ASSOCIAÇÃO
        self.m = m
        if type(self.m) == float:
            b = self.coo[0][1] - self.coo[0][0]* self.m
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
    
    def identificador(self):
        return '_reta'

class Coo_unica: #classe auxiliar  que retorna x ou y, serve para exemplo prático e simples de associação com circulo que precisa de um ponto somente
    def __init__(self,x,y):
        self.__x = x
        self.__y = y
    def coordenadaX(self):
        return self.__x
    
    def coordenadaY(self):  #get para pegar um atributo privado.
        return self.__y

class Circulo: 
    def __init__(self,x,y,r):
        self.x = x
        self.y = y
        self.r = r

    def circunferencia(self):
        C = 2*3.1415926535*self.r 
        return C

    def diametro(self):
        D = 2*self.r
        return D

    def areaCirculo(self):
        A = 3.1415926535*(self.r**2)
        return A

    def Perimetro(self, teta,C):
        P = (teta/(2*3.1415926535))*C
        return P

    def identificador(self):
        return '_circulo'

class TriangEquilatero:
    #todos lados iguais
    def __init__(self,a,b,c):
        self.a = a 
        self.b = b
        self.c = c
    
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
            return "as entradas não são válidas aqui."

    def area(self):
        verificarTriang = self._verificarTriangulo()
        verificarLado = self._verificarLados()
        perimetro = self.perimetro()
        if verificarTriang == True and verificarLado == True:
            A = (perimetro*(perimetro-self.a)*(perimetro-self.b)*(perimetro-self.c))**0.5 #fórmula de Heron
            return A
        else:
            return "as entradas não são válidas aqui."

    def perimetro(self): # será utilizado no isosceles através de herança.
        verificarTriang = self._verificarTriangulo()
        verificarLados = self._verificarLados()
        if verificarTriang == True and verificarLados == True:
            P = self.a+self.b+self.c #é a soma dos lados, só q como a=b=c, pode ser feito a*3, ao inves de a+b+c.
            return P
        else:
            return "as entradas não são válidas aqui."
    
    def identificador(self):
        return '_triangulo_equilatero'
import math

class TriangEscaleno(TriangEquilatero): #neta(mãe) # lados diferentes
    def __init__(self,a,b,c):
        super().__init__(a,b,c)

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

    def __init__(self,a,b,c):
        super().__init__(a,b,c)

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
    def __init__(self, __l):
        self.__l = __l #encapsulamento de atríbuto, privado

    def diagonal(self):
        d = self.__l * 2**0.5
        return d
    
    def area(self):
        A = self.__l**2
        return A
    
    def perimetro(self):
        p = self.__l*4
        return p
    
    def getLado(self):
        return self.__l #get para acessar o atríbuto privado
    
    def identificador(self):
        return '_quadrado'

class Losango(Quadrado): #herança
    def __init__(self,__l,dMaior,dMenor):
        self.dMaior = dMaior
        self.dMenor = dMenor
        super().__init__(__l)

    def area(self):
        A = (self.dMaior * self.dMenor)/2
        return A

    def identificador(self):
        return '_losango'
class Retangulo:
    def __init__(self, a,b):
        self.a = a
        self.b = b

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

    def identificador(self):
        return '_retangulo'

from abc import ABC, abstractmethod 

class Poligono(ABC): 
    #class abstrata que será modelo referência para os poligonos: pentagono, hexagono...
    def __init__(self,a):
        self.a = a
    @abstractmethod

    def area(self):
        pass

    def perimetro(self):
        p = self.i*self.a
        return p

    def identificador(self):
        return '_poligono'

class Pentagono(Poligono): #herança com classe abstrata, filho 1
    def __init__(self,a):
        super().__init__(a)
        self.i = 5

    def area(self): #polimorfismo
        aux = math.tan(36)
        A = (5*self.a**2)/(4*aux)
        return A

    def identificador(self):
        return '_pentagono'

class Hexagono(Poligono): #herança com classe abstrata, filho 2
    def __init__(self,a):
        super().__init__(a)
        self.i = 6

    def area(self): #polimorfismo
        A = ((3*self.a**2)*3**0.5)/2
        return A

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
    
class FigurasGeometricas: #AGREGAÇÃO, pois vai possuir formas geometricas 
    def __init__(self):
        self.formas = {}
        self.count = 0
    
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
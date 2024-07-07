
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
            X = int(input(f"digite a coordenada de X{i}: "))
            Y = int(input(f"digite a coordenada de Y{i}: "))
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

    def retornarPontosY(self,p): #associação
        self.p = p
        v_y = {}
        for i in range(0,self.n):
            v_y[f'Y{i}'] = self.p[i][1]
        return(v_y)

    def setPontosY(self,p):
        self.p = p
        for i in range(0,self.n):
            nY = int(input(f'digite o novo valor de Y{i}: '))
            p[i].pop()
            p[i].append(nY)

    def setPontosX(self,p):
        self.p = p
        for i in range(0,self.n):
            nY = int(input(f'digite o novo valor de X{i}: '))
            p[i].pop(0)
            p[i].insert(0,nY)

    def retornarPonto(self, p,c): #c é o vetor das cores
            # o vetor p, a ser recebido tem que ser um vetor de listas, com pontos x e y; vetores só de x ou só de y, não funcionam.
            num = int(input(f"dados os pontos: {p}\n digite a index do ponto que você quer consultar as informações: ")) 
            print(f"vetor solicitado: {p[num]}\ncor: {c[num]}")

class Reta: 

    def __init__(self,n):
        self.n = n
        self.objPonto = Ponto(n) #composição
        self.coo = self.objPonto.coordenada()

    def inclinacao(self):
        if len(self.coo) >=2:
            deltaX = self.coo[1][0]-self.coo[0][0]
            deltaY = self.coo[1][1]-self.coo[0][1]
            inclina = deltaY/deltaX
            return inclina
        elif len(self.coo) == 1:
            inclina = self.coo[0][1]/self.coo[0][0]
            return inclina

    def CoefLinear(self,m): #m é o coeficiente angular q vem de inclinação, portanto ele tem uma ASSOCIAÇÃO
        self.m = m
        b = self.coo[0][1] - self.coo[0][0]* self.m
        return b

    def montarTabela(self,m,b,i):
        print(f"__TABELA__\n  X | Y  ")
        for x in range(0,i):
            y = m*x + b
            print(f"  {x} | {y}  ")
    def interpolar(self,m,b,x):
        y = m*x+b
        return y

class coo_circulo: #classe auxiliar  que retorna x ou y, serve para exemplo prático e simples de associação com circulo que precisa de um ponto somente
    def __init__(self):
        self.x = input("digite a coordenada x: ")
        self.y = input("digite a coordenada y: ")
    def coordenadaX(self):
        return self.x
    def coordenadaY(self):
        return self.y

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

    def set(self):
        self.x = int(input("digite o novo valor de X: "))
        self.y = int(input("digite o novo valor de Y: "))

class TriangEquilatero: #triangulo Triangulo_Equilatero
    #todos lados iguais
    def __init__(self,a,b,c):
        self.a = a 
        self.b = b
        self.c = c
    
    def _verificarTriangulo(self): #tem como imprimir no testbench e ser usada na filha
        aux = False
        if(self.a + self.b) > self.c and (self.a + self.c) > self.b and (self.b + self.c) > self.a:
            aux = True
            return aux
        else:
            return aux

    def _verificarLados(self):
        aux = False
        if self.a == self.b == self.c:
            aux = True
            return aux
        else:
            return aux

    def altura(self):
        verificarTriang = self._verificarTriangulo()
        verificarLado = self._verificarLados()
        if verificarTriang == True and verificarLado == True:
            if self.a == self.b:
                h = ((self.c/2)**2 +  self.a**2)**0.5
                return h
            elif self.a == self.c:
                h = ((self.b/2)**2 +  self.a**2)**0.5
                return h
            elif self.b == self.c:
                h = ((self.a/2)**2 +  self.b**2)**0.5
                return h
        else:
            return "as entradas não são válidas aqui."

    def area(self):
        verificarTriang = self._verificarTriangulo()
        verificarLado = self._verificarLados()
        if verificarTriang == True and verificarLado:
            if self.a == self.b and self.b == self.c:
                A = ((self.a**2)*(3**0.5))/4
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
        
class TriangIsosceles(TriangEquilatero): #filho(mae) #herança, primeiro filho
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
        
    def _altura(self):
        verificarTriang = self._verificarTriangulo() #encapsulamento válido da mãe pra usar no filho, se fosse privado não daria certo.
        verificarLados = self._verificarLados()
        if verificarTriang == True and verificarLados == True:
            if self.a == self.b:
                h = (self.a**2 - (self.c**2)/4)**0.5
                return h
            elif self.a == self.c:
                h = (self.a**2 - (self.b**2)/4)**0.5
                return h
            elif self.b == self.c:
                h = (self.b**2 - (self.a**2)/4)**0.5
                return h
        else:
            return "as entradas não são válidas aqui."

    def _base(self):
        verificarTriang = self._verificarTriangulo()
        verificarLados = self._verificarLados()
        if verificarTriang == True and verificarLados == True:
            if self.a == self.b:
                return self.c
            elif self.a == self.c:
                return self.b
            elif self.b == self.c:
                return self.a
        else:
            return "as entradas não são válidas aqui."

    def area(self): #polimorfismo
        verificarTriang = self._verificarTriangulo()
        verificarLados = self._verificarLados()
        if verificarTriang == True and verificarLados == True:
            h = self._altura()
            base =  self._base()
            A = (base*h)/2
            return A
        else:
            return "as entradas não são válidas aqui."

import math

class TriangEscaleno: # lados diferentes
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def __verificarDiferenca(self): #encapsulamento de método, não tem como imprimir no testbench e não tem como usar na filha 
        aux = False
        if self.a + self.b > self.c and self.b + self.c > self.a and self.c + self.a > self.b:
            if self.a != self.b and self.b != self.c and self.a != self.c:
                aux = True
                return aux
            else:
                return aux
        else: 
            return aux
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
        menorTeta = self.__menorAngulo()
        maiorTeta = self.__maiorAngulo()
        TetaMeio = 180 - menorTeta - maiorTeta
        print(f"{maiorTeta}, {menorTeta},{TetaMeio}")

    def _altura(self): #polimorfismo sobrescreve a informação do método da mãe
        verificador = self.__verificarDiferenca()
        if verificador == True:
            a = self.__menorAngulo()
            aux = math.sin(a)
            h = self.c*aux
            return h
        else:
            return "as entradas não são válidas"

    def area(self):
        verificador = self.__verificarDiferenca()
        if verificador == True:
            h =  self._altura()
            A = (self.c * h)/2
            return A
        else:
            return "as entradas não são válidas aqui."

    def perimetro(self):
        verificador = self.__verificarDiferenca()
        if verificador == True:
            p = self.a + self.b + self.c
            return p
        else: 
            return "as entradas não são válidas aqui."

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

class Losango(Quadrado): #herança
    def __init__(self,__l,dMaior,dMenor):
        self.dMaior = dMaior
        self.dMenor = dMenor
        super().__init__(__l)
    def area(self):
        A = (self.dMaior * self.dMenor)/2
        return A

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
            print("as entradas não são válidas aqui.")
    def area(self):
        flag = self.__verificarRetangulo()
        if flag == True:
            A = self.a*self.b
            return A
        else:
            print("as entradas não são válidas aqui.")
    def diagonal(self):
        d = (self.a**2 + self.b**2)**0.5    
        return d

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

class Pentagono(Poligono): #herança com classe abstrata
    def __init__(self,a):
        super().__init__(a)
        self.i = 5
    def area(self):
        aux = math.tan(36)
        A = (5*self.a**2)/(4*aux)
        return A

class Hexagono(Poligono): #herança com classe abstrata
    def __init__(self,a):
        super().__init__(a)
        self.i = 6
    def area(self):
        A = ((3*self.a**2)*3**0.5)/2
        return A

class TrapezioIsosceles:
    def __init__(self,b, B, _h):
        self.B = B
        self._h = _h #encapsulamento de atríbuto, protegido.
        self.b = b
    def area(self):
        A = ((self.b + self.B)*self._h)/2
        return A
    def __lado(self): #não tem como retornar nada no testbench, só serve neste escopo.
        aux = (self.B - self.b)/2
        l = (self._h**2 + aux**2)**0.5
        return l
    def perimetro(self):
        lado = self.__lado()
        p = lado*2 + self.b + self.B
        return p
    def getAltura(self):
        return self._h

class TrapezioRetangulo(TrapezioIsosceles): #herança
    #filho não precisa do construtor, pois o construtor dele é o mesmo da mãe
    def __lado(self): 
        aux = self.B - self.b
        l = (aux**2 + self._h**2)**0.5
        return l
    def perimetro(self):
        lado = self.__lado()
        p = self.B + self.b + lado + self._h
        return p


from package.maths.terms import TriangEquilatero,TriangIsosceles, TriangEscaleno

def workspace():
    a = int(input("digite o valor do lado a: "))
    b = int(input("digite o valor do lado b: "))
    c = int(input("digite o valor do lado c: "))
    # ---EQUILATER0---
    # obj_eq = TriangEquilatero(a,b,c)
    # area = obj_eq.area()
    # print(area)

    # ---ISOSCELES---
    obj_iso = TriangIsosceles(a,b,c)
    area = obj_iso.area()
    print(area)
    p = obj_iso.perimetro()
    print(p)

    # # --ESCALENO
    # obj_es = TriangEscaleno(a,b,c)
    # m = obj_es.maiorAngulo()
    # print(m)
    # area = obj_es.area()
    # p = obj_es.perimetro()
    # print(area)
    # print(p)
workspace()

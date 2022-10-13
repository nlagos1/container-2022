# ------------------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------------------ #
import csv
import calculator as clt

option = []
normal = []
normal2 = []
refrigerado = []
refrigerado2 = []
estanque = []
estanque_inf = []


solido = []
liquido = []
gas = []

n1 = []
r = []
inf = []


# -------------Clases Base---------------- #
# ---------------------------------------- #
class Transporte:

    def __init__(self, cost, storage_t):
        self.cost = cost
        self.storage_t = storage_t

    def mov(self):
        pass

    def cost_t(self):
        pass

    def per_masa(self):
        pass

    def per_tipo(self):
        pass


class Container:
    def __init__(self, idx, nombre, tipo, masa, peso):
        self.idx = idx
        self.nombre = nombre
        self.tipo = tipo
        self.masa = masa
        self.peso = peso
    def made_type(self):
        pass


# ----------------Método----------------- #
# --------------Transporte--------------- #
class Avion(Transporte):
    cost = 1000000
    storage_t = 240000

    def cost_t(self):
        if int(sum(cal2)) < Avion.storage_t:
            return Avion.cost

        else:
            qx = round((int(sum(cal2)) / Avion.storage_t) + 1)
            sx = sum(cal2) - Avion.storage_t
            rx = Avion((Avion.cost*qx), sx)
            return rx.cost

    def mov(self):
        ax = round(float(cal[0]))
        bx = round(float(cal[1]))
        cx = round(float(cal[2]))
        dx = round(float(cal[3]))
        fx = round(float(cal[4]))
        gx = round(float(cal[5]))

        print(f'Cantidad de contenedores:'
              f'' f' Normal {ax},'
              f' Normal Pequeno: {bx}'
              f' Refrigerado: {cx},'
              f' Refrigerado pequeno: {dx},'
              f' Estanque: {fx},'
              f' Estanque para Inflables :{gx}')

    def per_masa(self):
        ax = int(cal3[0])
        bx = int(cal3[1])
        cx = int(cal3[2])

        print(f'Tonelaje por masa:' f' Solido {ax}, Liquido: {bx}, Gas: {cx}')

    def per_tipo(self):
        ax = int(cal4[0])
        bx = int(cal4[1])
        cx = int(cal4[2])

        print(f'Tonelaje por tipo:' f' Solido {ax}, Liquido: {bx}, Gas: {cx}')


class Barco(Transporte):

    contador = 0
    cost = 1000000000
    storage_t = 576000000
    contador += 1

    def cost_t(self):
        if int(sum(cal2)) < Barco.storage_t:
            return Barco.cost

        else:
            qx = round(int(sum(cal2)) / Barco.storage_t)
            sx = sum(cal2) - Barco.storage_t
            rx = Barco((Barco.cost*qx), sx)
            return rx.cost

    def mov(self):
        ax = round(float(cal[0]))
        bx = round(float(cal[1]))
        cx = round(float(cal[2]))
        dx = round(float(cal[3]))
        fx = round(float(cal[4]))
        gx = round(float(cal[5]))

        print(f'Cantidad de contenedores:'
              f'' f' Normal {ax},'
              f' Normal Pequeno: {bx}'
              f' Refrigerado: {cx},'
              f' Refrigerado pequeno: {dx},'
              f' Estanque: {fx},'
              f' Estanque para Inflables :{gx}')

    def per_masa(self):
        ax = int(cal3[0])
        bx = int(cal3[1])
        cx = int(cal3[2])

        print(f'Tonelaje por masa:' f' Solido {ax}, Liquido: {bx}, Gas: {cx}')

    def per_tipo(self):
        ax = int(cal4[0])
        bx = int(cal4[1])
        cx = int(cal4[2])

        print(f'Tonelaje por tipo:' f' Solido {ax}, Liquido: {bx}, Gas: {cx}')


class Camion(Transporte):
    cost = 500000
    storage_t = 24000

    def cost_t(self):
        if int(sum(cal2)) < Camion.storage_t:
            return Camion.cost

        else:
            qx = int(sum(cal2)) / Camion.storage_t
            sx = sum(cal2) - Camion.storage_t
            rx = Camion((Camion.cost*qx), sx)
            return rx.cost

    def mov(self):
        ax = round(float(cal[0]))
        bx = round(float(cal[1]))
        cx = round(float(cal[2]))
        dx = round(float(cal[3]))
        fx = round(float(cal[4]))
        gx = round(float(cal[5]))

        print(f'Cantidad de contenedores:'
              f'' f' Normal {ax},'
              f' Normal Pequeno: {bx}'
              f' Refrigerado: {cx},'
              f' Refrigerado pequeno: {dx},'
              f' Estanque: {fx},'
              f' Estanque para Inflables :{gx}')

    def per_masa(self):
        ax = int(cal3[0])
        bx = int(cal3[1])
        cx = int(cal3[2])

        print(f'Tonelaje por masa:' f' Solido {ax}, Liquido: {bx}, Gas: {cx}')

    def per_tipo(self):
        ax = int(cal4[0])
        bx = int(cal4[1])
        cx = int(cal4[2])

        print(f'Tonelaje por tipo:' f' Solido {ax}, Liquido: {bx}, Gas: {cx}')


class Tren(Transporte):
    cost = 10000000
    storage_t = 6000004

    def cost_t(self):
        if int(sum(cal2)) < Tren.storage_t:
            return Tren.cost

        else:
            qx = int(sum(cal2)) / Tren.storage_t
            sx = sum(cal2) - Tren.storage_t
            rx = Tren((Tren.cost*qx), sx)
            return rx.cost

    def mov(self):
        ax = round(float(cal[0]))
        bx = round(float(cal[1]))
        cx = round(float(cal[2]))
        dx = round(float(cal[3]))
        fx = round(float(cal[4]))
        gx = round(float(cal[5]))

        print(f'Cantidad de contenedores:'
              f'' f' Normal {ax},'
              f' Normal Pequeno: {bx}'
              f' Refrigerado: {cx},'
              f' Refrigerado pequeno: {dx},'
              f' Estanque: {fx},'
              f' Estanque para Inflables :{gx}')

    def per_masa(self):
        ax = int(cal3[0])
        bx = int(cal3[1])
        cx = int(cal3[2])

        print(f'Tonelaje por masa:' f' Solido {ax}, Liquido: {bx}, Gas: {cx}')

    def per_tipo(self):
        ax = int(cal4[0])
        bx = int(cal4[1])
        cx = int(cal4[2])

        print(f'Tonelaje por tipo:' f' Solido {ax}, Liquido: {bx}, Gas: {cx}')


# ---------------Container---------------- #
# -------------------1-------------------- #
class CNormal(Container):
    pass


class CPeque(CNormal):
    pass


# ---------------Container---------------- #
# -------------------2-------------------- #
class RefriP(Container):
    pass


class RefriG(RefriP):
    pass


# ---------------Container---------------- #
# -------------------3-------------------- #
class Estanque(Container):
    pass


class EstanqueI(Estanque):
    pass


# ----------------------------------Creacion de--------------------------------------------------------------- #
# ------------------------------------Objetos----------------------------------------------------------------- #
def made_type_n():
    with open('../ejemplo_lista.csv', 'r') as dato:
        reader = csv.reader(dato)
        header = dato.readline()
        for row in reader:
            if row[2] == 'normal' and row[3] == 'solida':
                clt.normal.append(CNormal(row[0], row[1], row[2], row[3], row[4]))
    return clt.normal


def made_type_np():
    with open('../ejemplo_lista.csv', 'r') as dato:
        reader = csv.reader(dato)
        header = dato.readline()
        for row in reader:
            if row[2] == 'normal' and row[3] == 'solida':
                clt.normal2.append(CPeque(row[0], row[1], row[2], row[3], row[4]))

    return clt.normal2


def made_type_rg():
    with open('../ejemplo_lista.csv', 'r') as dato:
        reader = csv.reader(dato)
        header = dato.readline()
        for row in reader:
            if row[2] == 'refrigerado':
                clt.refrigerado2.append(RefriG(row[0], row[1], row[2], row[3], row[4]))

    return clt.refrigerado2


def made_type_rp():
    with open('../ejemplo_lista.csv', 'r') as dato:
        reader = csv.reader(dato)
        header = dato.readline()
        for row in reader:
            if row[2] == 'refrigerado':
                clt.refrigerado.append(RefriP(row[0], row[1], row[2], row[3], row[4]))

    return clt.refrigerado


def made_type_e():
    with open('../ejemplo_lista.csv', 'r') as dato:
        reader = csv.reader(dato)
        header = dato.readline()
        for row in reader:
            if row[3] == 'liquido' or row[3] == 'gas' and row[2] != 'inflamable':
                clt.estanque.append(Estanque(row[0], row[1], row[2], row[3], row[4]))

    return clt.estanque


def made_type_ei():
    with open('../ejemplo_lista.csv', 'r') as dato:
        reader = csv.reader(dato)
        header = dato.readline()
        for row in reader:
            if row[2] == 'inflamable':
                clt.estanque_inf.append(EstanqueI(row[0], row[1], row[2], row[3], row[4]))

    return clt.estanque_inf


def solida():
    with open('../ejemplo_lista.csv', 'r') as dato:
        reader = csv.reader(dato)
        header = dato.readline()
        for row in reader:
            if row[3] == 'solida':
                clt.solido.append(Container(row[0], row[1], row[2], row[3], row[4]))
    return clt.solido


def liquida():
    with open('../ejemplo_lista.csv', 'r') as dato:
        reader = csv.reader(dato)
        header = dato.readline()
        for row in reader:
            if row[3] == 'liquido':
                clt.liquido.append(Container(row[0], row[1], row[2], row[3], row[4]))

    return clt.liquido


def gases():
    with open('../ejemplo_lista.csv', 'r') as dato:
        reader = csv.reader(dato)
        header = dato.readline()
        for row in reader:
            if row[3] == 'gas':
                clt.gas.append(Container(row[0], row[1], row[2], row[3], row[4]))

    return clt.gas


# ------------------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------------------ #
def n():
    with open('../ejemplo_lista.csv', 'r') as dato:
        reader = csv.reader(dato)
        header = dato.readline()
        for row in reader:
            if row[2] == 'normal':
                clt.n1.append(Container(row[0], row[1], row[2], row[3], row[4]))
    return clt.n1


def rf():
    with open('../ejemplo_lista.csv', 'r') as dato:
        reader = csv.reader(dato)
        header = dato.readline()
        for row in reader:
            if row[2] == 'refrigerado':
                clt.r.append(Container(row[0], row[1], row[2], row[3], row[4]))

    return clt.r


def t_inf():
    with open('../ejemplo_lista.csv', 'r') as dato:
        reader = csv.reader(dato)
        header = dato.readline()
        for row in reader:
            if row[2] == 'inflamable':
                clt.inf.append(Container(row[0], row[1], row[2], row[3], row[4]))

    return clt.inf


# ----------------------------------------------------------------------------------------------------------- #
# ------------------------------------------------------------------------------------------------------------ #
def mejor_op():
     a = Avion(Avion.cost, Avion.storage_t)
     b = Barco(Barco.cost, Barco.storage_t)
     c = Camion(Camion.cost, Camion.storage_t)
     t = Tren(Tren.cost, Tren.storage_t)

     x = float(Avion.cost_t(a))
     y = float(Barco.cost_t(b))
     z = float(Camion.cost_t(c))
     w = float(Tren.cost_t(t))

     at = x / Avion.cost
     bt = y / Barco.cost
     ct = z / Camion.cost
     wc = w / Tren.cost

     if x < y and z and w:
        option.append('Avion')
        option.append(x)
        option.append(at)
        option.append("../imgs/avion.jpeg")
        return option

     elif y < x and z and w:
        option.append('Barco')
        option.append(y)
        option.append(bt)
        option.append("../imgs/barco.jpg")
        return option

     elif z < y and x and w:
        option.append('Camion')
        option.append(z)
        option.append(ct)
        option.append("../imgs/camion.jpg")
        return option

     elif w < y and x and z:
        option.append('../imgs/Tren')
        option.append(w)
        option.append(wc)
        option.append("../imgs/tren.jpg")
        return option


# ------------------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------------------ #
p = made_type_np()
q = made_type_rp()
rx = made_type_rg()
s = made_type_e()
t = made_type_ei()

op = solida()
ap = liquida()
gs = gases()

ns = n()
rs = rf()
ix = t_inf()

cal = clt.calcular_cont()
cal2 = clt.calcular_tonelaje()
cal3 = clt.calcular_tonelaje_masa()
cal4 = clt.calcular_tonelaje_tipo()

z = mejor_op()

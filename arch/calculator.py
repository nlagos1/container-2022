

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


def calcular_tonelaje():
    xd = []
    k = 0
    j = 0
    l = 0
    p = 0
    m = 0
    n = 0

    for q in normal:
        j += int(q.peso)

    for w in normal2:
        k += int(w.peso)

    for e in refrigerado:
        l += int(e.peso)

    for r in refrigerado2:
        p += int(r.peso)

    for y in estanque:
        m += int(y.peso)

    for v in estanque_inf:
        n += int(v.peso)

    xd.append(k)
    xd.append(j)
    xd.append(l)
    xd.append(p)
    xd.append(m)
    xd.append(n)

    return xd


def calcular_cont():
    cont = []
    k = 0
    j = 0
    lx = 0
    px = 0
    mx = 0
    nx = 0

    for qx in normal:
        j += float(qx.peso)/24000

    for w in normal2:
        k += float(w.peso)/12000

    for e in refrigerado:
        lx += float(e.peso)/10000

    for f in refrigerado2:
        px += float(f.peso)/20000

    for y in estanque:
        mx += float(y.peso)/24000

    for v in estanque_inf:
        nx += float(v.peso)/20000

    cont.append(k)
    cont.append(j)
    cont.append(lx)
    cont.append(px)
    cont.append(mx)
    cont.append(nx)

    return cont


def calcular_tonelaje_masa():
    fs = []

    kx = 0
    jx = 0
    lx = 0

    for qx in solido:
        jx += int(qx.peso)

    for w in liquido:
        kx += int(w.peso)

    for e in gas:
        lx += int(e.peso)

    fs.append(kx)
    fs.append(jx)
    fs.append(lx)

    return fs


def calcular_tonelaje_tipo():
    fx = []

    hx = 0
    qx = 0
    cx = 0

    for q in n1:
        hx += int(q.peso)

    for w in r:
        qx += int(w.peso)

    for e in inf:
        cx += int(e.peso)

    fx.append(hx)
    fx.append(qx)
    fx.append(cx)

    return fx


def cal_tonelaje_total():
    xd = []
    k = 0
    j = 0
    l = 0
    p = 0
    m = 0
    n = 0

    for q in normal:
        j += int(q.peso)

    for w in normal2:
        k += int(w.peso)

    for e in refrigerado:
        l += int(e.peso)

    for r in refrigerado2:
        p += int(r.peso)

    for y in estanque:
        m += int(y.peso)

    for v in estanque_inf:
        n += int(v.peso)

    xd.append(k)
    xd.append(j)
    xd.append(l)
    xd.append(p)
    xd.append(m)
    xd.append(n)

    return sum(xd)

def tipo_ropa(tipos):
    typess=[]
    for i in tipos:
        if i not in typess:
            typess.append(i)
    return(typess)

def ropa_faltante(ropas, ropas1, ropas2):
    ropa=[]
    for i in range(0,len(ropas)):
        if ropas2 == ropas1[ropas[i]]:
            ropa.append(ropas[i])
    return(ropa)

def novendo(no_esta, no_esta1):
    a_vender=[]
    for i in no_esta:
        if i not in no_esta1:
            a_vender.append(i)
    return(a_vender)

def cambio_socios(x, y):
    listax1=[]
    listax2=[]
    for i in x:
        if i not in y:
            listax1.append(i) 
    for i in y:
        if i not in x:
            listax2.append(i)
    if len(listax1)<len(listax2):
        return(len(listax1))
    else:
        return(len(listax2))
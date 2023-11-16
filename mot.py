def NbcMin(passe):
    nb=0
    for i in passe:
        if'a'<=i<='z':
            nb=nb+1
    return nb
###############################################
def NbcMaj(passe):
    nb=0
    for i in passe:
        if'A'<=i<='Z':
            nb=nb+1
    return nb       
################################################
def NbcAlpha(passe):
    return len(passe)-NbcMaj(passe)-NbcMin(passe)
###############################################
def longMaj(passe):
    d=0
    s=0
    i=0
    while i<len(passe):
        if 'A'<passe[i]<'Z':
            s+=1
        else:
            if s>d:
                s=d
                s=0
            i+=1
        return d
##############################################   
def longMin(passe):
    d=0
    s=0
    i=0
    while i<len(passe):
        if 'a'<passe[i]<'z':
            s+=1
        else:
            if s>d:
                s=d
                s=0
            i+=1
        return d     
################################################
def score(passe):
    bonus=(len(passe)-NbcMin(passe))*3+(len(passe)-NbcMaj(passe))*2+(len(passe)-NbcAlpha(passe))*5
    penalites=longMaj(passe)*3+longMin(passe)*2
    val=bonus-penalites
    if val<20:
        print("tres faible")
    elif val<40:
        print("faible")
    elif val<80:
        print("fort")
    else:
        print("trés fort")
##############################################
passe=input("entrez un mot de pass")
print(NbcMin(passe))
print(NbcMaj(passe))
print(NbcAlpha(passe))
print(longMaj(passe))
print(longMin(passe))
print(score(passe))

def getFail(P):
    '''Utility that computes and returns KMP 'fail' list'''
    Plen=len(P)
    fail=[0]*Plen
    j=1
    k=0
    while j<Plen:
        if P[j]==P[k]:
            fail[j]=k+1
            j+=1
            k+=1
            
        elif k>0:
            k=fail[k-1]
        else:
            j+=1
    return fail

def findKMP(T,P):
    '''Return the lowest index of T at which substring P begins (of else -1)'''
    Tlen,Plen=len(T),len(P)
    if Plen==0:return 0
    fail=getFail(P)
    j=0
    k=0
    while j<Tlen:
        if T[j]==P[k]:
            if k==Plen-1:
                return j-Plen+1
            j +=1
            k +=1
        elif k>0:
            k=fail[k-1]
        else:
            j+=1
    return -1

if __name__=='__main__':
    T='abababaa'
    P='abaa'
    print findKMP(T,P)

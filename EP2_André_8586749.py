import math

def decompoe_LU_tridiagonal(a,b,c,L,U):
# a, b, c, L, U são vetores // este algoritmo supõe uma matriz nxn // 
    n = len(a)
    U[0] = b[0]
    for i in range(1,n,1):
        L[i] = a[i]/U[i-1]
        U[i] = b[i]-L[i]*c[i-1]
    return

def resolve_LU_tridiagonal(L,U,d,c,x,y):
# L,U,d,c,x,y são vetores // este algoritmo supõe uma matriz nxn //
    n = len(L)
    y[0] = d[0]
    for i in range (1,n,1):
        y[i] = d[i]-L[i]*y[i-1]
    x[n-1] = y[n-1]/U[n-1]
    for j in range (n-2,-1,-1):
        x[j] = (y[j]-c[j]*x[j+1])/U[j]
    return

def preenche_vetor(v,a,n):
    # dado um vetor criado, sem elementos, preenche este vetor com um valor especificado "a" com "n" elementos
    ''' vetor, float, inteiro -> null '''
    for i in range (0,n,1):
        v.append(a)
    return

def preenche_resp(v,n):
    # Esta função é um quebra galho bem específico deste problema, apenas para eu não escrever o vetor na mao
    ''' vetor, inteiro - > null
    Esta função modifica um vetor dado, preenchendo-o com o vetor d específico do problema'''
    for i in range (0,n,1):
        v.append(math.cos(((i+1)*math.pi)/10))
    return

def escalar_por_vetor(k,v):
    ''' float, vetor -> vetor
    Esta função multiplica cada elemento de um vetor por um numero k'''
    xz = []
    for i in range (0,len(v),1):
        xz.append(k*v[i])
    return xz

def soma_vetores(u,v):
    ''' float , float - > float
    Esta função soma os elementos de dois vetores dois a dois'''
    # u e v devem ter o mesmo tamanho! Use com cuidado
    s=[]
    for i in range (0,len(u),1):
        s.append(u[i]+v[i])
    return s


def main ():
    #Neste primeiro trecho preparamos os vetores a serem usados
    a=[]
    b=[]
    c=[]
    d=[]
    
    # a = [0,0.5,0.5,...,0.5] com 19 casas
    a.append(0)
    preenche_vetor(a,0.5,18)
    
    # c = [0.5,0.5,...,0.5,0] com 19 casas
    preenche_vetor(c,0.5,18)
    c.append(0)

    # b = [2,2,...,2,2] com 19 casas
    preenche_vetor(b,2,19)

    # d é vetor de 20 elementos tal que dn = cos(n*pi/10), 1<n<20
    preenche_resp(d,19)

    # declaramos os vetores a serem usados e construimos cada um com 19 elementos
    y=[]
    preenche_vetor(y,0,19)
    yb=[]
    preenche_vetor(yb,0,19)
    L=[]
    preenche_vetor(L,0,19)
    U=[]
    preenche_vetor(U,0,19)

    #resolve decomposição LU de uma matriz tridiagonal dado os vetores das diagonais mais dois vetores auxiliares para a resposta
    decompoe_LU_tridiagonal(a,b,c,L,U)

    #resolve sistema tridiagonal decomposto em LU LUX=d. Deve ser fornecidos os vetores L, U, d (respostas),
    #c (vetor da matriz original representando a diagonal reaproveitada na decomposição LU de matrizes tridiagonais)
    # e os vetores yb e y auxiliares.
    # Observe que resolvemos U*x = y e depois L*y = d
    'Aqui resolvemos a matriz T*yb = d'
    resolve_LU_tridiagonal(L,U,d,c,yb,y)

    
    #print ("%.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f"%(round(d[0],2), round(d[1],2), round(d[2],2), round(d[3],2), round(d[4],2), round(d[5],2), round(d[6],2), round(d[7],2), round(d[8],2), round(d[9],2), round(d[10],2), round(d[11],2), round(d[12],2), round(d[13],2), round(d[14],2), round(d[15],2), round(d[16],2), round(d[17],2), round(d[18],2)))
    #print ("%.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f"%(round(x[0],2), round(x[1],2), round(x[2],2), round(x[3],2), round(x[4],2), round(x[5],2), round(x[6],2), round(x[7],2), round(x[8],2), round(x[9],2), round(x[10],2), round(x[11],2), round(x[12],2), round(x[13],2), round(x[14],2), round(x[15],2), round(x[16],2), round(x[17],2), round(x[18],2)))

    y1=[]
    preenche_vetor(y1,0,19)
    
    z=[]
    preenche_vetor(z,0,19)
    
    v=[]
    v.append(0.5)
    preenche_vetor(v,0,17)
    v.append(0.5)
    
    resolve_LU_tridiagonal(L,U,v,c,z,y1)
    ' Aqui resolvemos Tz = v'

    '''calcula Xn específico para o sistema a ser solucionado. Caso se queira
    fazer futuramente essa resolução de uma maneira geral deverá colocar isso em uma função
    e substituir alguns dos valores por argumentos da função'''
    xn= (math.cos(((20)*math.pi)/10) - 0.5*yb[0] -0.5*yb[18])/(2-0.5*z[0]-0.5*z[18])
    

    xbarra = soma_vetores(yb,escalar_por_vetor(-xn,z))

    '''imprime o vetor x, resultado do teste sugerido'''

    print("Resposta final:")
    for j in range (0,19,1):
        print ("x[%d] = %f"%(j+1,xbarra[j]))
    print("x[20] = %f"%(xn))
    print("")

    print("Diagonal principal de U:")
    for j in range (0,19,1):
        print ("U[%d] = %f"%(j+1,U[j]))
    print("")

    print("Diagonal inferior de L:")
    for j in range (0,19,1):
        print ("L[%d] = %f"%(j+1,L[j]))
    print("")

    print("yb em T*yb = d:")
    for j in range (0,19,1):
        print ("yb[%d] = %f"%(j+1,yb[j]))
    print("")

    print("z em T*z = v:")
    for j in range (0,19,1):
        print ("z[%d] = %f"%(j+1,z[j]))





    return 0

main()

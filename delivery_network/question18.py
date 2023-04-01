def trucks_filtre(filename):
    with open(filename, 'r') as file:
        nb_trucks=int(file.readline())
        trucks=[]
        for _ in range(nb_trucks):
            power,cost=file.readline().split()
            trucks.append((int(power),int(cost)))
    file.close()
    trucks.sort(key=lambda x: (x[0],-x[1]))
    trucks_filtre=[trucks[-1]]
    for elt in trucks[-2::-1]:
        if elt[1]<trucks_filtre[-1][1]:
            trucks_filtre.append(elt)
    return trucks_filtre[::-1]

def process_knapsack(filename,trucks_filtre):
    with open(filename,'r') as file:
        nb_path=int(file.readline())
        path=[]
        for _ in range(nb_path):
            city1,city2,utility,power=file.readline().split()
            path.append((int(city1),int(city2),float(utility),int(power)))
    file.close()
    path.sort(key=lambda x: (x[3]))
    knapsack=[]
    i=0
    N=len(trucks_filtre)
    for k in range(N):
        if trucks_filtre[k][0]>=path[i][3]:
            while i<len(path) and trucks_filtre[k][0]>=path[i][3] :
                knapsack.append((trucks_filtre[k][0],trucks_filtre[k][1],path[i][2],path[i][0],path[i][1])) #Puissance, coût, profit, ville1, ville2
                i+=1
        if i>=len(path):
            return knapsack

B=25*10**9
def whatisinmybag(knapsack):
    knapsack.sort(key=lambda x: x[1]/x[2])
    Mybag=[]
    k=0
    S=0
    P=0
    N=len(knapsack)
    while k<N:
        if S+knapsack[k][1]<=B:
            Mybag.append((knapsack[k][0],knapsack[k][1],knapsack[k][3],knapsack[k][4]))
            S+=knapsack[k][1]
            P+=knapsack[k][2]
            k+=1
        else:
            return Mybag,S
    return Mybag,S


def sacADos_dynamique(knapsack):
    matrice = np.array([[0 for _ in range(B+ 1)] for x in range(len(knapsack) + 1)])
    print(matrice)
    for i in range(1, len(knapsack) + 1):
        print(i)
        for w in range(1, B+1):
            print(w)
            if knapsack[i-1][1] <= w:
                matrice[i][w] = max(knapsack[i-1][2] + matrice[i-1][w-knapsack[i-1][1]], matrice[i-1][w])
            else:
                matrice[i][w] = matrice[i-1][w]
            
    # Retrouver les éléments en fonction de la somme
    w = B
    n = len(knapsack)
    elements_selection = []

    while w >= 0 and n >= 0:
        e = knapsack[n-1]
        if matrice[n][w] == matrice[n-1][w-e[1]] + e[2]:
            elements_selection.append(e)
            w -= e[1]

        n -= 1

    return matrice[-1][-1], elements_selection
    




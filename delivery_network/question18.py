def trucks_filtre(filename):
    """""   Fonction : trucks_filtre
    Description:
    -----------
    on  effectue un tri sur le fichier : si c1=c2, on prend le camion le plus puissant et si p1=p2, 
    on prend le camion le moins cher.
    input:
    ------
    Fichier trucks.x.in

    output:
    -------
    Liste des camions triés, les moins chères pour une puissance donnée

    Complexité:
    -------
    O(C) avec C le nombre de camions

    """
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
    """""   Fonction : process_knapsack
    Description:
    -----------
    On veut construire la liste des éléments pouvant être mis dans le sac à dos. Chaque trajet du fichier routes.x.out lui est le 
    camion le moins cher avec une puissance suffisante. Ainsi, l'analogie avec le problème du sac à dos revient à mettre dans le sac 
    des camions associés à un trajet qui ont donc un coût et une valeur : le profit du camion.
    input:
    ------
    Fichier routes.x.out et trucks_filtre

    output:
    -------
    Les camions associés à leur trajet pouvant être mis dans le sac à dos.
    Complexité:
    -------
    O(T+C) avec C le nombre de camions et T le nombre de trajets.

    """
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

B=25*10**9 #BUDGET
def sol_exacte(knapsack):
    """""   Fonction : sol_exacte
    Description:
    -----------
    On donne la solution exacte au problème du sac à dos
    input:
    ------
    Knapsack

    output:
    -------
    Les camions associés à leur trajet pouvant être mis dans le sac à dos.
    Complexité:
    -------
    O(T*B) avec T le nombre de trajet

    """
    matrice = [[0 for x in range(B + 1)] for x in range(len(knapsack) + 1)]
    for i in range(1, len(knapsack) + 1):
        for w in range(0, B+1):
            print(w)
            if knapsack[i-1][1] <= w:
                matrice[i].append(max(knapsack[i-1][2] + matrice[i-1][w-knapsack[i-1][1]], matrice[i-1][w]))
            else:
                matrice[i].append(matrice[i-1][w])
            
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

    return elements_selection, matrice[-1][-1]



def whatisinmybag(knapsack):
    """""   Fonction : whatisinmybag
    Description:
    -----------
    On donne une solution approchée des camions à acheter et des trajets à effectuer pour maximiser le profit
    input:
    ------
    Knapsack

    output:
    -------
    Les camions associés à leur trajet pouvant être mis dans le sac à dos.

    Complexité:
    -------
    O(Tlog(T)) avec T le nombre de trajet

    """

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



    




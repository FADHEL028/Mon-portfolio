#--------QUESTION-1---------
def create_answers_from_text_file(fichier):
    """
    Transforme un fichier contenant une chaîne multiligne "Nom:note/note/..." 
    en un dictionnaire {nom: [notes en entiers]}
    """
    dictionnaire_de_réponses = {}                                       #on initialise le dictionnaire de réponses 
    text = open(fichier).read()                         #on lit le fichier et on stocke son contenu dans une variable
    lines = text.strip().split('\n')                    #on divise le texte en lignes
    #Créez une boucle while pour parcourir les lignes du fichier et remplir notre dictionnaire en enlevant les espaces inutiles et les separateurs 
    i = 0 
    while i < len(lines):
        line = lines[i].split(":")
        # Ajout du nom
        name = line[0]
        # Ajout des réponses
        answers = []
        scores = line[1].split("/")
        j = 0
        while j < len(scores):
            answers.append(int(scores[j]))
            j += 1    
        dictionnaire_de_réponses[name.strip()] = answers
        i += 1
    return dictionnaire_de_réponses                       #on retourne le dictionnaire de réponses 

#--------QUESTION-2---------
from math import sqrt
def Euclidean_distance(answer1, answer2):
    """
    Calcule la distance euclidienne entre deux listes de réponses de même longueur
    """
    somme = 0                                 #on initialise la somme à 0
    #Créez une boucle while pour parcourir les deux listes et calculer la somme des carrés des différences entre les éléments correspondants
    i = 0
    while i < len(answer1):
        somme += (answer1[i] - answer2[i]) ** 2 #on calcule la différence au carré entre les éléments correspondants et on l'ajoute à la somme
        i += 1
    return sqrt(somme)                            #on retourne la racine carrée de la somme

#--------QUESTION-3---------
def Euclidean_house(reponses, reference):
    """
    Trouve la maison d'un élève la plus proche des références en utilisant la distance euclidienne
    """
    i = 0
    distance_minimale = float('inf')  #on initialise la distance minimale à l'infini
    #Créez une boucle while pour parcourir les références et trouver la maison avec la distance euclidienne minimale
    while i < len(reference):
        distance = Euclidean_distance(reponses, reference[i]["answer"]) #on calcule la distance euclidienne entre les réponses de l'élève et les réponses des fondateurs
        if distance < distance_minimale: #on vérifie si la distance calculée est inférieure à la distance minimale actuelle
            distance_minimale = distance #on met à jour la distance minimale
            maison_la_plus_proche = reference[i]["house"]#on met à jour la maison la plus proche
        i += 1
    return maison_la_plus_proche

#--------QUESTION-4-&-5---------
from json import load
from s101 import nb_erreurs
f = open("houses_ref.json")
reference = load(f)
f.close()
def Euclidean_repartition(reponses, reference) :
    """
    Répartit les élèves dans les maisons en utilisant la distance euclidienne
    """
    répartition = {}                          #on initialise le dictionnaire de répartition
    #Créez une boucle while pour parcourir les réponses des élèves et déterminer leur maison en utilisant la fonction Euclidean_house
    élèves = list(reponses.keys()) #on crée une liste des noms des élèves à partir des clés du dictionnaire de réponses
    i = 0
    while i < len(élèves):
        nom = élèves[i]            #on récupère le nom de l'élève à l'indice i
        house = Euclidean_house(reponses[nom], reference) #on détermine la maison de l'élève en utilisant la fonction Euclidean_house
        répartition[nom] = house #on ajoute l'élève et sa maison au dictionnaire de répartition
        i += 1
    return répartition                       #on retourne le dictionnaire de répartition

#--------QUESTION-6---------
from json import load
def insertion_position_NN (answer, ref, neighbors) :
    """Retourne l'indice de positionnement dans neighbors de la maison la plus proche de answer selon ref.
    """
    distance = Euclidean_distance(answer, ref["answer"])
    position = 0
    while position < len(neighbors) and distance >= Euclidean_distance(neighbors[position]["answer"], answer):
    #on parcourt la liste des voisins tant que la position est inférieure à la longueur de la liste et que la distance est supérieure à la distance euclidienne entre la réponse et la réponse de référence du voisin à la position actuelle
        position += 1           
    return position

#--------QUESTION-7---------
def insertion_NN(answer, ref, neighbors, k):
    """Insère la maison la plus proche de answer dans neighbors en respectant la taille maximale k >= len(neighbors).
    """
    position = insertion_position_NN(answer, ref, neighbors) #on trouve la position d'insertion de la maison la plus proche
    if k >= len(neighbors) :
        if position < k:
            neighbors.insert(position, ref) #on insère la maison à la position trouvée
            if len(neighbors) > k:
                neighbors.pop() #on supprime la dernière maison si la taille dépasse k        
    return neighbors

#--------QUESTION-8---------
def NN(answer, neighbors, k) :
    """
    Retourne un tableau des k plus proches voisins triés du plus proche au moins proche.
    """
    i = 0
    nearest_neighbors = []
    while len(nearest_neighbors) < k or i < len(neighbors):
        nearest_neighbors = insertion_NN(answer, neighbors[i], nearest_neighbors, k)
        i += 1
    return nearest_neighbors

#--------QUESTION-9---------
def NN_house(neighbors) :
    """
    Retourne la maison la plus fréquente parmi les k plus proches voisins.
    """
    houses = {}
    i = 0
    while i < len(neighbors):
        house = neighbors[i]["house"] #on récupère la maison du voisin à l'indice i
        if house in houses:     #on vérifie si la maison est déjà dans le dictionnaire
            houses[house] += 1
        else:
            houses[house] = 1
        i += 1
    # Trouver la maison avec le maximum de votes 
    majority_house = ""
    max_votes = 0
    cles = list(houses.keys())
    j = 0
    while j < len(cles):
        h = cles[j]
        if houses[h] > max_votes:
            max_votes = houses[h]
            majority_house = h
        j += 1
    return majority_house       #retourne la maison majoritaire

#--------QUESTION-10---------
def NN_repartition(answer, reference, k) :
    """
    Répartit les élèves dans les maisons en utilisant la méthode des k plus proches voisins.
    """
    répartition = {}
    élèves = list(answer.keys()) #on crée une liste des noms des élèves à partir des clés du dictionnaire de réponses
    i = 0
    while i < len(élèves):
        nom = élèves[i]
        neighbors = NN(answer[nom], reference, k) #on trouve les k plus proches voisins de l'élève
        house = NN_house(neighbors) #on détermine la maison majoritaire parmi les k plus proches voisins
        répartition[nom] = house  #on ajoute l'élève et sa maison au dictionnaire de répartition
        i += 1
    return répartition

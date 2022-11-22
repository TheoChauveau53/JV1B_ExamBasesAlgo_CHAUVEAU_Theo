myTable = [5,3,4,2]

#Partie 1 - Tri à bulles

#1

#a=myTable[1]
#myTable[1]=myTable[0]
#myTable[0]=a
#
#print(myTable)

#2

#for i in range(0, len(myTable)-1):
#    if (myTable[i]>myTable[i+1]):
#        a=myTable[i]
#        myTable[i]=myTable[i+1]
#        myTable[i+1]=a

#print(myTable)

#3
for n in range (0,len(myTable)-1):
    for i in range(0, len(myTable)-1-n):
        if (myTable[i]>myTable[i+1]):
            a=myTable[i]
            myTable[i]=myTable[i+1]
            myTable[i+1]=a

print(myTable)

#4
#Le tri à bulles est très lent car il a besoin de comparer plusieurs fois chaque élément du tableau et de faire plusieurs permutations pour que la plus grande valeur soit à sa place.
#Alors qu'un tri par insertion trouve la plus grande valeur et l'envoie à sa place en une seule permutation.
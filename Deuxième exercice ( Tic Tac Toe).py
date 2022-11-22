#partie 2 - Tic tac Toe

#1
end=False

joueur="X"

a="a" 
b="b" 
c="c" 
d="d" 
e="e" 
f="f" 
g="g" 
h="h" 
i="i"


while (end==False):
    if (joueur=="X" and end==False):
        stock=input("joueur X, où voulez-vous jouer?")
        if (stock=="a"):
            if(a=="X" or a=="O"):
                print("Case déjà occupée")
            else:
                a="X"
                joueur="O"
        if (stock=="b"):
            if(b=="X" or b=="O"):
                print("Case déjà occupée")
            else:
                b="X"
                joueur="O"
        if (stock=="c"):
            if(c=="X" or c=="O"):
                print("Case déjà occupée")
            else:
                c="X"
                joueur="O"
        if (stock=="d"):
            if(d=="X" or d=="O"):
                print("Case déjà occupée")
            else:
                d="X"
                joueur="O"
        if (stock=="e"):
            if(e=="X" or e=="O"):
                print("Case déjà occupée")
            else:
                e="X"
                joueur="O"
        if (stock=="f"):
            if(f=="X" or f=="O"):
                print("Case déjà occupée")
            else:
                f="X"
                joueur="O"
        if (stock=="g"):
            if(g=="X" or g=="O"):
                print("Case déjà occupée")
            else:
                g="X"
                joueur="O"
        if (stock=="h"):
            if(h=="X" or h=="O"):
                print("Case déjà occupée")
            else:
                h="X"
                joueur="O"
        if (stock=="i"):
            if(i=="X" or i=="O"):
                print("Case déjà occupée")
            else:
                i="X"
                joueur="O"
        
        print(a,end='')
        print("|",end='')
        print(b,end='')
        print("|",end='')
        print(c)

        print(d,end='')
        print("|",end='')
        print(e,end='')
        print("|",end='')
        print(f)

        print(g,end='')
        print("|",end='')
        print(h,end='')
        print("|",end='')
        print(i)

        if(a==b==c):    #condition victoire pour X 
            end=True
            win="X"
        if(d==e==f):
            end=True
            win="X"
        if(g==h==i):
            end=True
            win="X"
        if(a==d==g):
            end=True
            win="X"
        if(b==e==h):
            end=True
            win="X"
        if(c==f==i):
            end=True
            win="X"
        if(a==e==i):
            end=True
            win="X"
        if(c==e==g):
            end=True
            win="X"

        if(end==False):  #voir si la grille est complète
            if(a=="X" or a=="O"):
                if(b=="X" or b=="O"):
                    if(c=="X" or c=="O"):
                        if(d=="X" or d=="O"):
                            if(e=="X" or e=="O"):
                                if(f=="X" or f=="O"):
                                    if(g=="X" or g=="O"):
                                        if(h=="X" or h=="O"):
                                            if(i=="X" or i=="O"):
                                                end=True
                                                win="personne"

  
    if (joueur=="O" and end==False):
        stock=input("joueur O, où voulez-vous jouer?")
        if (stock=="a"):
            if(a=="X" or a=="O"):
                print("Case déjà occupée")
            else:
                a="O"
                joueur="X"
        if (stock=="b"):
            if(b=="X" or b=="O"):
                print("Case déjà occupée")
            else:
                b="O"
                joueur="X"
        if (stock=="c"):
            if(c=="X" or c=="O"):
                print("Case déjà occupée")
            else:
                c="O"
                joueur="X"
        if (stock=="d"):
            if(d=="X" or d=="O"):
                print("Case déjà occupée")
            else:
                d="O"
                joueur="X"
        if (stock=="e"):
            if(e=="X" or e=="O"):
                print("Case déjà occupée")
            else:
                e="O"
                joueur="X"
        if (stock=="f"):
            if(f=="X" or f=="O"):
                print("Case déjà occupée")
            else:
                f="O"
                joueur="X"
        if (stock=="g"):
            if(g=="X" or g=="O"):
                print("Case déjà occupée")
            else:
                g="O"
                joueur="X"
        if (stock=="h"):
            if(h=="X" or h=="O"):
                print("Case déjà occupée")
            else:
                h="O"
                joueur="X"
        if (stock=="i"):
            if(i=="X" or i=="O"):
                print("Case déjà occupée")
            else:
                i="O"
                joueur="X"
        
        print(a,end='')
        print("|",end='')
        print(b,end='')
        print("|",end='')
        print(c)

        print(d,end='')
        print("|",end='')
        print(e,end='')
        print("|",end='')
        print(f)

        print(g,end='')
        print("|",end='')
        print(h,end='')
        print("|",end='')
        print(i)

        if(a==b==c):    #condition victoire pour O
            end=True
            win="O"
        if(d==e==f):
            end=True
            win="O"
        if(g==h==i):
            end=True
            win="O"
        if(a==d==g):
            end=True
            win="O"
        if(b==e==h):
            end=True
            win="O"
        if(c==f==i):
            end=True
            win="O"
        if(a==e==i):
            end=True
            win="O"
        if(c==e==g):
            end=True
            win="O"
        
        if(end==False):  #voir si la grille est complète
            if(a=="X" or a=="O"):
                if(b=="X" or b=="O"):
                    if(c=="X" or c=="O"):
                        if(d=="X" or d=="O"):
                            if(e=="X" or e=="O"):
                                if(f=="X" or f=="O"):
                                    if(g=="X" or g=="O"):
                                        if(h=="X" or h=="O"):
                                            if(i=="X" or i=="O"):
                                                end=True
                                                win="personne"




if(win=="X" or win=="O"):
    print("La partie est finie, le joueur",win,"a gagné")
if(win=="personne"):
    print("La partie est finie, la grille est complète, personne de ne gagne")
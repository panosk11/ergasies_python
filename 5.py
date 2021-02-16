import random

print ("\n")
x = input("Δώσε τον x άξονα του ορθογώνιου πίνακα...\n")
print ("\n")
y = input("Δώσε τον y άξονα του ορθογώνιου πίνακα...\n")
      
x = int(x)
y = int(y)
dim = x*y
count = 0

print(f"Ο πίνακας θα είναι {dim} στοιχείων, {x}X{y}. ")
for q in range (100):
    a=[[0 for j in range(x)] for i in range (y)]

    for i in range (y):
        if (i%2!=0):
            for j in range (x):          
                if (j%2!=0):
                    a[i][j]="O"
                else:
                    a[i][j]="S"
            random.shuffle(a[i])
        else:
            for j in range (x):
                
                if (j%2!=0):
                    a[i][j]="S"
                else:
                    a[i][j]="O"
            random.shuffle(a[i])

    for row in a:
        print(' '.join([str(elem) for elem in row]))

    hor = 0
    ver = 0
    diag = 0
    #Οριζόντια
    for i in range (y):
        if (x>=3):
            for j in range (x-2):       
                if (a[i][j]=="S"):            
                    if (a[i][j+1]=="O"):
                        if (a[i][j+2]=="S"):
                            hor = hor + 1       
    #Κάθετα
    k=-1
    for j in range (x):
        if (y>=3):
            k=k+1
            for i in range (y-2):       
                if (a[i][k]=="S"):            
                    if (a[i+1][k]=="O"):
                        if (a[i+2][k]=="S"):
                            ver = ver + 1
    #Διαγώνια
    if (x>=3 and y>=3):
        for i in range (y-2):
            for j in range (x-2):
                if (a[i][j]=="S"):
                    if (a[i+1][j+1]=="O"):
                        if (a[i+2][j+2]=="S"):
                            diag = diag + 1
    #Ανάποδα διαγώνια                        
    if (x>=3 and y>=3):
        for i in range (y-1,y):
            for j in range (x-2):
                if (a[i][j]=="S"):
                    if (a[i-1][j+1]=="O"):
                        if (a[i-2][j+2]=="S"):
                            diag = diag + 1    

    if (hor==0):
        print ("\n")
        print ("Οριζόντια δεν εμφανίζονται SOS")
    elif (hor==1):
        print ("\n")
        print ("Οριζόντια εμφανίζεται 1 SOS")
    else:
       print ("\n")
       print ("Οριζόντια εμφανίζονται",hor,"SOS")
    if (ver==0):
        print ("Κάθετα δεν εμφανίζονται SOS")
    elif (ver==1):
        print ("Κάθετα εμφανίζεται 1 SOS")
    else:
        print ("Κάθετα εμφανίζονται",ver,"SOS")
    if (diag==0):
        print ("Διαγώνια δεν εμφανίζονται SOS")
        print ("------------------------------------------------")
    elif (diag==1):
        print ("Διαγώνια εμφανίζεται 1 SOS")
        print ("------------------------------------------------")
    else:
        print ("Διαγώνια εμφανίζονται",diag,"SOS")
        print ("------------------------------------------------")    
        
    count = count + hor + ver + diag
mo = count/100
print ("\n")
print ("Ο μέσος όρος των SOS στα 100 ορθογώνια είναι :",mo)
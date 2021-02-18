import random

n = int(input("Δώσε μου τον ν όρο της ακολουθίας Fibonacci.\n\n"))

#Περίπτωση 0 ή αρνητικού αριθμού
while (n<=0):
    n = int(input("\nΔώσε μου θετικό αριθμό.\n\n"))

#Δημιουργία λίστας Fibonacci
count = 0
p, p2 = 0, 1
while (count < n):
    x = p + p2
    p = p2
    p2 = x
    count = count + 1

#Περιπτώσεις

#Περίπτωση όρου 1 ή 2
if (n==1 or n==2):
    print("\nΟ",n,"όρος της ακολουθίας Fibonacci είναι ο 1 και είναι πρώτος.")
#Περίπτωση όρου 3
elif (n==3):
    print("\nΟ",n,"όρος της ακολουθίας Fibonacci είναι ο 2 και είναι πρώτος.")
#Περίπτωση όρου >3
else:
    count1 = 0
    for i in range (20):
        a = random.randint(2,p-1)
        x = a**p
        if (x%p==a):
            count1 = count1 + 1
    if (count1==20):
        print("\nΟ",n,"όρος της ακολουθίας Fibonacci είναι ο",p,"και είναι πρώτος.")   
    else:
        print("\nΟ",n,"όρος της ακολουθίας Fibonacci είναι ο",p,"και δεν είναι πρώτος.")
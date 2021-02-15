import urllib.request
import json
import datetime, time

Current_Date_Formatted = datetime.datetime.today().strftime ('%d%m%Y')
Day = datetime.datetime.today().strftime ('%d')
Month = datetime.datetime.today().strftime ('%m')
Year = datetime.datetime.today().strftime ('%Y')

now = datetime.datetime.now()
current_time = now.strftime("%H:%M:%S")

if current_time < str("09:00:00"):
    dToday = int(Day)-1
else:
    dToday = int(Day)
    
def get_stats(stats):
    url2 = f"https://api.opap.gr/draws/v3.0/1100/{li1[0]}"
    a2 = urllib.request.urlopen(url2)
    b2 = a2.read()
    b2 = b2.decode()
    li2 = json.loads(b2)
    return li2[stats]["list"]

x = [0]*(dToday*20)

y = 0
for d in range (1, dToday+1):
    k = 0
    date1 = f'{Year}-{Month}-{d:02d}'
    date2 = f'{d:02d}-{Month}-{Year}'
    url1 = f"https://api.opap.gr/draws/v3.0/1100/draw-date/{date1}/{date1}/draw-id"
    a1 = urllib.request.urlopen(url1)
    b1 = a1.read()
    b1 = b1.decode()
    li1 = json.loads(b1)
    for w in range (0, 20):
        x[y] = (get_stats("winningNumbers")[w])
        y = y+1
    print ("Αριθμός κλήρωσης :",li1[0]) 
    print ("Ημερομηνία :", date2)
    print ("Αριθμοί που κληρώθηκαν :")
    print (get_stats("winningNumbers"))
    print ("--------------------------------------------------------------------------------")

for i in range (1, 81):
    if x.count(i)>1:
        print ("Ο αριθμός", i, "εμφανίζεται", x.count(i), "φορές")
    elif x.count(i)!=0:
        print ("Ο αριθμός", i, "εμφανίζεται", x.count(i), "φορά")
    else:
        print ("Ο αριθμός", i, "δεν εμφανίζεται")
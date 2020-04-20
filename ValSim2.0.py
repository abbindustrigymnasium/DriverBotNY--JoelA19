import random 
Partier = [

    {"parti": "Gröngölingarna", "inriktning": "vänster",
        "Block": "småpartierna", "Min Röst": 3, "Max Röst": 12, "partiledare":"Jonas Ostbåge"},
    {"parti": "Partikelpartiet", "inriktning": "vänster",
        "Block": "småpartierna", "Min Röst": 2, "Max Röst": 8, "partiledare": "Mister Bylund"},
    {"parti": "Mälarpartiet", "inriktning": "höger",
        "Block": "småpartierna", "Min Röst": 8, "Max Röst": 18, "partiledare":"Robert Downey jr"},
    {"parti": "Sjörövarpartiet", "inriktning": "höger",
        "Block": "småpartierna", "Min Röst": 3, "Max Röst": 12, "partiledare": "Hans Majonäs"},
    {"parti": "Extremisterna", "inriktning": "höger",
        "Block": "Oljeblocket", "Min Röst": 3, "Max Röst": 6, "partiledare": "Orange man"},
    {"parti": "Maskinpartiet", "inriktning": "vänster",
        "Block": "Oljeblocket", "Min Röst": 12, "Max Röst": 22, "partiledare": "Yussuf Stealen"},
    {"parti": "Framtidspartiet", "inriktning": "höger",
        "Block": "Oljeblocket", "Min Röst": 12, "Max Röst": 18, "partiledare": "Neo"},
    {"parti": "Allpartiet", "inriktning": "vänster",
        "Block": "inget", "Min Röst": 20, "Max Röst": 34, "partiledare": "Kleobold III"},
] # Alla värden
Platsuttalanden = ["i en intervju med Fria Tider.", "när vi frågar honom om hans åsikter på det amerikanska valet.", "på lokalTV i Flen.", "i en intervju med Playboy.", "när vi hittar honom i kön till en strippklubb.", "i veckans avsnitt av skavlan."]
PåverkandeUttalanden = ["Jag är inte rasist, men...", "Jag tycker inte att kommunism är så dåligt ändå...", "Varför tycker alla att Trump är så dålig egentligen?", "Det finns alldeles för mycket glasssmaker!"]
Uttalanden = ["är väldigt nöjd med de", "är väldigt tacksam för de", "vill tacka sin mamma för de", "har återfått sin tro på Allah på grund av de", "hoppar glädjehopp på grund av de", "tar av sig alla kläder och gör helikoptern för de"]
NegUtt = ["vill inte spekulera kring de", "tänker inte kommentera på de", "skyller på nazisterna för de", "säger att det är kommunisternas fel, Det han syftar på är de"]
BlockUtt = ["Inte ens nära, sa", "Vart är motståndet? sa", "lätt som en plätt, sa", "HAHAHAHAHA, sa", "Varför försöker ni ens? sa", "Lär ni er aldrig? sa", "Vi är oövervinnliga, sa", "Vi är odödliga, sa"]  
# Listor med uttalanden
def Rösta(): # Funktionen som allt hänger på, simulerar ett val
    for x in Partier:
        antal_röster = random.randint(x["Min Röst"], x["Max Röst"]) # För varje dictionary i Partier, skapa ett objekt som heter antal_röster, och gör den till ett random värde mellan min och max röster för det objektet
        x["Röster"] = antal_röster # Lägger till objektet
    def takeLast(elem): # En funktion som används för att jag ska kunna sortera Partier på antal röster
        return elem["Röster"]
    Partier.sort(key=takeLast, reverse = True) # Själva sorteringen
    HParti = [] # Skapar en lista per inriktning och block, för att lägga till alla partiledare
    VParti = []
    IParti = []
    SParti = []
    OParti = []
    BlockRöster = [["Småpartierna", 0, SParti], ["Oljeblocket", 0, OParti], ["Inget Block", 0, IParti]] # Skapar listor som jag kan använda vid presentationen för att deklarera vinnare i varje kategori och dess partiledare
    InriktningsRöster = [["Vänster", 0,  VParti ], ["Höger", 0, HParti]]
    TotalRöster = 0
    for x in Partier: # Alla röster räknas ihop, och alla block får sin egen räkning
        TotalRöster += x["Röster"]
        if x["Block"] == "Oljeblocket":
            BlockRöster[1][1] += x["Röster"]
            OParti.append(x["partiledare"])
        elif x["Block"] == "småpartierna":
            BlockRöster[0][1] += x["Röster"]
            SParti.append(x["partiledare"])
        else:
            BlockRöster[2][1] += x["Röster"]
            IParti.append(x["partiledare"])
        if x["inriktning"] == "vänster":
            InriktningsRöster[0][1] += x["Röster"]
            VParti.append(x["partiledare"])
        if x["inriktning"] == "höger":
            InriktningsRöster[1][1] += x["Röster"]
            HParti.append(x["partiledare"])
    return TotalRöster, HParti, VParti, IParti, SParti, OParti, BlockRöster, InriktningsRöster # Returnar alla variablar som behövs

for x in Partier: # Alla partier har en chans att deras partiledare säger något dumt som sänker deras Max Röst med 4. Om partiet är åt höger är chansen 7.5%, annars 5%.

        if x["inriktning"] == "höger":
            y = random.randint(0, 40)
        else:
            y = random.randint(0, 60)
        if y < 4:
            print(PåverkandeUttalanden[y], "säger", x["partiledare"], Platsuttalanden[random.randint(0, 5)])
            print("Analytiker säger att detta kommer påverka", x["parti"] +  "s resultat i valet...")
            x["Max Röst"] = x["Max Röst"] - 4
            if x["Max Röst"] < x["Min Röst"]:
                x["Max Röst"] = x["Min Röst"]
        
TotalRöster, HParti, VParti, IParti, SParti, OParti, BlockRöster, InriktningsRöster = Rösta() # Definerar alla variablar och sätter igång funktionen


while TotalRöster > 100:
    TotalRöster, HParti, VParti, IParti, SParti, OParti, BlockRöster, InriktningsRöster= Rösta() # Om totala röster är mer än 100, så blir det omröstning


for x in Partier: # Om den här for-loopen inte skulle funnits, hade de procenttalen som visats upp bara varit giltiga ifall totala röster = 100. Lyckligtvis kan den räkna ut det sanna procenttalet och avrunda det till hela tal.
    x["Röster"] = round((x["Röster"]/TotalRöster) * 100)
    
def takeSecond(elem): # Samma funktion som tidigare, men den tar det andra objektet istället för det sista
    return elem[1]
BlockRöster.sort(key=takeSecond, reverse = True) # Sorterar blocken efter röster
InriktningsRöster.sort(key=takeSecond, reverse = True)# Sorterar inriktningarna efter röster


print("Det var " + str(TotalRöster) + "% av invånarna som röstade.") # Totala röster

for x in range(3):
    print(Partier[x-1]["partiledare"], Uttalanden[random.randint(0, len(Uttalanden)-1)], Partier[x]["Röster"],"% av rösterna som", Partier[x-1]["parti"],"fick.") # De tre största partierna går ut med varsitt pressmedelande, med ett random uttalande från listan tidigare

a = 0 
for x in range(len(Partier)): # Den går igenom alla partier baklänges, efter att de är sorterade på röster, och sen gör det minsta partiet ett pressmedelande, med ett random uttalande från listan tidigare, men om det minsta partiet har mindre än 4% röster så går den vidare till det näst minsta, osv.
    if Partier[0 - (x + 1)]["Röster"] > 3 :
        if a == 0:
            print(Partier[0 - (x + 1)]["partiledare"], NegUtt[random.randint(0, len(NegUtt)-1)], Partier[0 - (x + 1)]["Röster"],"% av rösterna som", Partier[0 - (x + 1)]["parti"],"fick.")
            a = 1

print(BlockUtt[random.randint(0, len(BlockUtt)-1)], end=" ") # Här börjar uttalandet som det största blocket gör, med ett random uttalande från listan tidigare
if len(BlockRöster[0][2]) > 1 : # Eftersom att Allpartiet har ett eget block, får de ett eget pressmedelande, eftersom att grammatiken måste ändras, så den kollar hur många partier som är med i det vinnande blocket
    a = len(BlockRöster[0][2]) - 1
    for x in range(a): # Räknar upp alla partiledare i det vinnande blocket
        print(BlockRöster[0][2][x], end=", ") 
    print("och", BlockRöster[0][2][-1], end=" ") # Man följer svenska grammatiska regler, så då används 'och' när man säger det sista objektet i listan 
    print("när de fick reda på att", BlockRöster[0][0] + " är blocket med flest röster, alltså", BlockRöster[0][1], "% av rösterna!") #  BlockRöster[0][0] är blockets namn och BlockRöster[0][1] är blockets röster
else: # Som sagt, Allpartiet har ett eget pressmedelande, bara för att det är svårt att använda korrekt grammatik annars
    print("Jag är odödlig, sa", BlockRöster[0][2][0],"när han fick reda på att ingen av blocken vann, och hans eget parti, Allpartiet fick",BlockRöster[0][1], "% av rösterna!")


 # Samma som med det vinnande blocket måste också det näst största blocket uttala sig, men den här gången har de ingen lista med uttalanden, utan ett hårdkodat meddelande som används varje gång.
if len(BlockRöster[1][2]) > 1 :
    print("Ettan förlora, tvåan vann. Är detta sant? Den här frågan har", end=" ")
    a = len(BlockRöster[1][2]) - 1 # Samma kod som ovan
    for x in range(a):
        print(BlockRöster[1][2][x], end=", ") 
    print("och", BlockRöster[1][2][-1], end=" ")
    print("ställt, eftersom", BlockRöster[1][0] + " kom på en stark andraplats med", BlockRöster[1][1], "% av rösterna!", end="")
else:
    print("Det får duga, sa", BlockRöster[1][2][0],"när han fick reda på att  hans eget parti, Allpartiet fick",BlockRöster[1][1], "% av rösterna, och kom på andraplats.")


if len(BlockRöster[2][2]) > 1 : # Som vanligt, ett hårdkodat meddelande för det förlorande blocket
    a = len(BlockRöster[2][2]) - 1 # Se ovan för förklaring
    for x in range(a):
        print(BlockRöster[2][2][x], end=", ") 
    print("och", BlockRöster[2][2][-1], end=" ")
    print("kommer gråta sig till sömns eftersom deras block,", BlockRöster[2][0] + " kom på en sistaplats, med", BlockRöster[2][1], "% av rösterna!")
else:
    print("Jag vill inte kommentera på denna tragedi, sa", BlockRöster[2][2][0],"när han fick reda på att hans parti, Allpartiet, förlorade mot de andra blocken, med",BlockRöster[2][1], "% av rösterna!")


print(BlockUtt[random.randint(0, len(BlockUtt)-1)], end=" ") # samma koncept som med blocken, fast med inriktningen. Använder ett random uttalande från listan tidigare.
a = len(InriktningsRöster[0][2]) - 1 # Samma kod som för blocken, det enda som ändras är vilken lista man måste rota i
for x in range(a):
    print(InriktningsRöster[0][2][x], end=", ") 
print("och", InriktningsRöster[0][2][-1], end=" ")
print("när de fick reda på att", InriktningsRöster[0][0] + " är inriktningen med flest röster, alltså", InriktningsRöster[0][1], "% av rösterna!")

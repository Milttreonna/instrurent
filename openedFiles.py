import datetime
now = datetime.datetime.now()
userInfo_lst = []
clarinetCost = 1171.99
drumCost = 910.00
pianoCost = 1700.99
violinCost = 699.99
eguitarCost = 899.99
aguitarCost = 439.99
banjoCost = 479.00
saxCost = 3153.99
trumpetCost = 2438.99
congaCost = 269.99

with open("emails.csv", "r") as emailFile:
    emails = emailFile.read().split()
with open("inventory.csv", 'r') as inventoryFile:
    inventory = inventoryFile.read().split()
    dict = {inventory[line]: inventory[line + 1]
            for line in range(0, len(inventory), 2)}
    quantity = inventory[1::2]
    instruments = inventory[::2]
with open("transactions.csv", 'r') as transactionFile:
    transactionhistory = transactionFile.read()
with open("clarinet.txt", 'r') as clarinetFile:
    clarinet = clarinetFile.read()
with open("drums.txt", 'r') as drumFile:
    drums = drumFile.read()
with open("piano.txt", 'r') as pianoFile:
    piano = pianoFile.read()
with open("violin.txt", 'r') as violinFile:
    violin = violinFile.read()
with open("eguitar.txt", 'r') as eguitarFile:
    eguitar = eguitarFile.read()
with open("aguitar.txt", 'r') as aguitarFile:
    aguitar = aguitarFile.read()
with open("banjo.txt", 'r') as banjoFile:
    banjo = banjoFile.read()
with open("trumpet.txt", 'r') as trumpetFile:
    trumpet = trumpetFile.read()
with open("sax.txt", 'r') as saxFile:
    sax = saxFile.read()
with open("conga.txt", 'r') as congaFile:
    conga = congaFile.read()

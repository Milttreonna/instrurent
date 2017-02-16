import datetime

now = datetime.datetime.now()
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
userInfo_lst = []
date_dict = {}
option_dict = {}
item_dict = {}
week_dict = {}
total_dict = {}
return_dict = {}

with open("emails.txt", "r") as emailFile:
    emails = emailFile.read().split()
with open("inventory.txt", 'r') as inventoryFile:
    inventory = inventoryFile.read().split()
    dict = {inventory[line]: inventory[line + 1]
            for line in range(0, len(inventory), 2)}
    quantity = inventory[1::2]
    instruments = inventory[::2]
with open("transactions.txt", 'r') as transactionFile:
    trans_file = transactionFile.readlines()
    # transactionhistory = transactionFile.read()
    # transactionline = transactionhistory.splitlines()
with open("clarinet.txt", 'r') as clarinetFile:
    clarinet = clarinetFile.read()
with open("drums.txt", 'r') as drumFile:
    drums = drumFile.read()
with open("piano.txt", 'r') as pianoFile:
    piano = pianoFile.read()
with open("violin.txt", 'r') as violinFile:
    violin = violinFile.read()
with open("eguitar.txt", 'r') as eguitarFile:
    electricguitar = eguitarFile.read()
with open("aguitar.txt", 'r') as aguitarFile:
    acousticguitar = aguitarFile.read()
with open("banjo.txt", 'r') as banjoFile:
    banjo = banjoFile.read()
with open("trumpet.txt", 'r') as trumpetFile:
    trumpet = trumpetFile.read()
with open("sax.txt", 'r') as saxFile:
    sax = saxFile.read()
with open("conga.txt", 'r') as congaFile:
    conga = congaFile.read()
